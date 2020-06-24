from django.db import models

# Create your models here.
class Backend(models.Model):
	ok=models.BooleanField(default=True)
		
class Users(models.Model):
	import pytz
	TIMEZONES=tuple(zip(pytz.all_timezones, pytz.all_timezones, ))
	backend=models.OneToOneField(Backend, on_delete=models.CASCADE, null=True, related_name='members')
	id=models.CharField(max_length=15, unique=True, primary_key=True)
	real_name=models.CharField(max_length=30)
	tz=models.CharField(max_length=40, choices =TIMEZONES)

	def __str__(self):
		return self.id

class ActivityPeriod(models.Model):
	members=models.ForeignKey(Users, on_delete=models.CASCADE, related_name='activity_periods')
	start_time=models.DateTimeField()
	end_time=models.DateTimeField()

	class Meta:
		unique_together = ['start_time', 'end_time']
		ordering = ['start_time']

