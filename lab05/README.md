# Application monitoring with graphite and grafana

## Task 1

Write a simple application that sometimes (once every 30 calls) processes the request slower.
Monitor number of requests and processing time.
Create dashboard in grafana that will present: 
- mean, 90-percentile and max of processing time
- number of requests

## Run grafana with graphite in docker

### Run grafana

```bash
docker pull grafana/grafana-oss

docker run -d --network=host --name grafana grafana/grafana-oss
```

(add sudo if user is not in docker group)

### Run graphite

```bash
docker pull  graphiteapp/graphite-statsd

docker run -d \
 --name graphite \
 --restart=always \
 --network=host \
 graphiteapp/graphite-statsd
```

Log into grafana:
http://127.0.0.1:3000/

Add datasource with type: graphite and ip address: http://localhost

### Check

Send simple single metric:

```bash
echo -n "test:20|c" | nc -w 1 -u 127.0.0.1 8125;
```

verify on graphite web:
http://localhost/render?from=-10mins&until=now&target=stats.test

verify on grafana:
http://localhost:3000/render?from=-10mins&until=now&target=stats.test

## Task 2

- Add /health endpoint. 
- Create LB (similar to lab03) which checks created endpoint
- Verify if /health returns unhealthy state - LB will not forward traffic
- Add HEALTHCHECK in Dockerfile

