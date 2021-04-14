import redis
import sys

redisHost = "localhost"
redisPort = 6379
channel = sys.argv[1]

def connect():
    redisConnect = redis.Redis(host=redisHost, port=redisPort, charset="utf-8", decode_responses=True)
    return redisConnect

r = connect()

def sub():
    pubsub = r.pubsub()
    pubsub.subscribe(channel)
    for message in pubsub.listen():
        print(message)



def main():
    sub()

if __name__ == "__main__":
    main()