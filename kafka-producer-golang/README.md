# Kafka producer in Go

## Start Kafka broker in Docker

```sh
docker run -p 9092:9092 -it apache/kafka
```

## Start Kafka broker in Podman

```sh
podman run -p 9092:9092 -it apache/kafka
```

## Start Kafka producer in Go

```sh
go mod init kafka-producer/main
go mod tidy
go run .
```
