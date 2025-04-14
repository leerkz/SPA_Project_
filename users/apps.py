from django.apps import AppConfig
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.DAYS,
        )

        PeriodicTask.objects.get_or_create(
            interval=schedule,
            name='Deactivate inactive users',
            task='users.tasks.deactivate_inactive_users',
            defaults={'kwargs': json.dumps({})}
        )