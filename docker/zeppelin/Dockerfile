FROM docker.io/apache/zeppelin:0.8.2

# Muda para o usuário root para realizar as operações como root
USER root

# Atualiza os pacotes e instalações
RUN apt-get update \
    && apt-get install -y curl \
    && curl "https://repo.maven.apache.org/maven2/org/apache/hive/hive-jdbc/3.1.3/hive-jdbc-3.1.3.jar" -O \
    && mv hive-jdbc-3.1.3.jar /zeppelin/interpreter/jdbc \
    && curl "https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-common/3.1.0/hadoop-common-3.1.0.jar" -O \
    && mv hadoop-common-3.1.0.jar /zeppelin/interpreter/jdbc \
    && curl "https://repo1.maven.org/maven2/org/apache/thrift/libthrift/0.9.3/libthrift-0.9.3.jar" -O \
    && mv libthrift-0.9.3.jar /zeppelin/interpreter/jdbc \
    && curl "https://repo1.maven.org/maven2/org/apache/hive/hive-service-rpc/3.1.3/hive-service-rpc-3.1.3.jar" -O \
    && mv hive-service-rpc-3.1.3.jar /zeppelin/interpreter/jdbc \
    && curl "https://repo1.maven.org/maven2/org/apache/hive/hive-shims/3.1.3/hive-shims-3.1.3.jar" -O \
    && mv hive-shims-3.1.3.jar /zeppelin/interpreter/jdbc \
    && curl "https://repo1.maven.org/maven2/org/apache/hive/hive-metastore/3.1.3/hive-metastore-3.1.3.jar" -O \
    && mv hive-metastore-3.1.3.jar /zeppelin/interpreter/jdbc \
    && curl "https://repo1.maven.org/maven2/org/apache/hive/hive-serde/3.1.3/hive-serde-3.1.3.jar" -O \
    && mv hive-serde-3.1.3.jar /zeppelin/interpreter/jdbc \
    && curl "https://repo1.maven.org/maven2/org/apache/hive/hive-service/3.1.3/hive-service-3.1.3.jar" -O \
    && mv hive-service-3.1.3.jar /zeppelin/interpreter/jdbc \
    && curl "https://repo1.maven.org/maven2/org/apache/hive/hive-common/3.1.3/hive-common-3.1.3.jar" -O \
    && mv hive-common-3.1.3.jar /zeppelin/interpreter/jdbc \
    && curl "https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.4.13/httpcore-4.4.13.jar" -O \
    && mv httpcore-4.4.13.jar /zeppelin/interpreter/jdbc \
    && curl "https://repo1.maven.org/maven2/org/apache/zookeeper/zookeeper/3.4.6/zookeeper-3.4.6.jar" -O \
    && mv zookeeper-3.4.6.jar /zeppelin/interpreter/jdbc \
    && curl "https://repo1.maven.org/maven2/org/apache/curator/curator-framework/2.12.0/curator-framework-2.12.0.jar" -O \
    && mv curator-framework-2.12.0.jar /zeppelin/interpreter/jdbc \
    && curl "https://repo1.maven.org/maven2/org/apache/curator/curator-client/2.12.0/curator-client-2.12.0.jar" -O \
    && mv curator-client-2.12.0.jar /zeppelin/interpreter/jdbc \
    && curl "https://repo1.maven.org/maven2/org/apache/curator/curator-recipes/2.12.0/curator-recipes-2.12.0.jar" -O \
    && mv curator-recipes-2.12.0.jar /zeppelin/interpreter/jdbc \
    && curl "https://repo1.maven.org/maven2/com/google/guava/guava/11.0.2/guava-11.0.2.jar" -O \
    && mv guava-11.0.2.jar /zeppelin/interpreter/jdbc