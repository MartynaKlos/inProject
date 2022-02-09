import pytest

from ..models import Worker

@pytest.mark.django_db
def test_workers_list_view(workers, client):
    url = '/'
    response = client.get(url)
    workers = list(response.context['workers'].values_list('pk', flat=True))
    workers_db = list(Worker.objects.all().values_list('pk', flat=True))
    assert response.status_code == 200
    assert workers == workers_db


@pytest.mark.django_db
def test_worker_detail_view(workers, client):
    worker = Worker.objects.all().first()
    url = f'/worker/{worker.pk}/'
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['worker'].name == worker.name
    assert response.context['worker'].occupation == worker.occupation


@pytest.mark.django_db
def test_add_worker_view(client):
    url = '/add-worker/'
    data = {
        'name': 'Martyna',
        'surname': 'Klos',
        'age': 54,
        'occupation': 3,
        'photo': 'photos/s-l300.jpg'
    }
    response = client.post(url, data)
    breakpoint()
    assert response.status_code == 302
    assert Worker.objects.all().count() == 1