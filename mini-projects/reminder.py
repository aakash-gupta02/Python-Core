import time
from plyer import notification

while True:
    print("Hey get some snacks")
    notification.notify(title="Eat some snacks",
                        message="U are hunry.....don't you?")
    time.sleep(6)

