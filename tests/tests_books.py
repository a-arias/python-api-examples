import pytest
import requests

# Replace this URL with the URL of your running API
BASE_URL = 'http://127.0.0.1:5000'

@pytest.fixture
def sample_book():
    return {
        "title": "Sample Book",
        "author": "Sample Author",
        "publication_date": "01-01-2000"
    }

#Asserts that all the books count are more than 0 
def test_get_all_books():
    response = requests.get(f'{BASE_URL}/books')
    assert response.status_code == 200
    assert len(response.json()) > 0

#Asserts that book by id = 2 has correct information and data types
def test_get_book_by_id():
    response = requests.get(f'{BASE_URL}/books/2')
    assert response.status_code == 200
    #Asserts book information
    assert response.json()['id'] == 2
    assert response.json()['title'] == "The Alchemist"
    assert response.json()['author'] == "Paulo Coelho"
    assert response.json()['publication_date'] == "10-10-1988"
    # Asserts data types
    assert isinstance(response.json()["id"], int)
    assert isinstance(response.json()["title"], str)
    assert isinstance(response.json()["author"], str)
    assert isinstance(response.json()["publication_date"], str)


#Asserts we are able to create a new book passing sample_book fixture as parameter
def test_create_book(sample_book):
    response = requests.post(f'{BASE_URL}/books', json=sample_book)
    assert response.status_code == 201
    assert response.json()['title'] == "Sample Book"
    assert response.json()['author'] == "Sample Author"
    assert response.json()['publication_date'] == "01-01-2000"

#Asserts we are able to update a book with sample book fixture
def test_update_book(sample_book):
    response = requests.put(f'{BASE_URL}/books/3', json=sample_book)
    assert response.status_code == 200
    assert response.json()['title'] == sample_book['title']
    assert response.json()['author'] == sample_book['author']
    assert response.json()['publication_date'] == sample_book['publication_date']


#Asserts we are able to delete the first book
def test_delete_book():
    response = requests.delete(f'{BASE_URL}/books/1')
    assert response.status_code == 200
    assert response.json()["message"] == "Book deleted"

    response = requests.get(f'{BASE_URL}/books/1')
    assert response.status_code == 404


if __name__ == '__main__':
    pytest.main()