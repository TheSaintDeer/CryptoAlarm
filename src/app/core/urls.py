from django.urls import path, include
from rest_framework import routers

from . import views


app_name = 'core'

router = routers.DefaultRouter()
router.register(r'telegram-chat', views.TelegramChatViewSet)
router.register(r'pair', views.PairViewSet)
router.register(r'alarm', views.AlarmViewSet)

urlpatterns = [
    path('', include(router.urls)),
]