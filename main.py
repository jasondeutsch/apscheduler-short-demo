from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request
import json
from random import randint

app = Flask(__name__)
if __name__ == "__main__":
    app.run("0.0.0.0", port=6666)


queue = []


scheduler = BackgroundScheduler(daemon=True)

@app.route("/")
@app.route("/start-jobs", methods=["POST"])
def start_jobs():
    if scheduler.running:
        return json.dumps({"error": "jobs already running"})
    scheduler.start()
    return json.dumps({"status": scheduler.state})


@app.route("/jobs", methods=["GET"])
def get_jobs():
    jobs = []
    for job in scheduler.get_jobs():
        print(job)
        jobs.append(
            {
                "id": job.id,
                "name": job.name,
                #"nextRun": job.next_run_time.astype(str),
            }
        )
    return json.dumps(jobs)


@app.route("/jobs/<job_id>", methods=["GET"])
def get_job_instance(job_id):
    job = scheduler.get_job(job_id=job_id)
    return json.dumps(job)


@app.route("/add-job", methods=["POST"])
def add_job():
    job = scheduler.add_job(lambda: queue.append(randint(0, 100)), 'interval', seconds=5)
    return json.dumps(job)


@app.route("/state", methods=["POST"])
def change_state():
    state = request.json["state"]
    if state == "pause":
        scheduler.pause()
    elif state == "shutdown":
        scheduler.shutdown()
    elif state == "start":
        scheduler.start()
    else:
        return "no", 400

    return json.dumps(scheduler.state())



