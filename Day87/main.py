from flask import Flask, request, redirect, render_template_string
from replit import db

app = Flask(__name__)

# Initialize the database
if 'logged_in' not in db:
    db['logged_in'] = False
if 'posts' not in db:
    db['posts'] = []

# HTML template for the blog page
blog_template = """
<!doctype html>
<html>
  <body>
    {% if logged_in %}
      <h1>Welcome to Your Blog</h1>
      <h2>Existing Posts:</h2>
      <ul>
        {% for post in posts %}
          <li>{{ post }}</li>
        {% endfor %}
      </ul>
      <h2>Add a New Post:</h2>
      <form method="POST" action="/add_post">
        <textarea name="post_content" rows="4" cols="50"></textarea>
        <input type="submit" value="Submit">
      </form>
      <form method="POST" action="/logout">
        <input type="submit" value="Logout">
      </form>
      <form method="GET" action="/edit">
        <input type="submit" value="Edit">
      </form>
    {% else %}
      <h1>Blog Entries (Most Recent First):</h1>
      <ul>
        {% for post in posts %}
          <li>{{ post }}</li>
        {% endfor %}
      </ul>
      <form method="POST" action="/login">
        <input type="submit" value="Login">
      </form>
    {% endif %}
  </body>
</html>
"""

@app.route('/')
def index():
    logged_in = db['logged_in']
    posts = db['posts']
    return render_template_string(blog_template, logged_in=logged_in, posts=posts)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    # Check if the username is correct (you can replace 'your_username' with your actual username)
    if username == 'your_username':
        db['logged_in'] = True
    return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():
    db['logged_in'] = False
    return redirect('/')

@app.route('/add_post', methods=['POST'])
def add_post():
    if not db['logged_in']:
        return redirect('/')

    post_content = request.form['post_content']
    posts = db['posts']
    posts.insert(0, post_content)
    db['posts'] = posts[:10]  # Limit the number of stored posts to the latest 10
    return redirect('/')

@app.route('/edit', methods=['GET'])
def edit():
    logged_in = db['logged_in']
    # Check if the user is logged in (you can replace 'your_username' with your actual username)
    if not logged_in or db.get('username') != 'your_username':
        return redirect('/')
    return "Editing page for user 'your_username'"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
