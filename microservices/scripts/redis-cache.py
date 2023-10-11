import redis

# Create a Redis client
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)  # Adjust the connection details

# Get and print a cache value
cache_key = 'my_cache_key'
cache_value = redis_client.get(cache_key)

if cache_value:
    print(f'Cache value for {cache_key}: {cache_value.decode("utf-8")}')
else:
    print(f'Cache key {cache_key} not found.')
