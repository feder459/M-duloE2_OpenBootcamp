import time
CurrentHour=time.strftime('%H')
CurrentMinute=time.strftime('%M')

if int(CurrentHour) >= 19:
    print("Es hora de ir a casa")
else:
    print ("Quedan {} horas y {} minutos para irnos a casa".format(18- int(CurrentHour), 59-int(CurrentMinute)))
    
    