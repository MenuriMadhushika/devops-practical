from app import app


def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"CI/CD and Docker Pipeline is a massive success! V2" in response.data
