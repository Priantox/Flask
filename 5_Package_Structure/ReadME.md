myproject/
│
├── flaskblog/
│   ├── (____init____).py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── static/
│   └── templates/
│
├── venv/
├── config.py
├── requirements.txt
└── run.py

### 🔹 `__init__.py`

- Acts as the **application factory**.
- Creates the Flask app instance.
- Initializes extensions such as the database.
- Registers blueprints and configurations.

### 🔹 `routes.py`

- Defines all **application routes (URLs)**.
- Contains view functions that return HTML templates or responses.

### 🔹 `models.py`

- Holds the **database models** using SQLAlchemy.
- Example entities include:
  - `User`
  - `Post`

### 🔹 `forms.py`

- Contains **Flask-WTF form classes**.
- Handles form validation and user input.

---

## 🎨 **static/**

Stores **static files** that do not change frequently:

- CSS stylesheets
- JavaScript scripts
- Images
- Framework assets (e.g., Bootstrap)

Browsers load these directly.

---

## 🖼️ **templates/**

Contains all **HTML (Jinja2) templates**, such as:

- `home.html`
- `login.html`
- `dashboard.html`

Templates can use dynamic placeholders like `{{ form.username }}`.

---

## ⚙️ `config.py`

Application configuration file.Includes:

- `SECRET_KEY`
- Database URI
- Debug settings
- Any custom configuration variables

---

## 🚀 `run.py`

Entry point of the application.
Used to start the development server:
