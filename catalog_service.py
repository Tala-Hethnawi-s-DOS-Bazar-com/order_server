import requests
import json


class CatalogService:
    __CATALOG_SERVER_URL = "http://172.18.0.40:5000/"
    __INFO_ENDPOINT = "info/{book_id}"
    __UPDATE_QUANTITY_ENDPOINT = "update/{book_id}"

    def getBookInfo(self, book_id):
        # get book details from Catalog MS
        url = self.__CATALOG_SERVER_URL + self.__INFO_ENDPOINT.format(book_id=book_id)
        response = requests.get(url=url)
        if response.status_code >= 400:
            raise Exception("Failed to get book info.")
        return json.loads(response.content)

    def updateBookQuantity(self, book_id, quantity):
        # update quantity on catalog MS
        url = self.__CATALOG_SERVER_URL + self.__UPDATE_QUANTITY_ENDPOINT.format(book_id=book_id)
        response = requests.put(url=url, json={"quantity": quantity})
        if response.status_code >= 400:
            raise Exception("Failed to decrement book quantity.")
