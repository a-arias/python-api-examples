# python-api-testing-example
Pytest is a mature full-featured Python testing frame that helps you write and run tests in Python.
The requests module allows you to send HTTP requests using Python

## Getting started
* Download python3  on [Mac](https://docs.python-guide.org/starting/install3/osx/) or [Windows](https://www.python.org/downloads/)
* To download and install pytest, run this command from the terminal : `pip install pytest`
* To download and install requests, run this command from the terminal : `pip install requests`
* To download report librart: `pip install pytest-html`

## Running tests
* Clone the repo: `git clone git@github.com:a-arias/python-api-examples.git`
* Open folder `cd python-api-examples`
* run the Flask server in order to get access to the Book endpoints: `python3 app.py`
* Run the tests in another terminal tab with: `pytest tests/tests_books.py`


## Create tests reports
* To generate HTML results, run the following command : `pytest tests/tests_books.py --html=report.html` a report should be added to the folder


For more on Pytest, go [here.](https://docs.pytest.org/en/stable/)