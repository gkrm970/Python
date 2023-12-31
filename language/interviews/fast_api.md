### What is fastapi and how does it differ from other web framework?
Fastapi is a modern , fast(high performance ) web framework for building APIs with python 3.7+ based on standard python type hints. It is different from other framework due to its highly performant nature , built-in API documentation, support for asynchronous programming , and automatic generation of OpenAPI and schema documentation.

### What are the benefits of using FastAPI?
The benefits of using FastAPI include high performance, built-in API documentation , support for asynchronous, automatic generation of OpenAPI and schema documentation, easy integration with other python libraries, and simple deployment and cloud platforms.

### How does FastAPI handle requests and responses?
FastAPI uses the ASGI(asynchronous server gateway interface) standard to handle requests and responses, allowing for highly perfomant and scalable application. Its also provides support for HTTP method such as GET, POST, PUT, PATCH, DELETE.  as well as automatic validation  of request and response data using pydantic and error handling.

### Difference between ASGI and ?

### Difference between pydentic and pydantic?

### What is the synthax for defining a route in fastapi?
To define a route in fastapi we use the @app.route() decorator. followed by the HTTP method and the path of the route.
for example : @app.get("/api/users/{id}") define a GET route with a path parameter id.

### What are the different types of request parameter in FastAPI?
FastAPI supports the following types of request parameter:
Query parameters -> are added to the url query string.
Path parameters ->are defined in the url path.
Request body parameter -> are sent in the request body.

### What are the different types of response parameter in FastAPI?

### What is the purpose of using path parameter and query parameter?

### What is the difference between path parameter and query parameter

### What is the dependency injection in FasAPI?
Dependency injection is a process of injecting dependencies into a class or function.
Dependency injection is a design pattern used in FasAPI to handle dependencies between different components of an application .
It allows you to define dependencies once and then easily inject them into other components that require them.


### How do you define and use a dependency in FastAPI?
To define a dependency in FastAPI , You Use "Depends" function decorator. You can define dependencies at the endpoint level or at the application level . 
Once defined, you can then use the dependency as a parameter in your endpoint function, and FastAPI will automatically handle the injection of the dependency.

### What are middleware in FastAPI?
Middleware is a piece of code that runs between the request and response phases of an HTTP request.
Middleware in FastAPI are functions that are executed before or after an endpoint function is called.
They can be used to modify requests and responses, add additional functionality to an endpoint, or perform authentication and validation .
Middleware function can be added to an application using the "Middleware" class, and they can be added globally or to specific endpoints.

### What are the different types of middleware in FastAPI?



### What is the purpose of using middleware in FastAPI?

### How do you add middleware to a FastAPI app?
To add middleware to a application, you create a new instance of the "Middleware" class and pass in the middleware functions that you want to use. You can rhen add the middleware to the application using the add_middleware() method.


### What is the difference between path parameters and query parameters in FastAPI?
Path parameter are part oof the url and are used to specify a specific resource or endpoint.
Query parameters are used to filter or sort the results of request and are passed as part of the query string.
In FastAPI path parameters are defined using curly braces in the url path, while query parameters are defined as function parameters with default values.

### How does FastAPI handle exception and errors?
FastAPI has an exception handling mechanism that catches exceptions and return appropriate error responses to the client.
The system is customizable and can be extended with custom exception handles.

### How do you handle CORS in FASTAPI?
FastAPI has built-in middleware for CORS handling . You can use the fastapi.middleware.cors module (import CORSMiddleware) to configure CORS for your application.

### Where is CORS used in FastAPI?
Answer: CORS is used in FastAPI to enable cross-origin resource sharing.
 

### What is the purpose of using CORS in FastAPI?

### What is Pydantic and how is it used in FastAPI?
Pydantic is a data validation and settings management library for python. FastAPI uses pydantic for request and response validation, and for generating OPENAPI documentation.

### What is the difference between Pydantic and pydentic?

### What is OpenAPI and how is it used in FastAPI?

### What is the synthax for defining the response model in FASTAPI?
You can define a response model using the "Response" decorator and a Pydantic model class.
For example : @app.get("/api/users/{id}", response_model=UserOut)

### What is the purpose of using response model in FastAPI?

### What is the difference between OpenAPI and Swagger if there is any?

### What are background task in FASTAPI?
Background task are tasks that run asynchronously in the background, independent of the client request/response cycle. They can be used for tasks such as sending emails or updating database records or performing database clean-up performing other background tasks.

### What is the purpose of using background task in FastAPI?

### How do you use background task in FASTAPI?
You can define background task using the "BackgroundTasks" decorator. For example :dependency and the "background"  decorator.
For example async def send_email(email:str, background_tasks: BackgroundTasks)

### What is the purposes of WebSocket in FastAPI?
WebSocket allow for real-time communication between the client and server. FastAPI has builtin support for WebSockets , allowing for easy implementation of real-time features/ application.

### What is WebSocket and how is it used in FastAPI?

### How do you implement WebSocket in FastAPI?
You can use the "WebSocket" decorator. For example : @app.websocket("/ws/{item_id}")
You can Implement WebSockets in FastAPI using the WebSocket endpoint decorator and the "WebSocketDisconnect"  exception for handling disconnections. for example @app.websocket("/ws/{item_id}")  

### What is FastAPI support for OAUTH2 and authentication?
FastAPI has built-in support for OAUTH2 and authentication . You can use Oauth2 with JWT Bearer token as the authentication method, and FastAPI provides easy-to-use decorators to protect the endpoints with authentication.

### Why OAUTH2 with JWT Bearer token is used in FastAPI?

### Can you use FastAPI with PostgresSQL database?
Answer: Yes, FastAPI can be used with PostgresSQL database.

### Code implementation for Oauth2 with JWT Bearer token in FastAPI

### How do you secure a FastAPI app?
There are a several way to secure a fastapi application, including using https, setting strong passwords, implimenting authentication and authorization, validation user inputs , and using middleware for security headers.

### What are the benefits of using fastapi with docker?
Fastapi and Docker make a greate combination for developing, testing and deploying applications.
Docker simplifies the process of managing dependencies and environment, and Fastapis performance and ease of use make it and ideal framework for containerization.

### How do you deploy fastapi application in docker?
Answer: You can deploy fastapi application in docker using the docker-compose.yml file.

### How do you deploy fastapi application in kubernetes?
Answer: You can deploy fastapi application in kubernetes using the kubernetes.yml file.

### How do you deploy fastapi application to a cloud platform like AWS and HEROKU?
Answer: You can deploy fastapi application to a cloud platform like AWS and HEROKU using containerization or a platform-as-a-service(Pass) offering. Docker is a popular choice for containerization, and cloud providers like AWS and heroku offer easy to use Pass solutions for deploying Fastapi application.

### What is Fastapi support for testing?
Fast api provides builtin support for testing using pytest you can write unit test and integration test for you fastapi application , and fastapi provides test client to simulate request and responses for your endpoints.

### What are some best practices for developing and deploying fastapi applications?
Some best practices for developing and deploying fastapi application include using Pydantic for data validation, implementing caching and rate limiting , sung logging and monotoring for debugging and performance optimization, and following security best practices

### How does fastapi handle scalability and performance?
Fastapi is designed for high performance and scalable application. It uses the ASGI(asynchronous server gateway interface) standard to handle requests and responses, allowing for highly performant and scalable application.
It uses asynchronous programming with Pythons asyncio library to handle multiple request simultaneously , and its code generation feature optimized code for each endpoint. fastapi also has built in support for caching and rate limiting to improve performance.
