
from locust import HttpUser, task, between 


class Browsinguser(HttpUser):
    wait_time = between(1,5)  

    @task
    def woman_watch(self):
        self.client.get("/specialists")
