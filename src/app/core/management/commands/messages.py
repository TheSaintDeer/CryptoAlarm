new_user_start_answer = '''
Hello, I'm Crypto Alarm bot. With my help, you can monitor the price changes of your favorite pairs at a time convenient for you.\n
To start the time, you need to set your time. Write your time zone in the format 'GMTYX', where Y is + or -, and X is a number.'''

old_user_start_answer = '''
Hello, I'm Crypto Alarm bot. With my help, you can monitor the price changes of your favorite pairs at a time convenient for you.\n
To create a new alarm clock, write the command /new_alarm.\n
To find out all my capabilities, write the /help command.'''

set_time_zone_success = '''
Success! To create a new alarm clock, write the command /new_alarm.\n
To find out all my capabilities, write the /help command.'''

set_time_zone_error = '''
Something wrong! Try again.\n
The time must be in 'GMTYX' format, where Y is + or -, and X is a number.\n
Example: GMT+1 or GMT-12'''

change_timezone = '''
You want to change your time zone. Enter a new one in 'GMTYX' format, where Y is + or -, and X is a number.'''

help_answer = '''
SETTINGS
/my_id
/change_timezone

ALARM
/new_alarm
/my_alarms
/update_alarm
/delete_alarm
/delete_all_alarms'''

def list_alarms(alarms: list) -> str:
    text = ''
    alarm_id = 1

    for alarm in alarms:
        text += f'{alarm_id}. {alarm.pair.name} {alarm.time}\n'
        alarm_id += 1

    return text