from rest_framework import serializers
from ..models import Users, ActivityPeriod, Backend

class ActivitySerializer(serializers.ModelSerializer):
	

	class Meta:
		model = ActivityPeriod
		fields=['start_time', 'end_time',]

class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivitySerializer(read_only=True, many=True)
    

    class Meta:
        model = Users
        fields = ('id', 'real_name', 'tz', 'activity_periods')

class BackendSerializer(serializers.ModelSerializer):
	members=UserSerializer(read_only=True)
	class Meta:
		model=Backend
		fields=('ok', 'members')