import unittest

from api import app


class TestApi(unittest.TestCase):
  def setUp(self):
    self.client = app.test_client()

  def test_convert1(self):
    response = self.client.get('http://localhost:5000/api/convert?source=USD&target=JPY&amount=$1,525')
    self.assertEqual(response.json, {'msg': 'success', 'amount': '$170,496.52'})

  def test_convert2(self):
    response = self.client.get('http://localhost:5000/api/convert?source=TWD&target=USD&amount=325.15')
    self.assertEqual(response.json, {'msg': 'success', 'amount': '10.67'})

  def test_convert3(self):
    response = self.client.get('http://localhost:5000/api/convert?source=JPY&target=JPY&amount=1,525')
    self.assertEqual(response.json, {'msg': 'success', 'amount': '1,525.00'})

  def test_convert4(self):
    response = self.client.get('http://localhost:5000/api/convert?source=ABC&target=JPY&amount=$1,525')
    self.assertEqual(response.json, { 'msg': '不支援的source幣別' })

  def test_convert5(self):
    response = self.client.get('http://localhost:5000/api/convert?source=USD&target=ABC&amount=$1,525')
    self.assertEqual(response.json, { 'msg': '不支援的target幣別' })

  def test_convert6(self):
    response = self.client.get('http://localhost:5000/api/convert?source=USD&target=JPY&amount=$1,5*25')
    self.assertEqual(response.json, { 'msg': 'amount格式須為(幣別符號)+金額' })

if __name__ == '__main__':
  unittest.main(verbosity=2)