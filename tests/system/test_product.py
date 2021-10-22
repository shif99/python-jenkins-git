from unittest import TestCase

from mypage2 import app
import json
class ProductTest(TestCase): #ProductTest is  a testcase
    def test_welcome(self):
        with app.test_client() as c:
            resp = c.get('/api/products')
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()) ,
                                 [{"price":75542.5,"productId":1,"productName":"Iphone13","rating":4.8},
                                {"price":149999.5,"productId":2,"productName":"SamsungFlip","rating":4.6},
                                {"price":69999.5,"productId":3,"productName":"Oneplus","rating":4.2}])
#compares with this array and json files and gives test failed if they dont match else pass

