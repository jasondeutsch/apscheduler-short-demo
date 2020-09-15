from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler(daemon=True)
scheduler.add_job(lambda: scheduler.print_jobs(), 'interval', seconds=2)
scheduler.start()
