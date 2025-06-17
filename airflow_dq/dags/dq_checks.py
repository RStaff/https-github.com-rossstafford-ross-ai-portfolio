from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.exceptions import AirflowFailException
from datetime import datetime
import sqlite3, pandas as pd

DB = "/opt/airflow/airflow.db"

def row_check():
    n = pd.read_sql("SELECT COUNT(*) AS n FROM pos_sales_demo",
                    sqlite3.connect(DB)).iloc[0,0]
    if n < 1000:
        raise AirflowFailException(f"Row count too low: {n}")

def null_check():
    nulls = pd.read_sql(
        "SELECT SUM(CASE WHEN visits IS NULL THEN 1 END) AS n FROM pos_sales_demo",
        sqlite3.connect(DB)).iloc[0,0]
    if nulls > 0:
        raise AirflowFailException(f"visits NULLs: {nulls}")

with DAG("dq_checks",
         start_date=datetime(2025, 6, 1),
         catchup=False,
         schedule_interval="@daily") as dag:
    rc = PythonOperator(task_id="row_count",  python_callable=row_check)
    nc = PythonOperator(task_id="null_ratio", python_callable=null_check)
    rc >> nc
