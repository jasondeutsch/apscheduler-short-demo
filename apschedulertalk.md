This talk is structured so you can follow a long.

---

## APScheduler


APScheduler has three built-in scheduling systems you can use:

Cron-style scheduling (with optional start/end times)

Interval-based execution (runs jobs on even intervals, with optional start/end times)

One-off delayed execution (runs jobs once, on a set date/time)


---


#### tl;dr schedule your python code to run later.

---


## Crons

daily payments tasks

recurring report generation

automated backups

---

## Use case: intervallic scheduling 


---

## Simple Example

```sh
mkdir apsched && cd appsched
python3 -m venv venv
pip install apscheduler
vim simple.py
```

---

Basic BG scheduler

```python
from apscheduler.schedulers.background 
     import BackgroundScheduler

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(lambda: scheduler.print_jobs(), 
    'interval', seconds=5)
scheduler.start()
```
---


What's wrong here?

---



```
while True:
    cmd = input()
    if cmd == 'x':
        scheduler.shutdown()
        break
```

---


This is essentially the same as BlockScheduler


---


## APScheduler Components

---


![APScheduler Class Graph](https://enqueuezero.com/static/images/apscheduler-oo.png)

<em><small>source: https://enqueuezero.com/concrete-architecture/apscheduler.html</small></em>


---

### Scheduler

Offers a couple of scheduling schemes:

1. cron style
2. interval based
3. One off/delayed execution

### Trigger



(back to code)

let's use a simple 