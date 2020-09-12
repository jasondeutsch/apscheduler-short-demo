from apscheduler.schedulers.background import BlockingScheduler

scheduler = BlockingScheduler(daemon=True)
scheduler.add_job(lambda: scheduler.print_jobs(), 'interval', seconds=5)
scheduler.start()

