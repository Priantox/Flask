## **1.Flask Basics**

* Introduction to Flask and its features
* Installing Flask (`pip install flask`)
* Creating a simple “Hello World” app
* Flask app structure and project organization
* Running the Flask development server

---

## **2. Routing and URL Handling**

* `@app.route()` decorator
* Route variables and converters (`/<int:id>`, `<string:name>`)
* URL building with `url_for()`
* Handling query parameters
* Redirects and error handling (`abort`, custom 404 page)

---

## **3. Templates and Rendering**

* Introduction to **Jinja2** templates
* Template variables and expressions
* Control structures: loops and conditionals
* Template inheritance (`base.html`, `extends`, `block`)
* Including static files (CSS, JS, images)

---

## **4. HTTP Methods and Forms**

* GET vs POST requests
* Handling form data with `request.form`
* Query string parameters with `request.args`
* File uploads with `request.files`
* Form validation (basic and with  **WTForms** )

---

## **5. Static Files and Media**

* Serving static files
* Organizing CSS, JavaScript, and images
* Uploading and saving user files

---

## **6. Sessions and Cookies**

* Using `session` to store user data
* Configuring secret keys
* Setting and reading cookies

---

## **7. Flask Extensions**

* **Flask-SQLAlchemy** (ORM for databases)
* **Flask-Migrate** (database migrations)
* **Flask-WTF** (forms with validation)
* **Flask-Login** (user authentication)
* **Flask-Mail** (sending emails)
* **Flask-RESTful / Flask-RESTx** (building APIs)

---

## **8. Database Integration**

* Connecting Flask with databases (SQLite, MySQL, PostgreSQL)
* CRUD operations
* Using SQLAlchemy models
* Relationships: One-to-One, One-to-Many, Many-to-Many

---

## **9. Authentication and Authorization**

* User registration and login
* Password hashing (`werkzeug.security`)
* Session-based authentication
* Role-based access control

---

## **10. Error Handling**

* Custom error pages (404, 500)
* Exception handling
* Logging errors

---

## **11. RESTful API Development**

* Building API endpoints
* JSON input/output (`request.get_json()`, `jsonify()`)
* API versioning
* Token-based authentication (JWT)

---

## **12. Advanced Topics**

* Blueprint for modular applications
* Application factory pattern
* Contexts: application context, request context
* Middleware and request hooks (`before_request`, `after_request`)
* CORS handling
* Deploying Flask apps (Heroku, AWS, Docker)

---

## **13. Testing and Debugging**

* Flask testing basics (`FlaskClient`)
* Unit testing routes and views
* Debugging with Flask debugger
* Logging and error tracking
