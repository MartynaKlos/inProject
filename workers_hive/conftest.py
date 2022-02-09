import pytest
from faker import Faker
from random import randint

from workers_app.models import Worker

faker = Faker("pl_pL")

@pytest.fixture
def workers():
    for i in range(5):
        Worker.objects.create(
            name=faker.first_name(),
            surname=faker.word(),
            age=randint(20,65),
            occupation=randint(1,7),
            photo='photos/sbBTXnGmqLK9S0L43EzL.png'
        )