from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for storing books (in-memory storage)
books = [
    {"id": 1, "title": "The Shining", "author": "Stephen King", "publication_date": "01-28-1977"},
    {"id": 2, "title": "The Alchemist", "author": "Paulo Coelho", "publication_date": "10-10-1988"},
    {"id": 3, "title": "The Personal MBA", "author": "Josh Kaufman", "publication_date": "12-30-2010"},
    {"id": 4, "title": "The Lean Startup", "author": "Eric Ries", "publication_date": "05-05-2011"},
]

# Route to display welcome message
@app.route('/')
def hello_world():
    return 'Welcome to books app!'

# Route to retrieve all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Route to retrieve a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# Route to create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if "title" in data and "author" in data:
        new_book = {
            "id": len(books) + 1,
            "title": data["title"],
            "author": data["author"],
            "publication_date": data["publication_date"],
        }
        books.append(new_book)
        return jsonify(new_book), 201
    return jsonify({"error": "Invalid data"}), 400

# Route to update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = next((book for book in books if book['id'] == book_id), None)
    if book and "title" in data and "author" and "publication_date" in data:
        book["title"] = data["title"]
        book["author"] = data["author"]
        book["publication_date"] = data["publication_date"]
        return jsonify(book)
    return jsonify({"error": "Book not found or invalid data"}), 404

# Route to delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({"message": "Book deleted"})

if __name__ == '__main__':
    app.run(debug=True)