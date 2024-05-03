import pytest
import helpers as hlprs


@pytest.fixture(scope='function')
def payload_user():
    data = hlprs.create_new_user()
    payload_for_test = {
        "email": data[0],
        "password": data[1],
        "name": data[2]
    }
    yield payload_for_test, data[3], data[4], data[5]
    hlprs.delete_user(data[5]["accessToken"])
