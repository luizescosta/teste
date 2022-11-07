from locust import HttpUser
from rota_usuario import UserRouteLoadTest


class WebsiteUser(HttpUser):
    tasks = [
        UserRouteLoadTest
    ]
