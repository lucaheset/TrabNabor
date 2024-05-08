from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def index_page(self):
        self.client.get("/?p=1")

    @task(3)
    def view_posts(self):
        for post_id in range(10):
            self.client.get(f"/?p={post_id}", name="/?p=[id]")
            self.wait()

    @task(2)
    def specific_post(self):
        self.client.get("/2024/05/06/teste/")
