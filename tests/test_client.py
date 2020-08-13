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

    def test_bills_endpoint(self):
        """Test the Congressional Bills Resource Endpoint."""

        # Make the request.
        content = self.congress_client.congressional_bills(folder='116')

        # Make sure we have files.
        self.assertIn('files', content)

    def test_bills_status_endpoint(self):
        """Test the Bills Status Resource Endpoint."""

        # Make the request.
        content = self.congress_client.bill_status(folder='116')

        # Make sure we have files.
        self.assertIn('files', content)

    def test_bills_summary_endpoint(self):
        """Test the Bills Summaries Resource Endpoint."""

        # Make the request.
        content = self.congress_client.bill_summaries(folder='116')

        # Make sure we have files.
        self.assertIn('files', content)

    def test_commerce_buisness_daily_endpoint(self):
        """Test the Commerce Business Daily Resource Endpoint."""

        # Make the request.
        content = self.congress_client.commerce_business_daily(folder='2001')

        # Make sure we have files.
        self.assertIn('files', content)

    def test_code_of_federal_regulations_endpoint(self):
        """Test the Code of Federal Regulations Resource Endpoint."""

        # Make the request.
        content = self.congress_client.code_of_federal_regulations(
            folder='1996'
        )

        # Make sure we have files.
        self.assertIn('files', content)

    def test_electronic_code_of_federal_regulations_endpoint(self):
        """Test the Electronic Code of Federal Regulations Resource Endpoint."""

        # Make the request.
        content = self.congress_client.electronic_code_of_federal_regulation(
            folder='title-50'
        )

        # Make sure we have files.
        self.assertIn('files', content)

    def test_federal_register_endpoint(self):
        """Test the Federal Register Resource Endpoint."""

        # Make the request.
        content = self.congress_client.federal_register(folder='2020')

        # Make sure we have files.
        self.assertIn('files', content)

    def test_us_government_manuals_endpoint(self):
        """Test the US Government Manuals Resource Endpoint."""

        # Make the request.
        content = self.congress_client.us_government_manuals(folder='2019')

        # Make sure we have files.
        self.assertIn('files', content)

    def test_house_rules_and_manual_endpoint(self):
        """Test the House Rules and Manual Resource Endpoint."""

        # Make the request.
        content = self.congress_client.house_rules_and_manual(folder='116')

        # Make sure we have files.
        self.assertIn('files', content)

    def test_privacy_act_issuances_endpoint(self):
        """Test the Privacy Act Issuances Resource Endpoint."""

        # Make the request.
        content = self.congress_client.privacy_act_issuances(folder='2019')

        # Make sure we have files.
        self.assertIn('files', content)

    def test_private_and_public_laws_endpoint(self):
        """Test the Private and Public Laws Resource Endpoint."""

        # Make the request.
        content = self.congress_client.private_and_public_laws(folder='116')

        # Make sure we have files.
        self.assertIn('files', content)

    def test_presidential_papers_endpoint(self):
        """Test the Presidential Papers Resource Endpoint."""

        # Make the request.
        content = self.congress_client.public_papers_president(folder='2014')

        # Make sure we have files.
        self.assertIn('files', content)

    def test_supreme_court_decision_endpoint(self):
        """Test the Supreme Court Decisions Resource Endpoint."""

        # Make the request.
        content = self.congress_client.supreme_court_decisions(folder='1937')

        # Make sure we have files.
        self.assertIn('files', content)

    def test_statues_endpoint(self):
        """Test the Statutes at Large Resource Endpoint."""

        # Make the request.
        content = self.congress_client.statutes_at_large(folder='127')

        # Make sure we have files.
        self.assertIn('files', content)

    def tearDown(self) -> None:
        """Teardown the `CongressClient`."""

        del self.congress_client


if __name__ == '__main__':
    unittest.main()
