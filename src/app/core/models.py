from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


class TelegramUser(models.Model):

    telegram_id = models.CharField(
        max_length=10
    )

    def __str__(self):
        return f'{self.telegram_id}'
    

class Pair(models.Model):

    name = models.CharField(
        max_length=10,
    )
    isUsed = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f'{self.name} - {self.isUsed}'
    

class Alarm(models.Model):

    user = models.ForeignKey(
        'TelegramUser', 
        on_delete=models.CASCADE,
    )
    pair = models.ForeignKey(
        'Pair',
        on_delete=models.CASCADE,
    )
    price = models.IntegerField()

    def __str__(self):
        return f'{self.user.telegram_id}: {self.pair.name}-{self.price}'


@receiver(post_delete, sender=Alarm)
def pair_not_used(sender, instance, **kwargs):
    pair = Pair.objects.get(name=instance.pair.name)
    if not pair.alarm_set.all():
        pair.isUsed = False
        pair.save()

@receiver(pre_save, sender=Alarm)
def pair_used(sender, instance, **kwargs):
    pair = Pair.objects.get(name=instance.pair.name)
    if not pair.isUsed:
        pair.isUsed = True
        pair.save()