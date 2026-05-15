
from locust import HttpUser, task, between 


class Browsinguser(HttpUser):
    weight = 3
    wait_time = between(1,5)  

    @task
    def woman_watch(self):
        self.client.post("/v1/ft", json={
    "mode": "pagination",
    "paginationParams": {
        "page": 1,
        "size": 36
    }
})
