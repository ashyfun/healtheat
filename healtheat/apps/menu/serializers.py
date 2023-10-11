from rest_framework import serializers

from healtheat.apps.menu.models import DailyMenuModel


class DailyMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = DailyMenuModel
        fields = '__all__'
