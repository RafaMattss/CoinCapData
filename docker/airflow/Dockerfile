FROM apache/airflow:2.7.3

USER root

RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean

ENV HIVE_HOME /opt/hive
ENV JAVA_HOME /usr/lib/jvm/java-1.11.0-openjdk-amd64

ENV HADOOP_HOME /opt/hadoop

RUN curl -O https://archive.apache.org/dist/hadoop/core/hadoop-3.1.0/hadoop-3.1.0.tar.gz && \
    tar xzf hadoop-3.1.0.tar.gz && \
    mv hadoop-3.1.0 $HADOOP_HOME && \
    rm hadoop-3.1.0.tar.gz

ENV HADOOP_CONF_DIR $HADOOP_HOME/etc/hadoop

RUN curl -O https://archive.apache.org/dist/hive/hive-3.1.3/apache-hive-3.1.3-bin.tar.gz && \
    tar xzf apache-hive-3.1.3-bin.tar.gz && \
    mv apache-hive-3.1.3-bin $HIVE_HOME && \
    rm apache-hive-3.1.3-bin.tar.gz

ENV PATH $HIVE_HOME/bin:$PATH

RUN chown -R airflow $HIVE_HOME $HADOOP_HOME

USER airflow

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

USER root
