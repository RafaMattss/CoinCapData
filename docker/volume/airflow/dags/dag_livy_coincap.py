# dag_livy_coincap.py

from airflow import DAG
from airflow.providers.apache.livy.operators.livy import LivyOperator
from airflow.operators.python import PythonOperator
from airflow.models import Connection
from airflow import settings
from sqlalchemy.orm import Session
from datetime import datetime

def criar_conexao_livy():
    session: Session = settings.Session()
    
    conn_id = "livy_spark_conn"
    existing = session.query(Connection).filter(Connection.conn_id == conn_id).first()

    if existing:
        session.delete(existing)
        session.commit()

    conn = Connection(
        conn_id=conn_id,
        conn_type='http',
        host='livy',
        port=8998,
        schema='http'
    )
    session.add(conn)
    session.commit()
    session.close()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 4, 28),
}

dag = DAG(
    'dag_coincap_livy',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

criar_conexao = PythonOperator(
    task_id='criar_conexao_livy',
    python_callable=criar_conexao_livy,
    dag=dag
)

livy_job = LivyOperator(
    task_id='executar_pipeline_coincap',
    dag=dag,
    livy_conn_id='livy_spark_conn',
    file='s3a://pipelines/pipeline_coincap.py',
    executor_cores=2,
    num_executors=2,
    conf={
        'spark.dynamicAllocation.enabled': 'true'
    },
    args=["07c2e47d598ddac50c6fcff6ece0d23cae45a79f0d489fb5c9fb3e906ad9f889"]
)

criar_conexao >> livy_job
