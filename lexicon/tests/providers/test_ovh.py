"""Integration tests for OVH"""
from unittest import TestCase

from lexicon.tests.providers.integration_tests import IntegrationTests
from lexicon.providers.ovh import Provider


# Hook into testing framework by inheriting unittest.TestCase and reuse
# the tests which *each and every* implementation of the interface must
# pass, by inheritance from integration_tests.IntegrationTests
class OvhProviderTests(TestCase, IntegrationTests):
    """TestCase for OVH"""
    Provider = Provider
    provider_name = 'ovh'
    domain = 'pacalis.net'

    def _filter_headers(self):
        return ['X-Ovh-Application', 'X-Ovh-Consumer', 'X-Ovh-Signature']

    def _test_parameters_overrides(self):
        return {'auth_entrypoint': 'ovh-eu'}
