#MODULE:VOLUME

import DATA
import LED

import APNS

#ACTIONS

def update():
    print("VOLUME - UPDATE")

    distanceFull = DATA.load_distanceFull()
    distanceEmpty = DATA.load_distanceEmpty()
    distance = DATA.load_distance()

    range = distanceEmpty - distanceFull

    percentage = 0.0

    if distance < distanceEmpty:
        diffFromEmpty = distanceEmpty - distance
        percentage = diffFromEmpty / range
        print("VOLUME - UPDATE - PERCENTAGE = [%.2f]" % percentage)

    volumeMax = DATA.load_volumeMax()
    volume = volumeMax * percentage
    print("VOLUME - UPDATE - VOLUME = [%d]" % volume)

    DATA.save_volume(volume)
    DATA.save_percentage(percentage)

    warningPercentage = DATA.load_warningPercentage()

    LED.setup()
    if percentage < warningPercentage:
        LED.red()

        shouldSend = DATA.load_shouldSend()
        print("********************************************************** SHOULD SEND = ")
        print(shouldSend)

        if shouldSend:
            print("********************************************************** SEND NOTIF")
    
            # sending = DATA.load_sending()
            # print("********************************************************** SENDING = ")
            # print(sending)
            # if not sending:
                # DATA.save_sending(1)
            
            # APNS.sendNotification()
                
    else:
        if percentage > 0.5:
            print("********************************************************** SHOULD SEND SET TO 1")
            DATA.save_shouldSend(1)
        LED.blue()

    #UPDATE DAYS LEFT
