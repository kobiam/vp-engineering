# Redis Intro

This is an intro to Redis.io in-memory database, key-value store, cache and message broker
#

## Redis Common Commands

`INFO` command returns information and statistics about the server.

`SET` Set key to hold the string value.

`GET` Get the value of key.

`BGSAVE` Save the DB in background.

`SCAN` iterates the set of keys in the currently selected Redis database.

`HSET` Sets `field` in the hash stored at key to value.

`HGET` Returns the value associated with `field` in the hash stored at key.

`PING` This command is often used to test a connection.

`KEYS` Returns all keys matching pattern.

`BLPOP` is a blocking list pop primitive.

`SUBSCRIBE` Subscribes the client to the specified channels.

`PUBLISH` Posts a message to the given channel.


<a href="https://redis.io/commands">Redis Commands</a> 

#

## Redis Benchmark Utility

Redis includes the redis-benchmark utility that simulates running commands

try this command: `redis-benchmark -n 100`


<a href="https://redis.io/topics/benchmarks#how-fast-is-redis">How fast is Redis?</a> 

#

## Redis Configuration

Redis have a configuration file useally called `redis.conf` and it used to configure your redis nodes.

to alter `redis.conf` you'll need to restart the node after the change but it is also possiable to do it <strong>without restart</strong> using `CONFIG SET` and `CONFIG GET`

you'll have to update both the runtime and the `redis.conf` file to ensure changes will take effect after restart.

this is what `redis.conf` looks like:

`save 900 1`

`save 300 10`

to change on runtime example:

900 seconds if there is at least 1 change to the dataset, and after 300 seconds if there are at least 10 changes to the dataset.

`CONFIG SET SAVE "900 1 300 10"`

either way you need to update on both `redis.conf` and runtime in nodes.


<a href="https://redis.io/topics/config">Redis Configuration</a> 

to start the server with `redis.conf`

`src/redis-server redis.conf &`

#

save config without restart

All the configuration parameters set using `CONFIG SET` are immediately loaded by Redis and will take effect starting with the next command executed.

example: `CONFIG SET SAVE "900 1 300 10" `


<a href="https://redis.io/commands/config-set">CONFIG SET</a>

#

## Redis persistence

<strong>AOF </strong>logs every write operation received by the server, that will be played again at server statup.

<strong>RDB </strong>persistence performs point-in-time snapshots of your dataset at specified intervals.

to create a snapshot command at redis-cli: `SAVE`
to create a snapshot with intervals: `SAVE 60 1000`

that will save it every 60 seconds with at least 1000 keys changed.

snapshots are in file: `dump.rdb`

<strong>Append-only file </strong>every time Redis receives a command that change the dataset it will append to the AOF.

when Redis is restarted it will re-play the AOF to rebuild the state.

<strong>AOF Rewrite </strong>Redis is able to automatically rewrite the AOF in background when it gets too big.

if no rewrite of the log was performed in the meantime you can still save your data set just stopping the server, removing the latest command, and restarting Redis again.

AOF gets bigger and bigger as write operations are performed.

Redis is able to rebuild the AOF in the background without interrupting service to clients.

Whenever you issue a `BGREWRITEAOF` Redis will write the shortest sequence of commands needed to rebuild the current dataset in memory.


<a href="https://redis.io/topics/persistence">Redis Persistence</a>

#

## Redis logs

Setting the Log Location in redis.conf

`sudo vi redis.conf`

Locate the `logfile` line:

`logfile /var/log/redis/redis-server.log`

#

## Redis replication

replication: it allows replica Redis instances to be exact copies of master instances.

(excluding the high availability features provided as an additional layer by Redis Cluster or Redis Sentinel)

The replica will automatically reconnect to the master every time the link breaks, and will attempt to be an exact copy of it regardless of what happens to the master.

This system works using three main mechanisms:

1. When a master and a replica instances are well-connected, the master keeps the replica updated by sending a stream of commands to the replica, in order to replicate the effects on the dataset happening in the master side due to: client writes, keys expired or evicted, any other action changing the master dataset.

2. When the link between the master and the replica breaks, for network issues or because a timeout is sensed in the master or the replica, the replica reconnects and attempts to proceed with a partial resynchronization: it means that it will try to just obtain the part of the stream of commands it missed during the disconnection.

3. When a partial resynchronization is not possible, the replica will ask for a full resynchronization. This will involve a more complex process in which the master needs to create a snapshot of all its data, send it to the replica, and then continue sending the stream of commands as the dataset changes.


<a href="https://redis.io/topics/replication">Redis replication</a>

#

## Eviction policies

Redis stores its data, called keys, in memory only and uses eviction policies to free memory in order to write new data.

Eviction policies fall into two main categories: general policies that apply to all keys and policies that use a Time to Live (TTL) expiration value.

General policies apply to any keys that do not have expiration set.

**Policy and Description**

`noeviction` Returns an error if the memory limit has been reached when trying to insert more data

`allkeys-lru` Evicts the least recently used keys out of all keys

`allkeys-lfu` Evicts the least frequently used keys out of all keys

`allkeys-random` Randomly evicts keys out of all keys

`volatile-lru` Evicts the least recently used keys out of all keys with an “expire” field set

`volatile-lfu` Evicts the least frequently used keys out of all keys with an “expire” field set

`volatile-random` Randomly evicts keys with an “expire” field set

`volatile-ttl` Evicts the shortest time-to-live keys out of all keys with an “expire” field set.


<a href="https://www.digitalocean.com/docs/databases/redis/how-to/choose-eviction-policies/">Redis Eviction Policies</a> 

#

## Redis cluster and Sentinel

Redis Sentinel will monitor your cluster and handle <strong>automatic failovers</strong> of instances within the cluster without going to a full cluster solution.

Redis Cluster is a full cluster solution that <strong>splits your database on multiple nodes</strong> and better RAM consumption.

To set up a Redis cluster you'll need at least 3 Redis instances in the cluster.

This is a good option for HA concerns.

Redis cluster splits your data across instances and provide automatic management and replication.


<a href="https://redis.io/topics/sentinel">Redis Sentinel</a> and <a href="https://docs.redislabs.com/latest/rs/administering/new-cluster-setup/">Redis Cluster</a>
