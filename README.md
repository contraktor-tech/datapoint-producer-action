# README.md

# Datapoint Producer Action

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
