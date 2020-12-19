import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # The following are the test cases for this
    self.assertEqual(getDataPoint(quotes[0]),('ABC',120.48,121.2,120.84))
    # #quotes[0] is actually the quote that we need
    self.assertEqual(getDataPoint(quotes[1]),('DEF',117.87,121.68,119.775))
    self.assertEqual(getRatio(1,1),1)
    # self.assertEqual(getRatio(100/20),5)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # The following are the test cases 
    data_point_1 = getDataPoint(quotes[0])
    self.assertGreater(data_point_1[1],data_point_1[2])

    data_point_2 = getDataPoint(quotes[1])
    self.assertGreater(data_point_1[1],data_point_1[2])









if __name__ == '__main__':
    unittest.main()
