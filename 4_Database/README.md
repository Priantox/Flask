<h2>🗄️ Create Database in Flask (SQLAlchemy)</h2>

<h3>📌 Open Python Shell</h3>
<ul>
  <li><code>python</code></li>
</ul>

<h3>📌 Import App & Database</h3>
<ul>
  <li><code>from app import app, db</code></li>
</ul>

<h3>📌 Create All Tables</h3>
<ul>
  <li>
    <pre><code>with app.app_context():
    db.create_all()</code></pre>
  </li>
</ul>

<h3>📝 What This Does</h3>
<ul>
  <li>Loads your Flask app inside the Python shell</li>
  <li>Enters the Flask application context</li>
  <li>Creates all database tables (User, Post, etc.)</li>
  <li>Generates <strong>site.db</strong> automatically</li>
</ul>

<h3>✅ Done!</h3>
<ul>
  <li>Your SQLite database is now created successfully.</li>
</ul>
