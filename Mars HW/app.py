from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import pymongo
import scrape_mars
import pymongo
from flask_pymongo import PyMongo


app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
@app.route('/')
def index():
    mars= mongo.db.mars.find_one()
    return render_template('index.html', mars=mars)


@app.route('/scrape')
def scrape():
    mars = mongo.db.mars
    data = scrape_mars.scrape()
    mars.update(
        {},
        data,
        upsert=True
    )
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)