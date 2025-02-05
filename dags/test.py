from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import socket
import time

# Hàm Python để test worker
def test_worker(task_name):
    worker_name = socket.gethostname()  # Lấy tên máy worker đang chạy task
    print(f"🔥 Task {task_name} đang chạy trên worker: {worker_name}")
    time.sleep(3)  # Giả lập task chạy mất 3 giây
    print(f"✅ Task {task_name} đã hoàn thành trên {worker_name}")

# Cấu hình mặc định của DAG
default_args = {
    "owner": "TUANTUAN",
    "depends_on_past": False,
    "start_date": datetime(2024, 2, 1),
    "retries": 1,
    "retry_delay": timedelta(seconds=10),
}

# Khởi tạo DAG
dag = DAG(
    "test_workers",
    default_args=default_args,
    description="DAG kiểm tra nhiều worker",
    schedule_interval=None,  # Chạy thủ công
    catchup=False,
)

# Task 1
task_1 = PythonOperator(
    task_id="test_task_1",
    python_callable=test_worker,
    op_args=["Task 1"],
    dag=dag,
)

# Task 2
task_2 = PythonOperator(
    task_id="test_task_2",
    python_callable=test_worker,
    op_args=["Task 2"],
    dag=dag,
)

# Task 3
task_3 = PythonOperator(
    task_id="test_task_3",
    python_callable=test_worker,
    op_args=["Task 3"],
    dag=dag,
)

# Chạy song song 2 task trước, sau đó chạy task 3
[task_1, task_2] >> task_3
# nmbqhvk-ns46391