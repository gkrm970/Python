# Main Flask application file (main.py):
"""In this example, we separate the database file (database.py), the database models file (models.py),
and the schemas file (schemas.py) from the main Flask application file (main.py). This separation helps keep the code
organized and modular.

Make sure to adjust the database connection URL in the main.py file according to your database setup.

By separating the code into multiple files, you can easily manage and maintain different aspects of your Flask API
project, such as the database connection, models, and schemas.

"""
from flask import Flask, jsonify, request, current_app
from database import db
from models import Book
from schemas import BookCreateRequest, BookUpdateRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@localhost/database_name'
db.init_app(app)

# API endpoints
@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify(books)

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@app.route("/books", methods=["POST"])
def create_book():
    with current_app.app_context():
        request_data = request.get_json()
        book_request = BookCreateRequest(**request_data)
        book = Book(title=book_request.title, author=book_request.author)
        db.session.add(book)
        db.session.commit()
        return jsonify(book), 201

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = Book.query.get(book_id)
    if book:
        request_data = request.get_json()
        book_request = BookUpdateRequest(**request_data)
        book.title = book_request.title
        book.author = book_request.author
        db.session.commit()
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted successfully"})
    return jsonify({"error": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
