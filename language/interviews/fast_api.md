### What is fastapi and how does it differ from other web framework?

Fastapi is a modern , fast(high performance ) web framework for building APIs with
python
3.7+ based on standard python type hints.
It is different from other framework due to its highly performant nature ,
built-in API documentation, support for asynchronous programming , and
automatic generation of OpenAPI and schema documentation.

FastAPI is designed for asynchronous programming, it does support synchronous 
programming as well.

### What are the benefits of using FastAPI?

The benefits of using FastAPI include high performance, built-in API documentation ,
support for asynchronous, automatic generation of OpenAPI and schema documentation,
easy integration with other python libraries, and simple deployment and cloud platforms.

    Easy integration with other python libraries mean?
    FastAPI allows you to easily integrate with other libraries like Flask, Django, 
    and FastAPI. This makes it easier to create and deploy your API.

    Easy deployment and cloud platforms how?
    FastAPI provides a simple and easy-to-use deployment and cloud platform for your API.
    
    Built-in API documentation?
    FastAPI provides built-in API documentation, which makes it easier to understand 
    and use your API.

    Automatic generation of OpenAPI and schema documentation?
    FastAPI provides automatic generation of OpenAPI and schema documentation, which 
    makes it easier to understand and use your API.

### What is asynchronous programming in FastAPI?

Asynchronous programming is a programming paradigm that allows for multiple tasks to be
executed in parallel.

### What is await in FastAPI?

The await keyword is used in FastAPI to pause execution until the awaited coroutine is
complete mean original or previous operation get completed.

### Difference between async and await?

async and await are keywords in Python that are used in conjunction with asynchronous
programming to write asynchronous code more easily. They are often used with the asyncio
module.
Example:
async def my_coroutine():

# Some asynchronous code here

result = await some_async_function()
return result

await: This keyword is used inside an async function to pause execution until the
awaited coroutine is complete. When the coroutine is paused at an await expression,
it allows other coroutines to run concurrently.
Example:
async def another_coroutine():
result = await my_coroutine()

print(result)

In summary, async is used to define a coroutine function, and await is used within a
coroutine to pause execution until the awaited asynchronous operation is completed.
Together, they enable the creation and execution of asynchronous code in a more readable
and structured manner. 
Example:
Asynchronous programming is particularly useful for I/O-bound
operations where tasks can be efficiently scheduled to run concurrently,
improving overall program performance.

### What is coroutine function in FastAPI?

In FastAPI, a coroutine function is a special kind of function that is defined using the
async def syntax in Python. 
FastAPI uses asynchronous programming to handle high performance and concurrency by 
allowing the server to efficiently handle many requests simultaneously.

In FastAPI, route handlers can be asynchronous by using the async def syntax to define
coroutine functions. These coroutine functions can then use the await keyword to perform
asynchronous operations, such as making requests to databases or external APIs without
blocking the entire server.

### What is synchronous programming in FastAPI?

While FastAPI is designed for asynchronous programming, it does support synchronous 
programming as well. Here's a breakdown of synchronous programming in FastAPI and key 
points to remember:

Synchronous Programming in FastAPI:

Sequential Execution: Tasks are executed one at a time, in the order they are received.
Blocking Operations: When a function encounters a blocking operation (e.g., I/O, 
database calls), it halts execution until the operation completes, preventing other 
tasks from running.
Standard Functions: Synchronous functions are defined using the regular def keyword, 
without async.
No await Keyword: Synchronous functions don't use the await keyword.
Can Be Used for Simple Tasks: They are suitable for short, non-blocking tasks or when 
integrating with synchronous libraries.

Key Considerations:

Performance: Synchronous programming can impact performance negatively, especially when 
handling multiple concurrent requests or I/O-bound tasks.
Context Switching: FastAPI still switches between tasks to handle multiple requests, 
even with synchronous functions. However, it's less efficient than true asynchronous 
context switching.
Thread Pools: FastAPI uses a thread pool to handle multiple requests concurrently, even with synchronous functions. However, each thread can only handle one task at a time, limiting concurrency.
Example:

def sync_function():
    # Perform a synchronous task
    result = some_blocking_operation()
    return result

@app.get("/sync-endpoint")
def sync_endpoint():
    data = sync_function()
    return {"data": data}


When to Use Synchronous Programming:

Simple Tasks: For quick, non-blocking operations.
Synchronous Libraries: When interacting with libraries that don't support asynchronous operations.
When to Use Asynchronous Programming:

I/O-Bound Tasks: For tasks involving network calls, database interactions, or other I/O-bound operations.
High Concurrency: When handling many concurrent requests efficiently.
Optimized Resource Usage: To maximize resource utilization and reduce response times.
In general, it's recommended to use asynchronous programming in FastAPI whenever possible to take full advantage of its performance and scalability benefits. However, understanding synchronous programming concepts is still valuable for handling specific scenarios or working with synchronous libraries.

### Difference between FastAPI and Django?

### Difference between FastAPI and Flask?

1. Focus and Performance:

FastAPI: Designed for building high-performance APIs, prioritizing speed and efficiency.
It's built on Starlette and Pydantic, leveraging asynchronous programming and type hints
for optimization.
Flask: Versatile microframework for web applications and APIs, offering flexibility and
ease of use. Its performance is generally good, but not as optimized as FastAPI for
API-specific tasks.

2. Development Style:

FastAPI: Emphasizes strict type annotations and data validation, promoting code clarity
and reducing runtime errors.
Flask: Allows more flexibility in coding style, with optional type hints and manual
validation.

3. Features:

FastAPI:
Automatic data validation and documentation
Built-in support for OpenAPI (Swagger UI)
Dependency injection
Background tasks with Celery integration
Security features like OAuth2
Flask:
Wide range of extensions for various functionalities
Flexible for different use cases

4. Community and Ecosystem:

Flask: Larger and more established community with extensive resources and third-party
libraries.
FastAPI: Growing community and ecosystem, but still relatively new compared to Flask.
When to Choose Which:

FastAPI is generally a better choice for:

Building high-performance REST APIs
Projects prioritizing speed and data validation
Teams comfortable with type annotations and modern Python features
Flask is often preferred for:

Rapid prototyping and experimentation
Small-scale web applications
Projects requiring high flexibility and customization
Teams less familiar with type annotations or preferring a less strict approach
In summary:

FastAPI excels in API development with its focus on speed, type safety, and automation.
Flask offers versatility for diverse web projects, valuing flexibility and ease of use.
The best choice depends on your specific project requirements, team preferences, and
development style.

### How does FastAPI handle requests and responses?

FastAPI uses the ASGI(asynchronous server gateway interface) standard to handle requests
and responses, allowing for highly performant and scalable application.
Its also provides support for HTTP method such as GET, POST, PUT, PATCH, DELETE.  
It also provides support for caching and rate limiting as well as automatic validation
of request and response data using pydantic and error handling.

This is especially beneficial for I/O-bound operations where the server can await
responses from databases, external APIs, or other services without wasting resources on
processing or idle waiting.

### What is The ASGI?

ASGI stands for the asynchronous server gateway interface. ASGI is a standard
for building web applications and APIs.
It is a specification for asynchronous web servers and applications in Python.
ASGI is designed to handle asynchronous communication between web servers and
web applications, allowing them to efficiently manage a large number of simultaneous
connections.

Key features of ASGI include:

Asynchronous Support: ASGI allows web applications to handle asynchronous operations,
making it suitable for applications that involve long-polling, WebSocket communication,
and other asynchronous patterns.

Scope and Lifespan: ASGI introduces the concepts of "scope" and "lifespan" to represent
the context and lifecycle of a connection.
This allows the server and application to communicate information about the connection,
such as headers and state changes.

WebSocket Support: ASGI provides native support for handling WebSocket connections,
which is essential for real-time bidirectional communication between clients and
servers.

Concurrency: ASGI servers can efficiently handle many concurrent connections by
utilizing
asynchronous programming principles, allowing them to scale well for applications with
high levels of concurrency.

One popular ASGI framework is FastAPI, which leverages ASGI to provide high-performance
asynchronous web applications in Python.
To run an ASGI application, you need an ASGI server. Some examples of ASGI servers
include Uvicorn, Hypercorn, and Daphne.

### What is WSGI?

The traditional WSGI (Web Server Gateway Interface) standard used in Python was designed
for synchronous web servers. However, with the growing need for handling concurrent
connections and long-lived connections (such as WebSockets), WSGI became less suitable.
ASGI was introduced to address this limitation.

### Difference between ASGI and WSGI?

ASGI is a standard for asynchronous web servers and applications in Python.
It is a specification for asynchronous web servers and applications in Python.
ASGI is designed to handle asynchronous communication between web servers and
web applications, allowing them to efficiently manage a large number of simultaneous
connections.

WSGI is a standard for web servers in Python. It is a specification for web servers in
Python. WSGI is designed to handle synchronous communication between web servers and
web applications, allowing them to efficiently manage a large number of one after
another
connections.

### W

WebShat is WebSockets?ockets is a protocol that allows two-way communication between two
endpoints over a
connection. It is commonly used for real-time communication between clients and servers.

### What is the synthax for defining a route in fastapi?

To define a route in fastapi we use the @app.route() decorator followed by the
HTTP method and the path of the route.
For example : @app.get("/api/users/{id}") define a GET route with a path parameter id.

### What are the different types of request parameter in FastAPI?

FastAPI supports the following types of request parameter:
Query parameters -> are added to the url query string.
Path parameters ->are defined in the url path.
Request body parameter -> are sent in the request body.

Path parameters and query parameters are both ways to pass information within a URL,
but they serve different purposes:

Path parameters are used to identify a specific resource within a RESTful API.
They are embedded within the URL path itself, enclosed in curly braces ({}).

Key characteristics:
Mandatory: A path parameter is typically required for the API to function correctly.
Uniquely identify resources: A unique resource is mapped to each combination of path
parameter values.
Part of the URL structure: They contribute to the overall structure and hierarchy of the
API.

Example:
/users/123 (retrieves user with ID 123)
/posts/456/comments (retrieves comments for post 456)

Query parameters, on the other hand, are used to filter or modify the request in some
way.
They are appended to the end of a URL, following a question mark (?), and consist of
key-value pairs separated by ampersands (&).

Key characteristics:
Optional: Query parameters are often optional, providing additional customization for
the request.
Filtering and sorting: They are commonly used for filtering, sorting, searching,
or pagination.
Not part of the resource hierarchy: They don't directly map to specific resources.

Example:
/users?city=Bangalore&age=30 (filters users by city and age)
/posts?sort=popularity (sorts posts by popularity)

When to use which:
Use path parameters to identify a specific resource or a hierarchy of resources.
Use query parameters to filter, sort, or modify the request in a non-hierarchical way.
Remember:

### What are the different types of response parameter in FastAPI?

### What is the dependency injection in FasAPI?

Dependency injection is a process of injecting dependencies into a class or function.
Dependency injection is a design pattern used in FasAPI to handle dependencies between
different components of an application .
It allows you to define dependencies once and then easily inject them into other
components that require them.

### How do you define and use a dependency in FastAPI?

To define a dependency in FastAPI , You Use "Depends" function decorator. You can define
dependencies at the endpoint level or at the application level .
Once defined, you can then use the dependency as a parameter in your endpoint function,
and FastAPI will automatically handle the injection of the dependency.

Dependencies are functions that perform tasks or gather information before a path
operation is executed. They offer a powerful way to handle common tasks like
authentication, database connections, data validation, and more, promoting code
re-usability and maintainability.

Here's how to define and use dependencies in FastAPI:

1. Define a Dependency Function:
   Create a function that performs the necessary actions.
   It can take parameters as needed, including request information.
   It can return data to be used in the path operation.

from fastapi import Depends, HTTPException, status

async def get_current_user(token: str = Depends(get_token_header)):
user = await authenticate_user(token)
if not user:
raise HTTPException(
status_code=status.HTTP_401_UNAUTHORIZED,
detail="Invalid authentication credentials",
headers={"WWW-Authenticate": "Bearer"},
)
return user

2. Declare the Dependency in a Path Operation:

Use the Depends function in the path operation's parameters.
Pass the dependency function you defined as an argument to Depends.
The result of the dependency function will be injected as a parameter to the path
operation.

from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
async def read_user_me(current_user: User = Depends(get_current_user)):
return current_user

### What are middleware in FastAPI?

Middleware is a piece of code that runs between the request and response phases of an
HTTP request.
Middleware in FastAPI are functions that are executed before or after an endpoint
function is called.
They can be used to modify requests and responses, add additional functionality to an
endpoint, or perform authentication and validation .
Middleware function can be added to an application using the "Middleware" class,
and they can be added globally or to specific endpoints.

### What is the purpose of using middleware in FastAPI?

Middleware in FastAPI serves as a flexible and reusable layer to intercept and modify
requests and responses before they reach the actual path operations.
This empowers you to implement various cross-cutting concerns and features in a
centralized manner, promoting cleaner code organization and better maintainability.

Here's a breakdown of its key purposes:

1. Centralized Functionality:

Authentication and authorization: Middleware can verify user credentials and enforce
access control rules for all endpoints.
Logging and monitoring: Log request details, response times, and potential errors for
analysis and debugging.
Content compression: Reduce response sizes for faster delivery using techniques like
gzip compression.
CORS configuration: Enable cross-origin requests, specifying allowed origins and
headers.
Error handling: Capture and log exceptions, potentially returning custom error
responses.

2. Code Separation and Re-usability:

Keep path operations focused: Middleware isolates cross-cutting concerns, making path
operation code more readable and maintainable.
Enhance code organization: Reuse middleware across multiple endpoints or even projects.

3. Extensibility:

Custom functionality: Implement bespoke logic, such as rate limiting, request
validation, or data transformations.

4. Flexibility:

Apply selectively: Use middleware for specific routes or globally for the entire
application.
Chain multiple middleware: Combine different middleware functions to create a pipeline
of processing steps.
In essence, middleware in FastAPI offers a powerful mechanism to:

Streamline common tasks
Enforce consistent behavior across endpoints
Enhance code organization and maintainability
Build extensible and flexible API applications
By effectively leveraging middleware, you can construct well-structured, robust, and
feature-rich APIs with FastAPI.

### How do you add middleware to a FastAPI app?

To add middleware to a application, you create a new instance of the "Middleware" class
and pass in the middleware functions that you want to use. You can then add the
middleware to the application using the add_middleware() method.

### How do you implement middleware in FastAPI?

To implement middleware in FastAPI, you can use the "Middleware" class and its
add_middleware() method.

Here's a step-by-step guide on implementing middleware in FastAPI:

1. Define a Middleware Function:

Create an async function that accepts two parameters:
request: The incoming request object.
call_next: A function used to pass the request to the next middleware or path operation
in the chain.
Within the function, perform any desired actions on the request or response.

Example:

from fastapi import FastAPI, Request

async def simple_middleware(request: Request, call_next):
start_time = time.time()
response = await call_next(request)
process_time = time.time() - start_time
print(f"Request processed in {process_time:.2f} seconds")
return response

2. Register the Middleware:

Use the @app.middleware("http") decorator to register the middleware function with your
FastAPI application.
Example:

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
response = await simple_middleware(request, call_next)  # Chaining middleware
response.headers["X-Process-Time"] = str(response.elapsed.total_seconds())
return response

Key Points:

Middleware functions are executed in the order they are registered.
Employ call_next(request) to pass the request to the next middleware or path operation.
Middleware can modify both requests and responses.
Access request information like headers, body, cookies, etc. through the request object.
Customize response headers or content as needed.
Common Use Cases:

Logging and monitoring
Authentication and authorization
Content compression
CORS configuration
Error handling
Rate limiting
Data transformations
By effectively implementing middleware, you can create more robust, efficient, and
secure FastAPI applications.

### What is the difference between path parameters and query parameters in FastAPI?

Path parameter are part of the url and are used to specify a specific resource or
endpoint.
Query parameters are used to filter or sort the results of request and are passed as
part
of the query string.
In FastAPI path parameters are defined using curly braces in the url path, while query
parameters are defined as function parameters with default values.

### How does FastAPI handle exception and errors?

FastAPI has an exception handling mechanism that catches exceptions and return
appropriate error responses to the client.
HTTPException
RequestValidationError

Custom Exception Handling:

Define Exception Handlers: Use @app.exception_handler(ExceptionType) to handle specific
exceptions.
Example: @app.exception_handler(DatabaseError)
Override Default Handlers: Use @app.exception_handler(HTTPException) or
@app.exception_handler(RequestValidationError) to customize default behavior.

The system is customizable and can be extended with custom exception handles.

Key Points:

Pydantic Validation: FastAPI leverages Pydantic for data validation, raising
RequestValidationError for invalid inputs.
Exception Raising: Raise HTTPException to intentionally return specific errors with
appropriate status codes and messages.
Customization: Override default exception handlers for tailored error responses and
logging.

### What is CORS in FASTAPI?

CORS stands for Cross-Origin Resource Sharing. It is a mechanism that allows
cross-origin resources to communicate.

### How do you handle CORS in FASTAPI?

FastAPI has built-in middleware for CORS handling. You can use the
fastapi.middleware.cors
import CORSMiddleware module to configure CORS for your application.

### How do you implement CORS in FASTAPI?

1. Import the CORSMiddleware:

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

2. Create a list of allowed origins:

origins = [
"http://localhost:3000", # Allow requests from your frontend on port 3000
"https://www.example.com", # Allow requests from your production domain
]

3. Add the CORSMiddleware to your FastAPI app:

app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

Explanation of CORSMiddleware parameters:

allow_origins: A list of allowed origins (domains or regex patterns) that can make
cross-origin requests.
allow_credentials: Set to True to allow cookies and other credentials to be sent in
cross-origin requests.
allow_methods: A list of allowed HTTP methods (e.g., "GET", "POST", "PUT", "DELETE").
Use ["*"] to allow all methods.
allow_headers: A list of allowed headers that can be sent in cross-origin requests.
Use ["*"] to allow all headers.

Key Points:
Security: Configure CORS carefully to avoid potential security vulnerabilities.
Development and Production: Adjust allowed origins appropriately for development and
production environments.
Flexibility: Customize CORS settings based on your specific requirements.

@app.get("/hello")
async def hello():
return {"message": "Hello from FastAPI with CORS enabled!"}

With this setup, browsers will allow cross-origin requests from the specified origins,
enabling your frontend to interact with your FastAPI backend without CORS issues.

### What is the purpose of using CORS in FastAPI?

The purpose of using CORS (Cross-Origin Resource Sharing) in FastAPI is to enable web
applications running on different domains to securely communicate with each other.
It addresses a browser security mechanism that restricts web pages from making requests
to a different domain than the one that served the web page.

Here's why CORS is crucial in modern web development:

1. Breaking Down Domain Barriers:

Modern web applications often involve multiple domains or subdomains for frontend,
backend, and third-party services.
CORS allows these components to interact seamlessly, even if they reside on different
origins.

2. Enabling Cross-Origin Requests:

Without CORS, browsers would block requests initiated from a different domain,
hindering data exchange and functionality.
CORS provides a controlled way to permit cross-origin requests, facilitating
communication between different parts of your application.

3. Enhancing Security:

CORS isn't just about enabling cross-origin communication; it's also about doing it
securely.
You can explicitly specify which origins are allowed to access your FastAPI backend,
ensuring data integrity and preventing unauthorized access attempts.
This helps protect sensitive data and resources from unauthorized domains.

4. Facilitating Frontend Development:

CORS is particularly essential for single-page applications (SPAs) and frontend
frameworks that make extensive use of API calls.
By enabling CORS, you can streamline development and testing processes, as your frontend
can directly interact with your FastAPI backend without encountering browser
restrictions.

5. Promoting Flexibility and Integration:

CORS empowers you to create modular and interconnected web applications that leverage
services from various domains.
It fosters integration with third-party APIs and services, expanding the capabilities
of your web applications.
In essence, CORS plays a vital role in enabling secure and flexible cross-origin
communication in modern web development, allowing for the seamless integration of
different components and services within your FastAPI applications.

### What is Pydantic and how is it used in FastAPI?

Pydantic is a data validation and settings management library for python.
FastAPI uses pydantic for request and response validation, and for generating OPENAPI
documentation.

**In summary, Pydantic plays a crucial role in:

Ensuring data integrity and consistency
Streamlining data handling
Generating comprehensive API documentation
Facilitating database interactions
Enhancing performance and scalability.

### What is OpenAPI and how is it used in FastAPI?

OpenAPI (formerly known as Swagger) is an open-source specification for defining and
describing RESTful APIs. It provides a standard format for documenting APIs,
making them easier to understand, consume, and integrate with other systems.
FastAPI tightly integrates with OpenAPI, offering several benefits:

Automatic OpenAPI Schema Generation:

From Code: FastAPI automatically generates an OpenAPI schema (usually in JSON or YAML
format) based on your path operations, models, and dependencies. This schema captures
the structure, endpoints, and expected inputs/outputs of your API.
Interactive Documentation: FastAPI leverages this schema to provide interactive API
documentation, allowing users to explore API endpoints, try out requests, and visualize
responses directly in a browser. This fosters better understanding and usability of your
API.

Code Generation from OpenAPI Schema:

Reverse Engineering: You can also use existing OpenAPI schemas to generate FastAPI code,
essentially reverse-engineering an API from its definition. This can accelerate
development and ensure consistency between documentation and implementation.

Third-Party Tool Integration:

Wide Compatibility: The OpenAPI schema serves as a common language for various tools and
services, including:
API design tools
API testing tools
Code generators
API gateways
API monitoring tools

Expanded Ecosystem: This compatibility opens up a wide range of tools and services that
can interact with your FastAPI API, enhancing its development, testing, deployment, and
management.

Key Advantages in FastAPI:

Automatic Documentation: FastAPI's seamless OpenAPI integration streamlines API
documentation, saving time and ensuring accuracy.
Interactive Exploration: The interactive API docs powered by OpenAPI promote better
understanding and usability for developers consuming your API.
Tool Interoperability: OpenAPI compatibility unlocks a rich ecosystem of tools and
services to support various aspects of API development and management.
In essence, FastAPI's embrace of OpenAPI fosters:

Clearer API definitions
Better documentation
Enhanced discoverability
Improved consistency
Expanded interoperability with external tools and services
By effectively leveraging OpenAPI, FastAPI empowers you to create well-defined,
well-documented, and easily consumable APIs that seamlessly integrate into modern
API-driven architectures.

### What is the synthax for defining the response model in FASTAPI?

You can define a response model using the "Response" decorator and a Pydantic model
class.
For example : @app.get("/api/users/{id}", response_model=UserOut)

### What are background task in FASTAPI?

Background task are the tasks that run asynchronously in the background, independent of
the client request/response cycle. They can be used for tasks such as sending emails or
updating database records or performing database clean-up performing other background
tasks.

### What is the purpose of using background task in FastAPI?

The purpose of using background tasks in FastAPI is to execute long-running or
asynchronous operations without blocking the main request-response cycle.
This means your API can continue handling incoming requests while other tasks run in the
background, leading to a more responsive and scalable application.

Here are key reasons to use background tasks:

1. Non-Blocking Operations:

Offload Long-Running Tasks: Shift time-consuming operations like file uploads, database
interactions, external API calls, or complex computations to the background.
Maintain API Responsiveness: This prevents these tasks from delaying responses to users,
ensuring a smooth user experience.

2. Improved Performance:

Parallel Processing: Background tasks can run concurrently with other requests,
effectively utilizing available resources and potentially reducing overall response
times.
Prevent Bottlenecks: Offloading long-running tasks prevents them from becoming
bottlenecks, especially under high load.

3. Enhanced User Experience:

Faster Responses: By avoiding blocking operations, background tasks contribute to faster
and more responsive API interactions.
Improved User Satisfaction: This leads to a more seamless and satisfying user
experience.

4. Scalability:

Handle Increased Load: Background tasks help manage high-load scenarios by distributing
work across multiple processes or threads, allowing for better scalability.

5. Flexibility:

Schedule Tasks: You can schedule background tasks to run at specific times or intervals,
automating recurring processes and optimizing resource usage.
Handle Delayed Actions: Background tasks are ideal for actions that don't require
immediate results, such as sending emails, generating reports, or processing data in the
background.

### Implementation of Background Task in FastAPI

BackgroundTasks Class: FastAPI provides a BackgroundTasks class that allows you to
define and execute background tasks within path operations or dependencies.
Dependency Injection: Inject the BackgroundTasks object into your path operation
functions and use its add_task method to schedule tasks.
Asynchronous Functions: Background tasks are often implemented as asynchronous functions
using async def.
By effectively utilizing background tasks, you can create more efficient, scalable, and
user-friendly FastAPI applications that can gracefully handle long-running operations
without compromising responsiveness.

### How do you use background task in FASTAPI?

You can define background task using the "BackgroundTasks" decorator.
For example :dependency and the "background"  decorator.
For example async def send_email(email:str, background_tasks: BackgroundTasks)

### What is the purposes of WebSocket in FastAPI?

WebSocket allow for real-time communication between the client and server.
FastAPI has builtin support for WebSockets , allowing for easy implementation of
real-time features/ application.

# Implementation of WebSocket in FastAPI?

from fastapi import FastAPI, WebSocket

2. Create a WebSocket Endpoint:
   app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
await websocket.accept()
try:
while True:
data = await websocket.receive_text()
await websocket.send_text(f"Message text was: {data}")
except WebSocketDisconnect:
print("WebSocket disconnected")
)

Key Features:

Asynchronous Communication: WebSockets enable real-time, bidirectional communication
between client and server.
Persistent Connections: Connections remain open until explicitly closed, allowing for
continuous data exchange.
Full-Duplex: Both client and server can send messages at any time.

### What is FastAPI support for OAUTH2 and authentication?

FastAPI has built-in support for OAUTH2 and authentication . You can use Oauth2 with JWT
Bearer token as the authentication method, and FastAPI provides easy-to-use decorators
to protect the endpoints with authentication.

### Implementation of Oauth2 with JWT Bearer token in FastAPI

Sources
github.com/1uciuszzz/common-apis
jtuto.com/python/fastapi-oauth2-with-jwt-token-not-working/
stackoverflow.com/questions/72273998/how-to-integrate-oauth2-with-fastapi
stackoverflow.com/questions/65038133/typeerror-is-coming-when-trying-to-login
stackoverflow.com/questions/65933711/fastapi-masking-field
github.com/Baquara/fastapi-boilerplate

### What is JWT Bearer token in FastAPI?

### What are the benefits of using JWT Bearer token in FastAPI?

### What are the drawbacks of using JWT Bearer token in FastAPI?

### What are the limitations of using JWT Bearer token in FastAPI?

### How do you implement JWT Bearer token in FastAPI?

### Why OAUTH2 with JWT Bearer token is used in FastAPI?

### Can you use FastAPI with PostgresSQL database?

Answer: Yes, FastAPI can be used with PostgresSQL database.

### How do you secure a FastAPI app?

There are a several way to secure a fastapi application, including using https,
setting strong passwords, implementing authentication and authorization, validation user
inputs , and using middleware for security headers.

### What are the benefits of using fastapi with docker?

Fastapi and Docker make a greate combination for developing, testing and deploying
applications.
Docker simplifies the process of managing dependencies and environment, and FastAPI
performance and ease of use make it and ideal framework for containerization.

### How do you deploy fastapi application in docker?

Answer: You can deploy fastapi application in docker using the docker-compose.yml file.

### How do you deploy fastapi application in kubernetes?

Answer: You can deploy fastapi application in kubernetes using the kubernetes.yml file.

### How do you deploy fastapi application to a cloud platform like AWS and HEROKU?

Answer: You can deploy fastapi application to a cloud platform like AWS and HEROKU using
containerization or a platform-as-a-service(Pass) offering. Docker is a popular choice
for containerization, and cloud providers like AWS and heroku offer easy to use Pass
solutions for deploying Fastapi application.

### What is Fastapi support for testing?

Fast api provides builtin support for testing using pytest you can write unit test and
integration test for you fastapi application , and fastapi provides test client to
simulate request and responses for your endpoints.

### What are some best practices for developing and deploying fastapi applications?

Some best practices for developing and deploying fastapi application include using
Pydantic for data validation, implementing caching and rate limiting , sung logging and
monitoring for debugging and performance optimization, and following security best
practices

### How does fastapi handle scalability and performance?

Fastapi is designed for high performance and scalable application. It uses the
ASGI(asynchronous server gateway interface) standard to handle requests and responses,
allowing for highly performant and scalable application.
It uses asynchronous programming with Pythons asyncio library to handle multiple request
simultaneously , and its code generation feature optimized code for each endpoint.
Fastapi also has built in support for caching and rate limiting to improve performance.
