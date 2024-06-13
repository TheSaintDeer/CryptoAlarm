user_start_answer = '''
Hello, I'm Crypto Alarm bot. With my help, you can monitor the price changes of your favorite pairs at a time convenient for you.\n
To create a new alarm clock, write the command /new_alarm.\n
To find out all my capabilities, write the /help command.'''

help_answer = '''
INFO
/my_id

ALARM
/new_alarm
/my_alarms
/delete_alarm
/delete_all_alarms'''

def list_alarms(alarms: list) -> str:
    text = ''
    alarm_id = 1

    for alarm in alarms:
        text += f'{alarm_id}. {alarm.pair.name} {alarm.time}\n'
        alarm_id += 1

    return text