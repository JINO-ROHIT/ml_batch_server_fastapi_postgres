from apscheduler.schedulers.background import BackgroundScheduler
from src.api.routers.routers import health, predict_batch

scheduler = BackgroundScheduler()

scheduler.add_job(predict_batch, 'interval', seconds = 5)
#scheduler.add_job(predict_batch, trigger = 'cron', hour = 17, minute = 32, second = 0)