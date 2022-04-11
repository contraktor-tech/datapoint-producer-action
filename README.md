# README.md

# Datapoint Producer Action

[![Quality Gate Status](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_datapoint-producer-action&metric=alert_status&token=491b25a0aa08128e2abe0c76a3f8e00a84cc6c20)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_datapoint-producer-action)
[![Bugs](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_datapoint-producer-action&metric=bugs&token=491b25a0aa08128e2abe0c76a3f8e00a84cc6c20)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_datapoint-producer-action)
[![Vulnerabilities](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_datapoint-producer-action&metric=vulnerabilities&token=491b25a0aa08128e2abe0c76a3f8e00a84cc6c20)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_datapoint-producer-action)
[![Code Smells](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_datapoint-producer-action&metric=code_smells&token=491b25a0aa08128e2abe0c76a3f8e00a84cc6c20)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_datapoint-producer-action)
[![Coverage](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_datapoint-producer-action&metric=coverage&token=491b25a0aa08128e2abe0c76a3f8e00a84cc6c20)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_datapoint-producer-action)
[![Lines of Code](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_datapoint-producer-action&metric=ncloc&token=491b25a0aa08128e2abe0c76a3f8e00a84cc6c20)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_datapoint-producer-action)

This action was created to send metrics to [Influxdb](https://www.influxdata.com/)

```yaml
inputs:
  influxdb-token:
    description: 'token to access influxdb instance'
    require: true
  influxdb-bucket:
    description: 'influxdb bucket, used as metrics aggragetor'
    require: false
    default: 'deployment'
  influxdb-url:
    description: 'url to influxdb instance'
    require: true
  influxdb-org:
    description: 'organizarion used by influxdb'
    require: false
    default: 'Contraktor'
  app:
    description: 'application that was affected'
    require: true
```
