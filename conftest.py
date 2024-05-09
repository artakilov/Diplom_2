import pytest
from helpers import User


@pytest.fixture(scope='function')
def payload_user():
    user = User()
    payload_user = user.create_new_user()
    yield payload_user
    user.delete_user(payload_user["response"].json()["accessToken"])
