# Take it Notes:

Python is a case-sensitive language, so be mindful of capitalization.
Don't forget to enclose the text welcome inside quotation marks.

## Common Mistakes (I)

1. Spelling Error
   annual_income = 95000

error because of a spelling mistake

print(annual_icome)

2.  Adding Spaces at the Beginning
    In Python, indentation has a specific meaning. So, if we add unnecessary spaces at the beginning, we will get an error. For example,

          print("Hello")  # Error

3.  Error because of Quotation Marks
    We have seen many beginners make this mistake. They usually forget to close the string with quotation marks. For example,

4.  Forgetting Commas in the print() Function
    Here, Python interprets "Age:" age as a single item. Since it's neither a string nor a variable, we get an error.

5.  Forgetting to use f in a f-string
    If you forget to include f before the quotation marks, the string is treated as a normal string. As a result, {age} is interpreted as plain text instead of being evaluated as a variable

Learn How to:

1. create variables
2. comments
3. data types int, float, string
4. create a function
5. create a class with inheritance

## What's next ?

1. Web Frameworks
   Learn a Python web framework to build your REST API. The most popular ones are:

Flask: Lightweight and flexible, great for small to medium-sized projects.

FastAPI: Modern, fast, and easy to use, with built-in support for async and data validation.

Django: A full-featured framework with built-in ORM, admin panel, and more (great for larger projects).

Recommendation: Start with Flask or FastAPI for REST APIs.

2. HTTP Methods and Status Codes
   Understand the HTTP methods used in REST APIs:

GET: Retrieve data.

POST: Create new data.

PUT/PATCH: Update existing data.

DELETE: Remove data.

Learn common HTTP status codes:

200 OK: Successful request.

201 Created: Resource created successfully.

400 Bad Request: Invalid input.

404 Not Found: Resource not found.

500 Internal Server Error: Server-side error.

3. Routing
   Learn how to define routes (endpoints) in your chosen framework.

4. Request and Response Handling
   Learn how to handle incoming requests (e.g., JSON data, query parameters) and send responses (e.g., JSON).

5. Data Validation
   Validate incoming data to ensure it meets your API's requirements.

Libraries for validation:

- Pydantic (used in FastAPI).
- Marshmallow (used in Flask).

6. Database Integration
   Learn how to connect your API to a database (e.g., SQLite, PostgreSQL, MySQL).

Use an ORM (Object-Relational Mapping) tool to interact with the database:

SQLAlchemy: Works with Flask and FastAPI.

Django ORM: Built into Django.

7. Error Handling
   Handle errors gracefully in your API (e.g., invalid input, missing resources).

8. Authentication and Authorization
   Secure your API by implementing authentication and authorization.

Common methods:

- API Keys.
- JWT (JSON Web Tokens).
- OAuth2.

10. API Documentation
    Document your API so others can understand how to use it.

Tools for documentation:

- Swagger/OpenAPI: Automatically generates interactive docs (used in FastAPI).
- Flask-Swagger: For Flask.

11. Environment Variables
    Use environment variables to manage configuration (e.g., database credentials, API keys).

Libraries:

- python-decouple.
- dotenv.

12. Deployment
    Learn how to deploy your API to a production environment.

Popular deployment platforms:

- Heroku.
- AWS.
- Google Cloud.
- Docker (for containerization).

13. Versioning
    Implement versioning in your API to manage changes over time.

14. Logging
    Add logging to your API to track errors and monitor activity.

## Summary of What to Learn:

- Web frameworks (Flask, FastAPI, Django).
- HTTP methods and status codes.
- Routing and request/response handling.
- Data validation (Pydantic, Marshmallow).
- Database integration (SQLAlchemy, Django ORM).
- Error handling.
- Authentication and authorization (JWT, OAuth2).
- Testing (pytest, unittest).
- API documentation (Swagger/OpenAPI).
- Environment variables (python-decouple, dotenv).
- Deployment (Heroku, AWS, Docker).
- Versioning.
- Logging.
