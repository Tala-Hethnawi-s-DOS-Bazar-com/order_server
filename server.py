from flask import Flask, jsonify

from catalog_service import CatalogService
from models import Order
from utils import session

app = Flask(__name__)


@app.route('/purchase/<book_id>', methods=["POST"])
def purchase(book_id):
    try:
        # get book info
        catalog_service = CatalogService()
        book_info = catalog_service.getBookInfo(book_id=book_id)
        quantity = book_info["quantity"]
        # check if book is available
        if quantity < 1:
            return jsonify({"error": "Book not available in stock."}), 400
        else:
            order = Order(book_id=book_id)
            session.add(order)
            catalog_service.updateBookQuantity(book_id=book_id, quantity=(quantity-1))
            session.commit()
            return jsonify({"message": "Bought book {book_title}".format(book_title=book_info["title"])})
    except Exception:
        return jsonify({"error": "Sorry!, we were unable to process your order"}), 500
