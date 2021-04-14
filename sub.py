import redis
import sys
import json

redisHost = "localhost"
redisPort = 6379
channel = sys.argv[1]

def connect():
    redisConnect = redis.Redis(host=redisHost, port=redisPort, charset="utf-8", decode_responses=True, password="testpassword")
    return redisConnect

r = connect()

def sub():
    pubsub = r.pubsub()
    pubsub.subscribe(channel)
    for message in pubsub.listen():

        print(message)
        print(message["type"])

        if message["type"] == "message":
            a = json.loads(message["data"])
            print(type(a))
            print(a["message"])


def main():
    try:
        sub()
    except Exception as e:
        print(f"Error => {e}")

if __name__ == "__main__":
    main()