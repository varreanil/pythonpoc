import unittest
import json
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

        afile = open("accounts.json")
        pfile = open("products.json")
        dfile = open("downloads.json")

        self.accounts_json_resp = afile.read()
        self.products_json_resp = pfile.read()
        self.download_json_resp = dfile.read()

        afile.closed
        pfile.closed
        dfile.closed


    @patch('apiutils.appannie.requests.get')
    def test_appannie_all_downloads(self, mocked_get):
        mocked_get.return_value.ok = True
        mocked_get.return_value.status_code = "200"
        mocked_get.return_value.json.return_value = json.dumps(self.accounts_json_resp)

        result = appannie.AppAnnie(self.apikey).all_downloads("2016-05-1")
        mocked_get.assert_called_with(self.account_url, headers=self.header)

        print("Res json: {}".format(result))
        # self.assertEquals(result["code"], 200)


'''
    @patch('apiutils.appannie.requests.get')
    def test_appannie_downloads(self, mocked_get):
        mocked_get.response.ok = True
        mocked_get.response.status_code = "200"
        mocked_get.response.json = self.download_json_resp

        res = appannie.AppAnnie(self.apikey).downloads_by_product("415343", "784797900", "2016-05-1")
        mocked_get.assert_called_with(self.download_url, headers=self.header)
        self.assertTrue(res.ok)
        # self.assertTrue(not res)

    @patch('apiutils.appannie.requests.get')
    def test_appannie_accounts(self, mocked_get):
        mocked_get.response.ok = True
        mocked_get.response.status_code = "200"
        mocked_get.response.json = self.accounts_json_resp

        res = appannie.AppAnnie(self.apikey).accounts()
        mocked_get.assert_called_with(self.account_url, headers=self.header)
        self.assertTrue(res.ok)

    @patch('apiutils.appannie.requests.get')
    def test_appannie_products(self, mocked_get):
        mocked_get.response.ok = True
        mocked_get.response.status_code = "200"
        mocked_get.response.json = self.products_json_resp

        res = appannie.AppAnnie(self.apikey).products("415343")
        mocked_get.assert_called_with(self.product_url, headers=self.header)
        self.assertTrue(res.ok)
'''
