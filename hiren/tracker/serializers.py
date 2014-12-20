from django.contrib.auth.models import User
from rest_framework import serializers
from tracker.models import Hiren


class Tracker(serializers.ModelSerializer):

    class Meta:
        model = Hiren
        fields = ('id', 'tag')