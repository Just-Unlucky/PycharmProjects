import webbrowser
import time
import random



while True:
    sites = random.choice(["www.youtube.com/watch?v=dQw4w9WgXcQ"])
    visit = "https://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5, 100)
    time.sleep(seconds)