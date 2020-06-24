from django.core.management.base import BaseCommand, CommandError
from backend.models import Users, ActivityPeriod, Backend
from django.utils.crypto import get_random_string
from django.utils import timezone

import random
import datetime
import pytz
import string
TIMEZONES=list(pytz.all_timezones )

class Command(BaseCommand):
    help = 'Populate user'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')


    def random_string_generator(size=30, chars=string.ascii_lowercase ):
    	return ''.join(random.choice(chars) for _ in range(size))


    def handle(self, *args, **kwargs):
    	bools=[True, False]
    	total = kwargs['total']
    	for i in range(total):
        	backend=Backend.objects.create(ok=random.choice(bools))
        	users=Users.objects.create(id=get_random_string(), real_name=get_random_string(allowed_chars='qwertyuiopasdfgjjklzxcvbnm'), tz=random.choice(TIMEZONES), backend=backend)
        	for i in range(random.randint(0,10)):
        		present = timezone.now() + datetime.timedelta(seconds=random.randint(0, 86400))
        		future=  timezone.now() + datetime.timedelta(seconds=random.randint(0, 86400))+ datetime.timedelta(seconds=random.randint(0, 86400))
        		ActivityPeriod.objects.create(start_time=present, end_time=future, members=users)
