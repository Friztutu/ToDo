from django.db import models
from users.models import CustomUser
import datetime
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    is_die = models.BooleanField(default=False)

    def check_time(self):
        if not self.is_done and not self.deadline > timezone.now():
            self.is_die = True
            self.save()

    def get_now(self):
        self.check_time()
        return timezone.now()
