"""
TAP 21

Create a simple Flask web page.

- it should contain a home and and an about page
- optional: use a template as a base for the pages
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()