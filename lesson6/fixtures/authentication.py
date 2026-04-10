import pytest
from lesson6.clients.authentication.authentication_client import AuthenticationClient, get_authentication_client


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_authentication_client()