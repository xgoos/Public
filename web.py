#!/usr/bin/env python3
from flask import Flask
from livereload import Server
import functions

app = Flask(__name__)

@app.route("/")
# @functions.requires_auth
def index():
    return functions.render_template("index.jinja2",greatings="Ahoj svete")

if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.watch('*.py')  # Watch for changes in Python files
    server.watch('*.jinja2')  # Watch for changes in Jinja2 templates
    server.serve(port=5000, debug=True)
