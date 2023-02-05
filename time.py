print('please enter the time in a 24 hour format: ')
hour_24 = int(input('Hour: '))
minute_24 = int(input('Minutes: '))
minute_12 = minute_24

if(0 <= hour_24 < 12):
    period = 'am'
    if(hour_24 == 0):
        hour_12 = 12
    else:
        hour_12 = hour_24

else:
    period = 'pm'
    if(hour_24 == 12):
        hour_12 = 12
    else:
        hour_12 = hour_24 - 12

print(hour_24, ':', minute_24, ' = ', hour_12, ':', minute_12, period, sep='')