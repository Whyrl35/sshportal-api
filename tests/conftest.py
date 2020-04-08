import pytest
import datetime
from sshportal_api import app as ctx_app
from sshportal_api.resources.users import UserModel


@pytest.fixture
def app():
    return ctx_app


@pytest.fixture
def create_test_user():
    created_users = []

    def _create_test_user(name, password):
        user = UserModel()
        user.name = name
        user.password = UserModel.generate_hash(password)
        user.invite_token = "1234567890"
        user.is_admin = False
        user.email = "test@local"
        user.comment = "pytest user created"
        user.created_at = datetime.datetime.now()
        user.updated_at = datetime.datetime.now()
        user.save_to_db()
        created_users.append(user)
        return user

    yield _create_test_user

    for record in created_users:
        record.delete()
