import requests
import json
from html.parser import HTMLParser

h = HTMLParser()
# This is the base url of Walmart open API
API_BASE_URL='http://api.walmartlabs.com/v1/'

class WalmartException(Exception):
    """Base Class for Walmart Api Exceptions.
    """

class InvalidRequestException(WalmartException):
    """Exception thrown if an invalid request response is return by Walmart
    """

    def __init__(self, status_code, **kwargs):
        error_message = 'Error'
        if status_code == 400:
            error_message = 'Bad Request'
            if 'detail' in kwargs:
                error_message = error_message + ' - ' + kwargs['detail']
        elif status_code == 403:
            error_message = 'Forbidden'
        elif status_code == 404:
            error_message = 'Wrong endpoint'
        elif status_code == 414:
            error_message = 'Request URI too long'
        elif status_code == 500:
            error_message = 'Internal Server Error'
        elif status_code == 502:
            error_message = 'Bad Gateway'
        elif status_code == 503:
            error_message = 'Service Unavailable/ API maintenance'
        elif status_code == 504:
            error_message = 'Gateway Timeout'
        message = '[Request failed] Walmart server answered with the following error: {0:s}. Status code: {1:d}'.format(error_message, status_code)
        super(self.__class__, self).__init__(message)
    pass


# This is the class for creating product instance
class WalmartProduct:
    """Models a Walmart Product as an object
    """

    def __init__(self, payload):#, LSNID):
        #self.LSNID = LSNID
#         self.response_handler = ResponseHandler(payload)
        self.response_handler = payload["items"][0]
        # print(self.response_handler)

    @property
    def item_id(self):
        """Item id: A positive integer that uniquely identifies an item
        :return:
            Item id (string). Returns None if attribute is not found in the response.
        """
#         return self.response_handler._safe_get_attribute('itemId')
        return self.response_handler["itemId"]

    @property
    def name(self):
        """Item name
        :return:
            Standard name of the item (string). Returns None if attribute is not found in the response.
        """
#         return self.response_handler._safe_get_attribute_text('name')
#         return h.unescape(self.response_handler['name'])
        return self.response_handler["name"]

    @property
    def sale_price(self):
        """Sale price
        :return:
            Selling price for the item in USD (float). Returns None if attribute is not found in the response.
        """
#         return self.response_handler._safe_get_attribute_float('salePrice')
        return self.response_handler['salePrice']

    @property
    def upc(self):
        """Unique Product Code
        :return:
            Unique Product Code (string). Returns None if attribute is not found in the response.
        """
#         return self.response_handler._safe_get_attribute('upc')
        return self.response_handler['upc']

    @property
    def category_node(self):
        """Product Category node: Category id for the category of this item. This value can be passed to APIs to pull this item's category level information.
        :return:
            Product Category path (string). Returns None if attribute is not found in the response.
        """
#         return self.response_handler._safe_get_attribute('categoryNode')
        return self.response_handler['categoryNode']

    @property
    def available_online(self):
        """Available online: Whether the item is currently available for sale on Walmart.com
        :return:
            Available online. (boolean). Returns None if attribute is not found in the response.
        """
#         return self.response_handler._safe_get_attribute('availableOnline')
        return self.response_handler['availableOnline']

class Walcrawl:
    """Models the main Walmart API proxy class
    """

    def __init__(self, api_key, **kwargs):
        """Initialize a Walmart API Proxy
        :param api_key:
            A string representing the Walmart Open API key. Can be found in 'My Account' when signing in your Walmartlabs account.
        - Named params passed in kwargs:
            :param LinkShareID [Optional]
                Your own LinkShare ID. It can be found in any link you generate from the LinkShare platform after the 'id=' parameter. It is an 11 digit alphanumeric string.
        """
        self.params = {'apiKey':api_key} #,'format':'json'}
        # self.LSNID = kwargs.get('LinkShareID')

    # This is the function to search product by UPC
    def upc_search(self, upc):
        url = API_BASE_URL + 'items'
        request_params = self.params
        request_params["upc"] = upc
        r = requests.get(url, params=request_params)
        # print(r.url)
        if r.status_code == 200 or r.status_code == 201:
            # return WalmartProduct(r.json())
            # This is for collecting raw data
            return r.json()["items"][0]
        else:
            # if r.status_code == 400:
            #     #Send exception detail when it is a 400 error
            #     raise InvalidRequestException(r.status_code, detail=r.json()['errors'][0]['message'])
            # else:
            #     raise InvalidRequestException(r.status_code)
            data = {}
            data["itemId"] = -1
            data["upc"] = upc
            if r.status_code == 400:
                data["name"] = "400-" + r.json()["errors"][0]["message"]
            else:
                data["name"] = str(r.status_code) + "-" + self.get_error(r.status_code)
            return data

    # return error message
    def get_error(self, code):
        if code == 403:
            return 'Forbidden'
        elif code == 404:
            return 'Wrong endpoint'
        elif code == 414:
            return 'Request URI too long'
        elif code == 500:
            return 'Internal Server Error'
        elif code == 502:
            return 'Bad Gateway'
        elif code == 503:
            return 'Service Unavailable/ API maintenance'
        elif code == 504:
            return 'Gateway Timeout'
        else:
            return "Other Error"
