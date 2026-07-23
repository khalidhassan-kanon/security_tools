import unittest

from ip_utils import (
    network_address,
    broadcast_address,
    first_host,
    last_host,
    total_hosts,
    wildcard_mask
)


class TestSubnetCalculator(unittest.TestCase):

    def test_network_address(self):
        self.assertEqual(
            network_address("192.168.1.10", 24),
            "192.168.1.0"
        )

    def test_broadcast_address(self):
        self.assertEqual(
            broadcast_address("192.168.1.10", 24),
            "192.168.1.255"
        )

    def test_first_host(self):
        self.assertEqual(
            first_host("192.168.1.10", 24),
            "192.168.1.1"
        )

    def test_last_host(self):
        self.assertEqual(
            last_host("192.168.1.10", 24),
            "192.168.1.254"
        )

    def test_total_hosts(self):
        self.assertEqual(
            total_hosts(24),
            254
        )

    def test_wildcard_mask(self):
        self.assertEqual(
            wildcard_mask(24),
            "0.0.0.255"
        )


if __name__ == "__main__":
    unittest.main()