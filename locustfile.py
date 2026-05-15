
from locust import HttpUser, task, between 
import BeatifulSoup

class Browsinguser(HttpUser):
    weight = 3
    wait_time = between(1,5)  

    @task
    def woman_watch(self):
        self.client.get("/specialists")
