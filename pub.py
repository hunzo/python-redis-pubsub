import redis
import json
import sys

redisHost = "localhost"
redisPort = 6379
channel = sys.argv[1]
msg = sys.argv[2]

r = redis.Redis(host=redisHost, port=redisPort, charset="utf-8", decode_responses=True)

def pub():
    data = {
        "message": msg,
        "from": "me",
        "to": "you"
    }
    r.publish(channel, json.dumps(data))

def main():
    pub()

if __name__ == "__main__":
    main()