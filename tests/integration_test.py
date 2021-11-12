import pytest
from src.connection_factory import Session


class IntegrationTest:
    @pytest.fixture(scope="function", autouse=True)
    def session(self):
        Session.remove()

        yield Session()

        Session().rollback()