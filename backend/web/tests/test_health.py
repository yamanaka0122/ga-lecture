import pytest


@pytest.mark.django_db
def test_health(client):
    res = client.get("/healthz")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}
