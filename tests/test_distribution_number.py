import os.path
import sys
import mock
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from unittest import TestCase
from unittest import main
from src.business.distribution_number import DistributionNumber


class TestDistributionNumber(TestCase):

    def test_should_distribute_one_promo_number(self):
        expected = [
            {'serie': '0', 'number': '00001'}
        ]
        result = DistributionNumber().distribute(1)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
