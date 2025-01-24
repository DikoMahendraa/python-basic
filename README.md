# Take it Notes

Python is a case-sensitive language, so be mindful of capitalization.  
Don't forget to enclose the text `welcome` inside quotation marks.

## Common Mistakes (I)

1. **Spelling Errors**

   ```python
   annual_income = 95000
   print(annual_icome)  # Error due to a typo
   ```

2. **Adding Spaces at the Beginning**  
   In Python, indentation has a specific meaning. Adding unnecessary spaces at the beginning will cause an error.  
   Example:

   ```python
         print("Hello")  # Error
   ```

3. **Quotation Marks Errors**  
   Beginners often forget to close strings with quotation marks. Example:

   ```python
   print("Hello)  # Error: Missing closing quotation mark
   ```

4. **Forgetting Commas in the `print()` Function**  
   Python interprets `"Age:" age` as a single item, causing an error:

   ```python
   print("Age:" age)  # Error
   ```

5. **Forgetting to Use `f` in an f-string**  
   Without `f`, variables inside curly braces are treated as plain text:
   ```python
   age = 25
   print("{age}")  # Output: {age}, not 25
   ```

---

## Learn How to:

1. Create variables.
2. Use comments.
3. Work with data types (`int`, `float`, `string`).
4. Create a function.
5. Create a class with inheritance.

---

## What's Next?

### 1. Web Frameworks

Learn a Python web framework to build your REST API. Popular options include:

- **Flask**: Lightweight and flexible, great for small to medium-sized projects.
- **FastAPI**: Modern, fast, and easy to use, with built-in support for async and data validation.
- **Django**: A full-featured framework with built-in ORM, admin panel, and more (ideal for larger projects).

**Recommendation**: Start with Flask or FastAPI for REST APIs.

### 2. HTTP Methods and Status Codes

- **HTTP Methods**:

  - `GET`: Retrieve data.
  - `POST`: Create new data.
  - `PUT/PATCH`: Update existing data.
  - `DELETE`: Remove data.

- **Common Status Codes**:
  - `200 OK`: Successful request.
  - `201 Created`: Resource created successfully.
  - `400 Bad Request`: Invalid input.
  - `404 Not Found`: Resource not found.
  - `500 Internal Server Error`: Server-side error.

### 3. Routing

Define routes (endpoints) in your chosen framework.

### 4. Request and Response Handling

Learn to handle incoming requests (e.g., JSON data, query parameters) and send responses (e.g., JSON).

### 5. Data Validation

Validate incoming data to meet your API's requirements.

**Libraries for validation**:

- **Pydantic** (FastAPI).
- **Marshmallow** (Flask).

### 6. Database Integration

Connect your API to a database (e.g., SQLite, PostgreSQL, MySQL).

**ORM Tools**:

- **SQLAlchemy**: Works with Flask and FastAPI.
- **Django ORM**: Built into Django.

### 7. Error Handling

Handle errors gracefully (e.g., invalid input, missing resources).

### 8. Authentication and Authorization

Secure your API with methods like:

- API Keys.
- JWT (JSON Web Tokens).
- OAuth2.

### 9. API Documentation

Document your API for others to understand how to use it.

**Tools for Documentation**:

- Swagger/OpenAPI (FastAPI).
- Flask-Swagger (Flask).

### 10. Environment Variables

Manage configuration (e.g., database credentials, API keys) using environment variables.

**Libraries**:

- `python-decouple`.
- `dotenv`.

### 11. Deployment

Deploy your API to a production environment.

**Platforms**:

- Heroku.
- AWS.
- Google Cloud.
- Docker (containerization).

### 12. Versioning

Implement versioning to manage changes over time.

### 13. Logging

Add logging to track errors and monitor activity.

---

## Summary of What to Learn

- Web frameworks: Flask, FastAPI, Django.
- HTTP methods and status codes.
- Routing and request/response handling.
- Data validation: Pydantic, Marshmallow.
- Database integration: SQLAlchemy, Django ORM.
- Error handling.
- Authentication and authorization: JWT, OAuth2.
- Testing: `pytest`, `unittest`.
- API documentation: Swagger/OpenAPI.
- Environment variables: `python-decouple`, `dotenv`.
- Deployment: Heroku, AWS, Docker.
- Versioning.
- Logging.
