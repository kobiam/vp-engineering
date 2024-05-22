# Install Redis master (Ubuntu 20.04.1)

Download Redis 6.0.9

`wget https://download.redis.io/releases/redis-6.0.9.tar.gz`

`tar xzf redis-6.0.9.tar.gz`

`cd redis-6.0.9`

`sudo apt-get update -y`

`sudo apt-get install make gcc tcl build-essential -y`

if there is another error like "fatal error: jemalloc/jemalloc.h: No such file or directory"

just run `make distclean`

`make`

#

disable ufw

`sudo ufw status`

`sudo ufw stop`

#

edit `redis.conf`

change to those values

`protected-mode no`

The following line should be commented

`bind 127.0.0.1`

#

start redis server using the <strong>redis.conf</strong> `src/redis-server redis.conf &`

connect to the redis server

`src/redis-cli -p 6379`

## Install Redis replicate (Ubuntu 20.04.1)

Download Redis 6.0.9

`wget https://download.redis.io/releases/redis-6.0.9.tar.gz`

`tar xzf redis-6.0.9.tar.gz`

`cd redis-6.0.9`

`sudo apt-get update -y`

`sudo apt-get install make gcc tcl build-essential -y`

if there is another error like "fatal error: jemalloc/jemalloc.h: No such file or directory"

just run `make distclean`

`make`

#

disable ufw

`sudo ufw status`

`sudo ufw stop`

#

edit `redis.conf`

find <strong>port</strong> and change it from <strong>6379</strong> to `6380`

find `replicateof` uncomment it and change to [master ip] and [master port]

edit `redis.conf`

change to those values

`protected-mode no`

The following line should be commented

`bind 127.0.0.1`

#

start the replicate server `src/redis-server redis.conf &`

connect to the replicate server

`src/redis-cli -p 6380`

## Install Redis cli (Ubuntu 20.04.1)

`sudo apt-get install redis-tools -y`

start redis cli

`redis-cli`

connect to server:

`connect [server-ip] [server-port]`
