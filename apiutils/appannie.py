import requests
import json
from requests import ConnectionError


class AppAnnie:
    def __init__(self, apikey):
        self.header = {"authorization": "bearer {}".format(apikey)}

    def _api_call(self, URL):
        try:
            response = requests.get(URL, headers=self.header)
        except ConnectionError as CE:
            print("******** Unexpected error:", CE)
            raise

        print("Response status: {}".format(response.status_code))

        if not response.ok:
            raise ValueError(
                'Response to API call is not OK. HTTP Response received from server : {} '.format(response.status_code))

        return json.loads(response.text)

    def downloads_by_product(self, accountid, productid, dt):
        return self._api_call("https://api.appannie.com/v1.2/accounts/{aid}/products/{pid}/sales"
                              "?break_down=date%20country%20%20iap"
                              "&start_date={dt}&end_date={dt}"
                              .format(aid=accountid, pid=productid, dt=dt))

    def accounts(self):
        return self._api_call("https://api.appannie.com/v1.2/accounts")

    def products(self, accountid):
        return self._api_call("https://api.appannie.com/v1.2/accounts/{}/products".format(accountid))

    def all_downloads(self, date):
        accounts_json = self.accounts()
        return accounts_json
