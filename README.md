# Introduction
This is a Flask application designed to parse JSON data, both JSON arrays and individual JSON objects. It provides two endpoints: one for parsing JSON arrays (/parseJsonArray) and another for parsing individual JSON objects (/parseJson).

# Installation
## Clone the repository: 
https://github.com/anjaneyak10/JsonParserFlask.git

## Install the required dependencies:
pip install -r requirements.txt

# Usage
## Run the Flask application:
python main.py

Access the endpoints using a web browser or an API testing tool like Postman:

Parsing JSON Array: Send a POST request to /parseJsonArray with a JSON array in the request body. The application will parse the array and return the parsed data.

## Example request:

POST /parseJsonArray
Content-Type: application/json

[
  {"name": "John", "age": 30},
  {"name": "Alice", "age": 25}
]


Parsing JSON Object: Send a POST request to /parseJson with a JSON object in the request body. The application will parse the object and return the parsed data.

Example request:
POST /parseJson
Content-Type: application/json

{
  "name": "Bob",
  "age": 35,
  "city": "New York"
}



POST / parseJsonArray

[
{
  "name": "Bob",
  "age": 35,
  "city": "New York"
},
{
  "name": "Allica",
  "age": 90,
  "city": "New York"
}
]

You will get the output in the form of dictionary. 
