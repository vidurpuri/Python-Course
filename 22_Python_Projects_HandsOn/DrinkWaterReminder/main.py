import time
from plyer import notification

while True:
    print("Time to drink water!")
    notification.notify(
        title="Drink Water Reminder",
        message="It's important to stay hydrated! Please drink a glass of water now.",
        timeout=10
    )
    time.sleep(3600)  # Remind every hour