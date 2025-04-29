FROM apache/airflow:2.7.3

USER root

# Instalação do JDK (Java Development Kit) necessário para o Hive e Hadoop
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean

# Diretório de instalação do Hive
ENV HIVE_HOME /opt/hive
ENV JAVA_HOME /usr/lib/jvm/java-1.11.0-openjdk-amd64

# Diretório de instalação do Hadoop
ENV HADOOP_HOME /opt/hadoop

# Baixar e extrair o Apache Hadoop
RUN curl -O https://archive.apache.org/dist/hadoop/core/hadoop-3.1.0/hadoop-3.1.0.tar.gz && \
    tar xzf hadoop-3.1.0.tar.gz && \
    mv hadoop-3.1.0 $HADOOP_HOME && \
    rm hadoop-3.1.0.tar.gz

# Definir uma variável de ambiente HADOOP_CONF_DIR para apontar para a configuração do Hadoop
ENV HADOOP_CONF_DIR $HADOOP_HOME/etc/hadoop

# Baixar e extrair o Apache Hive
RUN curl -O https://archive.apache.org/dist/hive/hive-3.1.3/apache-hive-3.1.3-bin.tar.gz && \
    tar xzf apache-hive-3.1.3-bin.tar.gz && \
    mv apache-hive-3.1.3-bin $HIVE_HOME && \
    rm apache-hive-3.1.3-bin.tar.gz

# Adicionar o diretório binário do Hive ao PATH
ENV PATH $HIVE_HOME/bin:$PATH

# Definir permissões para o usuário airflow acessar o Hive e o Hadoop
RUN chown -R airflow $HIVE_HOME $HADOOP_HOME

USER airflow

# Copiar requirements.txt e instalar as dependências
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
