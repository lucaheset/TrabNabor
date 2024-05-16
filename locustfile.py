from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def index_page(self):
        self.client.get("/?p=1")

    @task(2)
    def specific_post(self):
        # self.client.get("/2024/05/10/teste/")  # 2mb images
        self.client.get("/2024/05/06/teste/")  # 2mb images
        # self.client.get("/2024/05/11/teste2/")  # 400kb texto
        self.client.get("/2024/05/15/teste2/")  # 400kb texto
        # self.client.get("/2024/05/11/teste3/")  # 300kb image
        self.client.get("/2024/05/15/teste3/")  # 300kb image
