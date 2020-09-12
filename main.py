from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request
import json
from random import randint

app = Flask(__name__)
if __name__ == "__main__":
    app.run("0.0.0.0", port=6666)


queue = []


scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(lambda: queue.append(randint(0,100)), 'interval', seconds=5)


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


@app.route("/jobs/{job_id}/instances", methods=["GET"])
def get_job_instance(job_id):
    return "to do"


@app.route("/add-job", methods=["POST"])
def add_to_queue():
    print(request.get_json())
    return "noodles"


