# test_service_stations.py
import unittest
from service_stations import min_stations

class TestServiceStations(unittest.TestCase):
    def test_linear_graph(self):
        self.assertEqual(min_stations(3, [(1,2), (2,3)]), 2)

    def test_no_connections(self):
        self.assertEqual(min_stations(5, []), 5)

    def test_star_graph(self):
        self.assertEqual(min_stations(4, [(1,2), (1,3), (1,4)]), 1)

    def test_two_components(self):
        self.assertEqual(min_stations(4, [(1,2), (3,4)]), 2)

    def test_single_connection(self):
        self.assertEqual(min_stations(2, [(1,2)]), 1)

if __name__ == "__main__":
    unittest.main()