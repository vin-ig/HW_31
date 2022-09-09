from pytest_factoryboy import register

from tests.factories import AdFactory, UserFactory

pytest_plugins = 'tests.fixtures'

register(AdFactory)
register(UserFactory)

# HTTP_AUTHORIZATION='Bearer ' + user_token
