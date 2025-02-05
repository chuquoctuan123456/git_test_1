from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

DBT_PROJECT_DIR = "/opt/airflow/dbt_projects/project_1"
DBT_PROFILES_DIR = "/opt/airflow/dbt_projects/project_1"

with DAG(
    dag_id="dbt_bash_dag_okok",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    # Chạy `dbt debug` để kiểm tra kết nối
    dbt_debug = BashOperator(
        task_id="dbt_debug",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt debug --profiles-dir {DBT_PROFILES_DIR}"
    )

    # # Chạy `dbt deps` để tải dependencies
    # dbt_deps = BashOperator(
    #     task_id="dbt_deps",
    #     bash_command=f"cd {DBT_PROJECT_DIR} && dbt deps"
    # )

    # # Chạy `dbt run` để thực thi model
    # dbt_run = BashOperator(
    #     task_id="dbt_run",
    #     bash_command=f"cd {DBT_PROJECT_DIR} && dbt run --profiles-dir {DBT_PROFILES_DIR}"
    # )

    # # Chạy `dbt test` để kiểm tra dữ liệu
    # dbt_test = BashOperator(
    #     task_id="dbt_test",
    #     bash_command=f"cd {DBT_PROJECT_DIR} && dbt test --profiles-dir {DBT_PROFILES_DIR}"
    # )

    # # Sắp xếp thứ tự chạy
    dbt_debug 
    #>> dbt_deps >> dbt_run >> dbt_test
