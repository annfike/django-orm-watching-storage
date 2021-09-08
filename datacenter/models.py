from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= 'leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )

def get_duration(visit):
      time1 = timezone.localtime(visit.leaved_at)    
      time0 = timezone.localtime(visit.entered_at)
      delta = time1 - time0
      return delta

def format_duration(duration):
      seconds = duration.total_seconds()
      hours = int(seconds // 3600)
      minutes = int((seconds % 3600) // 60)
      return (f"{hours}ч.{minutes}м.")

def is_visit_long(visit, minutes=60):
      duration = get_duration(visit)
      seconds = duration.total_seconds()
      sec = minutes * 60
      result = seconds > sec
      return result
      