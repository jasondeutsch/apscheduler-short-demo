# APScheduler
---

## APScheduler


Advanced Python Scheduler (APScheduler) is a Python library that lets you schedule your Python code to be executed later, either just once or periodically. You can add new jobs or remove old ones on the fly as you please. If you store your jobs in a database, they will also survive scheduler restarts and maintain their state. When the scheduler is restarted, it will then run all the jobs it should have run while it was offline 1.

---

## APScheduler


Among other things, APScheduler can be used as a cross-platform, application specific replacement to platform specific schedulers, such as the cron daemon or the Windows task scheduler. Please note, however, that APScheduler is not a daemon or service itself, nor does it come with any command line tools. It is primarily meant to be run inside existing applications. That said, APScheduler does provide some building blocks for you to build a scheduler service or to run a dedicated scheduler process.


---


#### tl;dr schedule your python code to run later.

---


## some use cases

daily payments tasks

recurring report generation

automated backups

---


![ct](crontab.png)


---

## setup

shell
```sh
mkdir apdemo && cd apdemo
python3 -m venv venv
source venv/bin/activate
echo apscheduler >> requirements.txt
echo Flask >> requiremnets.txt
pip install -r requirements.txt
vim simple.py
```


---

## Basic Blocking Scheduler

```python
# simple.py

from apscheduler.schedulers.blocking 
     import BlockingScheduler

scheduler = BlockingScheduler(daemon=True)
scheduler.add_job(lambda: scheduler.print_jobs(), 
    'interval', seconds=2)
scheduler.start()
```
---


## APScheduler Components

---


![APScheduler Class Graph](https://enqueuezero.com/static/images/apscheduler-oo.png)

<em><small>source: https://enqueuezero.com/concrete-architecture/apscheduler.html</small></em>

---

# Job

Jobs contain a functoin, parameters for execution, and scheduling paramters.
The scheduling parameters are for controlling scheduler behaviors.

---

# Trigger

All jobs have their own triggers. Triggers determine when the next time a given job should run. 

---

# Scheduler

The scheduler is the master coordinator. It manages the execture and the job store. There are a number of subclasses for specific use.


---

### Scheduler

APScheduler has three built-in scheduling systems you can use:

Cron-style scheduling (with optional start/end times)

Interval-based execution (runs jobs on even intervals, with optional start/end times)

One-off delayed execution (runs jobs once, on a set date/time)

---

# JobStore
JobStore houses the scheduled jobs. Saved in memory by default. You can supply other persitence sources such as Mongo, Redis, etc...


---

# Executor
Executors run the jobs. They manage the life cycles of jobs. By default, you can use thread or process as executors.



---

see main.py