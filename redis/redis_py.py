'''redis_py module'''
import redis

r = redis.Redis(
host='172.19.0.2',
port=6379,
password='')

p = r.pubsub()

# set key name with value
r.set('name', 'bruno')
# get the value of key name
getName = r.get('name')
print(getName)

# set key team with value
r.set('team', 'united')
# get the value of key team
getTeam = r.get('team')
print(getTeam)

# increment key address with value 200
r.incrby('address', 200)
# get the value of key address incremented
getAddress = r.get('address')
print(getAddress)

# set more than one key-value using mset
r.mset({'street': 'united lane', 'city': 'manchester'})
getStreet = r.mget('street', 'city')
print(getStreet)

# create a key-value pair within a hash
# hash is user:18
r.hmset('user:18', {'firstname': 'bruno', 'team': 'united', 'city': 'manchester'})
# get all the keys-values pairs
getAll = r.hgetall('user:18')
print(getAll)

# Redis Lists are lists of strings, sorted by isertion order.
r.rpush('rivals', 'liverpool', 'leeds', 'city')
# push leeds to the end of the list
r.rpush('rivals', 'leeds')
# push city to the beginning of the list
r.rpush('rivals', 'city')
# push out the last item on the list
r.rpop('rivals')
# output the entire list from 0 to negative 1 (result is everything in the list)
getRivals = r.lrange('rivals', 0, -1)
print(getRivals)

# add specified members to a set stored at key.
r.sadd('shirts', 'white', 'red', 'blue')

# return if a member is a member of the set stored at key.
# and output all the members of the set
r.smembers('shirts')

# Publish and subscribe

# subscribe to messages and news channels
p.subscribe('messages', 'news')

# publish a message to messages channel
r.publish('messages', 'How are you?')
