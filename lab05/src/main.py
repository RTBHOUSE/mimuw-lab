import random
import time

from fastapi import FastAPI
from statsd.defaults.env import StatsClient

app = FastAPI()

statsd = StatsClient()


def calc(cnt: int = None):
    r = 1
    for i in range(1, cnt):
        r *= i
    return r


@app.get("/")
@statsd.timer("app.root")
def root(cnt: int = None):
    statsd.incr("app.root.called")
    if cnt:
        sleep_time = random.randint(0, cnt * 3)
        time.sleep(sleep_time/5)
        statsd.gauge("app.root.cnt", cnt)
        statsd.gauge("app.root.sleep_time", sleep_time)
        statsd.incr("app.root.with_cnt")
        with statsd.timer('app.root.calc'):
            return {"message": f'{calc(cnt)}'}
    return {"message": "No value provided!"}


