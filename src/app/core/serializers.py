from rest_framework import serializers

from . import models


class TelegramUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TelegramUser
        fields = ['pk', 'telegram_id']


class PairSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pair
        fields = ['pk', 'name', 'isUsed']


class AlarmSerializer(serializers.ModelSerializer):

    user = TelegramUserSerializer()
    pair = PairSerializer()

    class Meta:
        model = models.Alarm
        fields = ['user', 'pair', 'price']

    def create(self, validated_data):
        validated_data['user'] = models.TelegramUser.objects.get(
            telegram_id=validated_data['user']['telegram_id']
        )
        validated_data['pair'], isCreated = models.Pair.objects.get_or_create(
            name=validated_data['pair']['name']
        )

        return super().create(validated_data)