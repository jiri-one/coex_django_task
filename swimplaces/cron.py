from django_cron import CronJobBase, Schedule
from .management.commands.temperature_update import Command

class TemperatureCronJob(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'swimplaces.temperature_cron_job'    # a unique code

    def do(self):
        temperature_update = Command()
        temperature_update.handle()
