import unittest 
from unittest import TestCase
from unittest.mock import patch 

import bitcoin 

class TestBitCoin(TestCase):

    @patch('bitcoin.get_bitcoin_data')
    def test_convert_bitcoin_to_dollars(self, mock_api_call):

        mock_api_call.return_value = {'time': {'updated': 'Nov 1, 2022 01:54:00 UTC', 'updatedISO': '2022-11-01T01:54:00+00:00', 'updateduk': 'Nov 1, 2022 at 01:54 GMT'}, 'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org', 'chartName': 'Bitcoin', 'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': '20,492.9679', 'description': 'United States Dollar', 'rate_float': 20492.9679}, 'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '17,123.7600', 'description': 'British Pound Sterling', 'rate_float': 17123.76}, 'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '19,963.1427', 'description': 'Euro', 'rate_float': 19963.1427}}}{'time': {'updated': 'Nov 1, 2022 01:54:00 UTC', 'updatedISO': '2022-11-01T01:54:00+00:00', 'updateduk': 'Nov 1, 2022 at 01:54 GMT'}, 'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org', 'chartName': 'Bitcoin', 'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': '20,492.9679', 'description': 'United States Dollar', 'rate_float': 20492.9679}, 'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '17,123.7600', 'description': 'British Pound Sterling', 'rate_float': 17123.76}, 'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '19,963.1427', 'description': 'Euro', 'rate_float': 19963.1427}}}
        expected_dollars = 2049296.79
        dollars = bitcoin.convert_bitcoin_to_dollars(100)
        self.assertEqual(expected_dollars, dollars)


if __name__ == '__main__':
    unittest.main()