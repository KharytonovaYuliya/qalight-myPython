def secondsconversion(seconds):
    minutes = 0.00
    hours = 0.00
    days = 0.00
    secpdayconst = 86400
    secphourconst = 3600
    secpminconst = 60
    if seconds >= secpdayconst:
        days = seconds / secpdayconst
        seconds -= int(days) * secpdayconst
        print('The number of days is ' + str(int(days)))
    if seconds >= secphourconst:
        hours = seconds / secphourconst
        seconds -= int(hours) * secphourconst
        print('The number of hours is ' + str(int(hours)))
    if seconds >= secpminconst:
        minutes = seconds / secpminconst
        seconds -= int(minutes) * secpminconst
        print('The number of minutes is ' + str(int(minutes)))
    return print('Days:Hours:Min:Sec: ' + str(int(days)) + ":" + str(int(hours)) + ":" + str(int(minutes)) + ":" + str(int(seconds)))

inputseconds = int(input("Enter the number of seconds:".strip()))
secondsconversion(inputseconds)