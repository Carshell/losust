#https://street-beat.ru/

from locust import HttpUser, task, between 

class Browsinguser(HttpUser):
    weight = 3
    wait_time = between(1,5)  

    @task(2)
    def woman_watch(self):
        self.client.get("/woman")
        self.client.get("/cat/woman/adidas-originals/japan/")
        self.client.get("/d/krossovki-adidas-originals-ih1631/")

    @task(4)
    def man_watch(self):
        self.client.get("/man")
        self.client.get("/cat/man/vans/knu-skool/")
        self.client.get("/d/kedy-vans-vn0009qc6bt1/")

    @task(7)
    def kids_watch(self):
        self.client.get("/kids")
        self.client.get("/cat/kids/vans/hylane")
        self.client.get("/d/kedy-vans-vn000d4nbzw1/")


class DbUser(HttpUser):
    weight = 2
    wait_time = between(1,5)

    @task
    def hello_world(self):
        self.client.get("/order/reg/")
        self.client.get("/woman")