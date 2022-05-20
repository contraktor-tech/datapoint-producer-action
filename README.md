# README.md

# Datapoint Producer Action

[![Quality Gate Status](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_datapoint-producer-action&metric=alert_status&token=491b25a0aa08128e2abe0c76a3f8e00a84cc6c20)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_datapoint-producer-action)
[![Bugs](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_datapoint-producer-action&metric=bugs&token=491b25a0aa08128e2abe0c76a3f8e00a84cc6c20)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_datapoint-producer-action)
[![Vulnerabilities](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_datapoint-producer-action&metric=vulnerabilities&token=491b25a0aa08128e2abe0c76a3f8e00a84cc6c20)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_datapoint-producer-action)
[![Code Smells](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_datapoint-producer-action&metric=code_smells&token=491b25a0aa08128e2abe0c76a3f8e00a84cc6c20)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_datapoint-producer-action)
[![Coverage](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_datapoint-producer-action&metric=coverage&token=491b25a0aa08128e2abe0c76a3f8e00a84cc6c20)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_datapoint-producer-action)
[![Lines of Code](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_datapoint-producer-action&metric=ncloc&token=491b25a0aa08128e2abe0c76a3f8e00a84cc6c20)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_datapoint-producer-action)

Esta action foi criada para enviar métricas de rollback e deploy para [Influxdb](https://www.influxdata.com/)

## Inputs
- **influxdb-token** → token de acesso a instancia do InfluxDB. Definição obrigatória.
- **influxdb-bucket** → bucket do InfluxDB, usado para agregar as métricas. Definição não obrigatória. **Valor default**: 'deployment'
- **influxdb-url** → url da instância do InfluxDB. Definição obrigatória.
- **influxdb-org** → organização que está usando o InfluxDB. Definição não obrigatória. **Valor default**: 'Contraktor'
- **app** → aplicação. Definição obrigatória.

## Etapas
- Verifica se o Python está instalado. Essa verificação não ocorre em docker-runner.
- Instala dependências
- Executa o script e envia as métricas para o InfluxDB

## Como usar
Acesse a documentação no [Confluence](https://contraktor.atlassian.net/wiki/spaces/CONTRAKTOR/pages/16842753/Actions#datapoint-producer-action) para ver uma pipeline de exemplo.

- **métricas de rollback**
```
- name: send rollback metric to influxdb
  uses: contraktor-tech/datapoint-producer-action@v2
  if: |
    contains(github.event.head_commit.message, 'rollback') ||
    contains(github.event.head_commit.message, 'revert')
  with:
    influxdb-token: XXXX
    influxdb-url: XXXX
    influxdb-measurement: 'rollback'
    app: '<nome-aplicação>'
```

- **métricas de deploy**
```
- name: send deploy metric to influxdb
  uses: contraktor-tech/datapoint-producer-action@v2
  if: |
    !contains(github.event.head_commit.message, 'rollback') &&
    !contains(github.event.head_commit.message, 'revert')
  with:
    influxdb-token: XXXX
    influxdb-url: XXXX
    influxdb-measurement: 'deploy'
    app: '<nome-aplicação>'
```



