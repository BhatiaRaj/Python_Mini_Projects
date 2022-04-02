import time
from plyer import notification

if __name__=='__main__':
    while True:
        notification.notify(
            title="** Please Drink Water Now !!",
            message="Drinking Water Helps to Maintain the Balance of Body Fluids.",
            #app_icon="R:\PythonProject\DrinkWaterNotificationReminder\Glass.ico",
            timeout=5
        )
        time.sleep(5)
        #time.sleep(60*60)