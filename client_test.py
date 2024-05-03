import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    expected_price = (120.48 + 121.2) / 2
        # Calculate the expected price directly based on input quotes
    actual_price = getDataPoint(quotes[0])[3]
    self.assertEqual(actual_price, expected_price)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    expected_price = (117.87 + 121.68) / 2
    # Calculate the expected price directly based on input quotes
    actual_price = getDataPoint(quotes[1])[3]
    self.assertEqual(actual_price, expected_price)
    
  """ ------------ Add more unit tests ------------ """
       
  def test_getRatio_positivePrices(self):
      # Test with positive price values
      ratio = getRatio(20, 10)
      self.assertEqual(ratio, 2)
      
  def test_getRatio_negativePrices(self):
      # Test with negative price values
      ratio = getRatio(-20, 10)
      self.assertEqual(ratio, -2)


if __name__ == '__main__':
    unittest.main()
