from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Define routes to serve the HTML and CSS files
@app.route('/')
def index():
    return render_template('style.html')

@app.route('/style.css')
def css():
    return send_from_directory('.', 'style.css')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
