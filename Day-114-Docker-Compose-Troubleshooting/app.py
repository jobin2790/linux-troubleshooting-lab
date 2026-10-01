from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/")
def home():
    return "Docker Compose App is running\n"

@app.route("/health")
def health():
    try:
        r.ping()
        return "OK\n"
    except Exception:
        return "Redis unavailable\n", 503

@app.route("/count")
def count():
    count = r.incr("visits")
    return f"Visits: {count}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
