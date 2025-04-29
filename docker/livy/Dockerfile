# Usa a imagem base do Apache Spark na versão 3.3.3
FROM docker.io/apache/spark:3.3.3

# Define a variável de ambiente LIVY_HOME como /opt/livy
ENV LIVY_HOME /opt/livy

# Muda para o usuário root para realizar as operações como root
USER root

# Atualiza os pacotes e instalações
RUN apt-get update \
    && echo "update terminado" \ 
    && apt-get install -y --no-install-recommends unzip software-properties-common r-base r-base-dev \  
    && echo "install terminado" \
    && add-apt-repository ppa:deadsnakes/ppa \  
    && apt-get update \
    && apt-get install -y python3.6 \
    && echo "instalação Python 3.6 terminada" \
    && rm -rf /var/lib/apt/lists/* \ 
    && echo "rm terminado" \
    && curl "https://dlcdn.apache.org/incubator/livy/0.8.0-incubating/apache-livy-0.8.0-incubating_2.12-bin.zip" -O \
    && echo "curl terminado" \
    && unzip "apache-livy-0.8.0-incubating_2.12-bin.zip" \
    && echo "unzip terminado" \
    && rm -rf "apache-livy-0.8.0-incubating_2.12-bin.zip" \
    && echo "rm terminado" \
    && mv "apache-livy-0.8.0-incubating_2.12-bin" $LIVY_HOME \
    && echo "mv terminado" \
    && mkdir -p /tmp/spark-events \
    && chmod -R 777 /tmp/spark-events \
    ##&& mkdir $LIVY_HOME/logs \
    ##&& echo "mkdir terminado" \
    && chown -R spark:spark $LIVY_HOME \
    && ln -s $(which python3.6) /usr/bin/python \
    && echo "chown terminado" \
    && curl "https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.2/hadoop-aws-3.3.2.jar" -O \
    && mv hadoop-aws-3.3.2.jar $SPARK_HOME/jars \
    && curl "https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.1026/aws-java-sdk-bundle-1.11.1026.jar" -O \
    && mv aws-java-sdk-bundle-1.11.1026.jar $SPARK_HOME/jars 

# Muda para o usuário spark para execução do serviço
USER spark

# Define o ponto de entrada (entrypoint) como iniciar o servidor Livy e abrir um shell bash
ENTRYPOINT /opt/spark/sbin/start-history-server.sh \
    && /opt/livy/bin/livy-server start \
    && bash
