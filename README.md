# 🚀 Projeto Big Data Coincap

Bem-vindo ao projeto de ambiente Big Data com foco em ingestão, transformação e análise de dados de criptomoedas provenientes da  [API Coincap](https://docs.coincap.io/).

Este repositório foi desenvolvido com o objetivo de demonstrar a criação de um ecossistema Big Data completo utilizando ferramentas como **Docker**, **Spark**, **Hive**, **Airflow**, **Zeppelin**, **Livy** e **MinIO**, além da integração com **Python** para desenvolvimento do pipeline de ingestão e transformação de dados.

---

## 🧩 Sobre o Projeto

O projeto contempla dois grandes focos:

1. **Criação do ambiente Big Data** com todas as ferramentas necessárias para rodar pipelines analíticos em um ambiente local e integrado via Docker.
2. **Execução de um fluxo ETL completo**, que realiza:
   - Extração de dados da API Coincap.
   - Transformações com Spark.
   - Armazenamento em tabelas Hive para posterior análise.

---

## 📥 Como clonar o projeto

Para obter este repositório em sua máquina local, utilize:

```bash
git clone https://github.com/RafaMattss/CoinCapData.git
cd CoinCapData
```

---

## 📚 Documentações

O projeto possui duas documentações específicas separadas na pasta `docs/`:

- 📁 [`docs/ambiente`](docs/ambiente/README.md): contém **instruções completas para configurar e iniciar o ambiente Docker**, incluindo todos os serviços necessários.
- 📁 [`docs/fluxo`](docs/fluxo/README.md): explica **todo o fluxo ETL** desde a extração da API até a geração das tabelas Hive, incluindo notebooks Zeppelin e código Python envolvido.

---

## 🛠️ Como começar

1. **Configure o ambiente:**  
   Acesse o [`README de ambiente`](docs/ambiente/README.md) e siga as instruções para iniciar o Docker com os serviços integrados.

2. **Execute o fluxo ETL Coincap:**  
   Depois que o ambiente estiver em funcionamento, acesse o [`README de fluxo`](docs/fluxo/README.md) para entender e executar o pipeline que coleta e processa os dados da API Coincap.

3. **PowerBI final:**
    Foi criado um powerbi simples com a extração dos dados no dia 29/04/2025 que pode ser acessado no seguinte link: [`Google Drive`](https://drive.google.com/drive/folders/1tu69so6-fguUtdb1rzbPhxoWlOSLulwW?usp=sharing)
---

Sinta-se à vontade para explorar, testar, adaptar e contribuir com este projeto!
