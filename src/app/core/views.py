from rest_framework import viewsets
from rest_framework.response import Response

from . import models, serializers, services


class TelegramChatViewSet(viewsets.ModelViewSet):

    queryset = models.TelegramChat.objects.all()
    serializer_class = serializers.TelegramChatSerializer

class PairViewSet(viewsets.ModelViewSet):

    queryset = models.Pair.objects.all()
    serializer_class = serializers.PairSerializer


class AlarmViewSet(viewsets.ModelViewSet):

    queryset = models.Alarm.objects.all()
    serializer_class = serializers.AlarmSerializer

    def create(self, request, *args, **kwargs):

        data = request.data
        if (services.get_price(data['pair.name'])):
            serializer = serializers.AlarmSerializer(data=data)
            if serializer.is_valid():
                serializer.save()    

        return Response(serializer.data)