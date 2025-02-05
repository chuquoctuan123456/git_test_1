# Sử dụng image cơ bản của bạn
FROM  tuancq/airflow:latest

# Cập nhật pip và cài đặt astronomer-cosmos
RUN  pip install --no-cache-dir astronomer-cosmos