from airflow import DAG
from cosmos import DbtDag, ProjectConfig, ProfileConfig
from datetime import datetime

with DAG(
    dag_id="dbt_cosmos_dag",  
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    dbt_dag = DbtDag(
        dag_id="dbt_project_1",  
        project_config=ProjectConfig("/opt/airflow/dbt_projects/project_1"),
        profile_config=ProfileConfig(
            profile_name="project_1",  
            target_name="dev",  
            profiles_yml_filepath="/home/airflow/.dbt/profiles.yml"
        )
    )

    dbt_dag 
