from rest_framework import serializers

from . import models


class TelegramChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TelegramChat
        fields = ['chat_id']


class PairSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pair
        fields = ['pk', 'name', 'isUsed']


class AlarmSerializer(serializers.ModelSerializer):

    pair = PairSerializer()

    class Meta:
        model = models.Alarm
        fields = ['user', 'pair']

    def create(self, validated_data):
        chat = validated_data['user']
        pair, isCreated = models.Pair.objects.get_or_create(
            name=validated_data['pair']['name']
        )

        return models.Alarm.objects.create(
            user=chat,
            pair=pair
        )