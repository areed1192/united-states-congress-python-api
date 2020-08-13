import unittest

from unittest import TestCase
from configparser import ConfigParser
from congress.client import Congress


class CongressSession(TestCase):

    """Will perform a unit test for the `CongressClient` session."""

    def setUp(self) -> None:
        """Set up the Client."""

        # Initialize the Client
        self.congress_client = Congress()

    def test_creates_instance_of_session(self):
        """Create an instance and make sure it's a `CongressClient`."""

        # Make Sure it's a `Congress` instance.
        self.assertIsInstance(self.congress_client, Congress)

    def tearDown(self) -> None:
        """Teardown the `CongressClient`."""

        del self.congress_client


if __name__ == '__main__':
    unittest.main()
