from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Define the path to the data file
data_file = "data/books.json"

# Function to read data from the JSON file
def read_data():
    try:
        with open(data_file, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

# Function to write data to the JSON file
def write_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)


# Route to display welcome message
@app.route('/')
def hello_world():
    return 'Welcome to books app!'

# Route to retrieve all books
@app.route('/books', methods=['GET'])
def get_books():
    data = read_data()
    return jsonify(data)

# Route to retrieve a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    data = read_data()
    book = next((book for book in data if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404


# Route to create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = read_data()
    new_book = request.get_json()
    if "title" in new_book and "author" in new_book and "publication_date" in new_book:
        new_book["id"] = max((book['id'] for book in data), default=0) + 1
        data.append(new_book)
        write_data(data)
        return jsonify(new_book), 201
    return jsonify({"error": "Invalid data"}), 400

# Route to update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = read_data()
    book = next((book for book in data if book['id'] == book_id), None)
    if book:
        updated_data = request.get_json()
        book.update(updated_data)
        write_data(data)
        return jsonify(book)
    return jsonify({"error": "Book not found or invalid data"}), 404

# Route to delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    data = read_data()
    book = next((book for book in data if book['id'] == book_id), None)
    if book:
        data.remove(book)
        write_data(data)
        return jsonify({"message": "Book deleted"})
    return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)