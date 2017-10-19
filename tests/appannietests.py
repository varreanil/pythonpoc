import unittest
import json
import os
from unittest.mock import patch
from apiutils import appannie


class TestAppAnnie(unittest.TestCase):
    def setUp(self):
        self.apikey = "306d7db159531f549f96cf178ad82bb737201d46"
        self.header = header = {"authorization": "bearer 306d7db159531f549f96cf178ad82bb737201d46"}
        self.download_url = "https://api.appannie.com/v1.2/accounts/415343/products/784797900/sales" \
                            "?break_down=date%20country%20%20iap" \
                            "&start_date=2016-05-1&end_date=2016-05-1"
        self.account_url = "https://api.appannie.com/v1.2/accounts"
        self.product_url = "https://api.appannie.com/v1.2/accounts/415343/products"

        dir = os.path.dirname(__file__)
        with open(os.path.join(dir, 'accounts.json')) as afile:
            self.accounts_json_resp = afile.read()

        with open(os.path.join(dir, 'products.json')) as pfile:
            self.products_json_resp = pfile.read()

        with open(os.path.join(dir, 'downloads.json')) as dfile:
            self.download_json_resp = dfile.read()


    # def test_int_appannie_all_downloads(self):
    #     result = appannie.AppAnnie(self.apikey).all_downloads("2017-09-1")
    #
    #     print("Res type: {}".format(type(result)))
    #     print("Res : {}".format(result))
    #     # self.assertEquals(result["code"], 200)

    @patch('apiutils.appannie.requests.get')
    def test_appannie_accounts(self, mocked_get):
        mocked_get.return_value.ok = True
        mocked_get.return_value.status_code = "200"
        mocked_get.return_value.text = self.accounts_json_resp

        res = appannie.AppAnnie(self.apikey).accounts()
        mocked_get.assert_called_with(self.account_url, headers=self.header)
        self.assertEqual(res, json.loads(self.accounts_json_resp))

    @patch('apiutils.appannie.requests.get')
    def test_appannie_products(self, mocked_get):
        mocked_get.return_value.ok = True
        mocked_get.return_value.status_code = "200"
        mocked_get.return_value.text = self.products_json_resp

        res = appannie.AppAnnie(self.apikey).products("415343")
        mocked_get.assert_called_with(self.product_url, headers=self.header)
        self.assertEqual(res, json.loads(self.products_json_resp))

    @patch('apiutils.appannie.requests.get')
    def test_appannie_downloads(self, mocked_get):
        mocked_get.return_value.ok = True
        mocked_get.return_value.status_code = "200"
        mocked_get.return_value.text = self.download_json_resp

        res = appannie.AppAnnie(self.apikey).downloads_by_product("415343", "784797900", "2016-05-1")
        mocked_get.assert_called_with(self.download_url, headers=self.header)
        self.assertEqual(res, json.loads(self.download_json_resp))

    @patch('apiutils.appannie.requests.get')
    def test_appannie_all_downloads(self, mocked_get):
        mocked_get.return_value.ok = True
        mocked_get.return_value.status_code = "200"
        mocked_get.return_value.text = self.accounts_json_resp

        res = appannie.AppAnnie(self.apikey).all_downloads("2016-05-1")
        mocked_get.assert_called_with(self.account_url, headers=self.header)
        self.assertEqual(res, json.loads(self.accounts_json_resp))


if __name__ == '__main__':
    unittest.main()