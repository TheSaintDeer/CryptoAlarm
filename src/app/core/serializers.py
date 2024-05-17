from rest_framework import serializers

from . import models


class TelegramChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TelegramChat
        fields = ['pk', 'chat_id', 'timezone']


class PairSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pair
        fields = ['pk', 'name', 'isUsed']


class AlarmSerializer(serializers.ModelSerializer):

    user = TelegramChatSerializer()
    pair = PairSerializer()

    class Meta:
        model = models.Alarm
        fields = ['user', 'pair', 'time']

    # def create(self, validated_data):
    #     validated_data['user'] = models.TelegramUser.objects.get(
    #         chat+_id=validated_data['user']['telegram_id']
    #     )
    #     validated_data['pair'], isCreated = models.Pair.objects.get_or_create(
    #         name=validated_data['pair']['name']
    #     )

    #     return super().create(validated_data)