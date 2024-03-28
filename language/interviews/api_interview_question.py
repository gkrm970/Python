# top 25 api testing interview questions
#
# 1 what all challenges are there in api testing?
#     API documentation
#     Access to DB  ---> this is happening when API are from a third part company where database details are not shared?
import json
#     authorization overhead   -> type of authentication

# 2 what is the difference between  put and post?
#     put is used to update data in the database or server
#     post is used to create new data in the database or server

# 3 what are the different ways to send requests in api testing?
#     Get method: It enables you to retrieve data from the server
#     Post method: It enables you to send data to the server
#     Put method: It enables you to update data in the server
#     Delete method: It enables you to delete data from the server
#     Patch method: It enables you to partially update data in the server

# 4 List out few authentication techniques used in APIs?
#     Session/Cookie-based authentication
#     Basic authentication   ---user name and password
#     Token-based authentication ---JWT
#     OAuth 2.0 authentication ----OAuth

# 5. why API testing determined as the most suitable form automation testing?

# 6. what is the Rest API?
#     REST stands for representational state transfer. It is an architectural style that defines a set of endpoints that can be called without specifying the underlying transport protocol.
#     or Its a set of funtions helping developers in performing request and receive responses. interation is made through HTTP protocol in REST AP.

# 7. what exactly need to verfy in API testing ?
#     a) we will need to verify the status code
#     b) we will need to verify the response body
#     c) we will need to verify the headers
#     d) we will need to verify the cookies
# e) response time should be less than 3 seconds
# f) Error codes in cases API return any error
#     g) authorization would be checked
#   non-functional testing such as performance testing, security testing \

# 8. what are the path and query parameter for bellow API request url.
#  http://localhost:8080/api/users?name=John
#  http://localhost:8080/api/users?name=John&age=30

# 9 what are the code components of and HTTP requests in API testing?
#     Type of http request method (GET, POST, PUT, PATCH, DELETE)
# uri (URI) uniform resource identifier
# resource and parameters
# request headers which carry meta data as key value pair for http request message example json, xml
#     request body which carries data as key value pair for http request message.
# what could be the http method for bellow API scenario? answer if it is GET or POST
#     An api which has endpoint, parameters, headers and request body
# example Get request URL http://localhost:8080/api/users?name=John&age=30
#          PoST request URL http://localhost:8080/api/users
#          GET request URL http://localhost:8080/api/users/1
#          PUT request URL http://localhost:8080/api/users/1
#          PATCH request URL http://localhost:8080/api/users/1
#          DELETE request URL http://localhost:8080/api/users/1

# 10 what is the differemce between API testing and UI testing ?
# UI = User Interface testing is the testing of
# graphical user interface  the focus of ui testing is on the look and feel of the application . in ui testing we are
# testing the user experience of the application in real time. with app elements such as images , fonts layout etc

# checked API = API testing is testing the server side of the application. it allows the communication between two
# software systems . APi testing works on back end server also known as back end testing between client and server

# 11 what protocol is used by the RESTFUL web server?
#     RESTFUL web services uses HTTP protocol for communication , they use the http protocol as a medium of communication. between the client and server

# 12 what is the soap web services?
#     SOAP stands for Simple Object Access Protocol. It is a messaging protocol that is used to exchange data between different applications.
#     it is a xml based messaging protocol. it helps in exchanging information among the computer.

# 13 how do we represent a resource in REST? OR RESTFULL web services?
#     using http methods
# 14 Can you use GET request instead of PUT request to create a resource?
#     No get quest only allowed to read only right. it enables you to retrieve data from the server. but no craetion resource , put or post method should be uded to craete a resouce

# post should be used when client send the page to the server and then the server lets the client know where it put it . PUT should be used when client specifies the location of the page on the server.


# 15 what is the difference between REST and SOAP?
# 15 can you use post request instead of put request to create a resource?
#     Yes we can . because post is super set of other http method except get.

# 16 what is you understand by payload in RESTfull web services?
#     it is data sent to the server. generally represented in json format in in restfull API

# 17.what is the difference between path and query parameter
# 18 what is Rest Assured?
#     its is java library which can automate REST API testing.

# 19 how would you define API details in Rest Asurred automation

# 20 what is Json serialization and deserialization in Rest Assured?
# 20 what is Json serialization and deserialization in python
#     serialize =
# json_string = '{"name": "Bob", "scores": [85, 90, 95]}'
# python_object = json.loads(json_string)
# print(python_object)

# deserialize
# json.loads(json_string)

# 20 what is Json serialization and deserialization
# 21 list out few command json parsing technique used in Rest Assured automation
# 21 list out few command json parsing technique in python automation
# 1. json.loads() (String Parsing):
#
# Ideal for parsing JSON data stored in a Python string variable.
# Example:
# import json
#
# json_string = '{"name": "Alice", "age": 30}'
# data = json.loads(json_string)
# print(data["name"])  # Output: Alice

# json.load() (File Parsing):
#
# Designed for parsing JSON data from a file on disk.
# Example:
# Python
# import json
#
# with open("data.json", "r") as file:
#     data = json.load(file)
# print(data["age"])  # Assuming "data.json" has appropriate key-value pairs

# 22 how would you send attachement to API in python automation
# Using with open("file_path", "rb") as f:   in binary mode
import requests

# def send_attachment_with_requests(api_url, file_path, data):
#     with open(file_path, 'rb') as f:
#         file_data = {'attachment': (f.name, f)}
#         payload = {**data, **file_data}
#         encoded_data = requests.MultipartEncoder(payload)
#         headers = {'Content-Type': encoded_data.content_type}
#         response = requests.post(api_url, data=encoded_data, headers=headers)
#         # Handle the response (check status code, etc.)
#         return response
#
# # Example usage
# data = {'name': 'Alice', 'message': 'This is a message with an attachment'}
# file_path = 'path/to/your/file.txt'
# api_url = 'https://your-api.com/upload'
# response = send_attachment_with_requests(api_url, file_path, data)
# print(response.status_code)  # Check for successful upload

# 23 different status codes and there description.
#     200 ok -> The request was successful
#     201 created -> The request was successful and a new resource was created
#     204 no content -> The request was successful but no content was returned
#     400 bad request -> The request was invalid
#     401 unauthorized -> The request was unauthorized
#     403 forbidden -> The request was forbidden, no permission to access the resource/api
#     404 not found -> The requested resource was not found
#     405 method not allowed -> The request method was not allowed
#     409 conflict -> The request was successful but the resource was not created because of a conflict
#     500 internal server error -> The request was unsuccessful due to an internal server error
#     502 bad gateway -> The request was unsuccessful due to a bad gateway
#     503 service unavailable -> The request was unsuccessful due to a service unavailable

# 24

