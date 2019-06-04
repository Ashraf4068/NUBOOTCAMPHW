# import necessary libraries
from flask import Flask, render_template
import pymongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)



# create mongo connection
client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_data_entries

@app.route("/")
def home():
    mars_data = collection.find_one()
    return  render_template('index.html', mars_data=mars_data)

@app.route("/scrape")
def scrape():
    db.collection.remove({})
    mars_data= scrape_mars.scrape()
    db.collection.insert_one(mars_data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)