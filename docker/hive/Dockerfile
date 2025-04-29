# Use a imagem base do Apache Hive
FROM docker.io/apache/hive:3.1.3

ENV HIVE_HOME /opt/hive

# Muda para o usuário root para realizar as operações como root
USER root

# Define o novo conteúdo do entrypoint.sh
RUN echo '#!/bin/bash' > /entrypoint.sh && \
    echo 'set -x' >> /entrypoint.sh && \
    echo ': ${DB_DRIVER:=derby}' >> /entrypoint.sh && \
    echo 'SKIP_SCHEMA_INIT="${IS_RESUME:-false}"' >> /entrypoint.sh && \
    echo 'function initialize_hive {' >> /entrypoint.sh && \
    echo '  $HIVE_HOME/bin/schematool -dbType $DB_DRIVER -initSchema' >> /entrypoint.sh && \
    echo '  if [ $? -eq 0 ]; then' >> /entrypoint.sh && \
    echo '    echo "Initialized schema successfully.."' >> /entrypoint.sh && \
    echo '  else' >> /entrypoint.sh && \
    echo '    echo "Schema initialization failed!"' >> /entrypoint.sh && \
    echo '    exit 1' >> /entrypoint.sh && \
    echo '  fi' >> /entrypoint.sh && \
    echo '}' >> /entrypoint.sh && \
    echo 'export HIVE_CONF_DIR=$HIVE_HOME/conf' >> /entrypoint.sh && \
    echo 'if [ -d "${HIVE_CUSTOM_CONF_DIR:-}" ]; then' >> /entrypoint.sh && \
    echo '  find "${HIVE_CUSTOM_CONF_DIR}" -type f -exec \' >> /entrypoint.sh && \
    echo '    ln -sfn {} "${HIVE_CONF_DIR}"/ \;' >> /entrypoint.sh && \
    echo '  export HADOOP_CONF_DIR=$HIVE_CONF_DIR' >> /entrypoint.sh && \
    echo '  export TEZ_CONF_DIR=$HIVE_CONF_DIR' >> /entrypoint.sh && \
    echo 'fi' >> /entrypoint.sh && \
    echo 'export HADOOP_CLIENT_OPTS="$HADOOP_CLIENT_OPTS -Xmx1G $SERVICE_OPTS"' >> /entrypoint.sh && \
    echo 'if [[ "${SKIP_SCHEMA_INIT}" == "false" ]]; then' >> /entrypoint.sh && \
    echo '  #Check schema initialization' >> /entrypoint.sh && \
    echo '  $HIVE_HOME/bin/schematool -dbType postgres -info' >> /entrypoint.sh && \
    echo '  if [ $? -eq 1 ]; then' >> /entrypoint.sh && \
    echo '    # handles schema initialization' >> /entrypoint.sh && \
    echo '    initialize_hive' >> /entrypoint.sh && \
    echo '  fi' >> /entrypoint.sh && \
    echo 'fi' >> /entrypoint.sh && \
    echo 'if [ "${SERVICE_NAME}" == "hiveserver2" ]; then' >> /entrypoint.sh && \
    echo '  export HADOOP_CLASSPATH=$TEZ_HOME/*:$TEZ_HOME/lib/*:$HADOOP_CLASSPATH' >> /entrypoint.sh && \
    echo 'elif [ "${SERVICE_NAME}" == "metastore" ]; then' >> /entrypoint.sh && \
    echo '  export METASTORE_PORT=${METASTORE_PORT:-9083}' >> /entrypoint.sh && \
    echo 'fi' >> /entrypoint.sh && \
    echo 'exec $HIVE_HOME/bin/hive --skiphadoopversion --skiphbasecp --service $SERVICE_NAME' >> /entrypoint.sh

# Atualiza os pacotes e instalações
RUN apt-get update \
    && apt-get install -y curl \
    && chown -R hive:hive /opt/hive \
    && echo "chown terminado" \
    && curl "https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.1.0/hadoop-aws-3.1.0.jar" -O \
    && mv hadoop-aws-3.1.0.jar /opt/hive/lib \
    && curl "https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.271/aws-java-sdk-bundle-1.11.271.jar" -O \
    && mv aws-java-sdk-bundle-1.11.271.jar /opt/hive/lib 

ENV HADOOP_CLASSPATH=$HADOOP_CLASSPATH:/opt/hadoop/share/hadoop/tools/lib/*

USER hive