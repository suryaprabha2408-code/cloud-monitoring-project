import random
import time

THRESHOLD = 80

while True:
    usage = random.randint(50, 120)
    print(f"Current Usage: {usage}")

    if usage > THRESHOLD:
        print(f"ALERT! High usage detected: {usage}")

    time.sleep(10)