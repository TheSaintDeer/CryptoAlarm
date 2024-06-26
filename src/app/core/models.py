from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


class TelegramChat(models.Model):
    '''User's ID in telegram'''
    chat_id = models.IntegerField(
        unique=True,
        primary_key=True
    )

    def __str__(self):
        return f'{self.chat_id}'
    

class Pair(models.Model):
    '''Pair of cryptovalues'''
    name = models.CharField(
        max_length=10,
    )
    isUsed = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f'{self.name}'
    

class Alarm(models.Model):
    '''All alarms that users have subscribed to'''
    user = models.ForeignKey(
        'TelegramChat', 
        on_delete=models.CASCADE,
    )
    pair = models.ForeignKey(
        'Pair',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.user.chat_id} - {self.pair.name}'


@receiver(post_delete, sender=Alarm)
def pair_not_used(sender, instance, **kwargs):
    '''No one is currently subscribed to this couple's mailing list.'''
    pair = Pair.objects.get(name=instance.pair.name)
    if not pair.alarm_set.all():
        pair.isUsed = False
        pair.save()

@receiver(pre_save, sender=Alarm)
def pair_used(sender, instance, **kwargs):
    '''Now someone is subscribed to this couple's mailing list'''
    pair = Pair.objects.get(name=instance.pair.name)
    if not pair.isUsed:
        pair.isUsed = True
        pair.save()