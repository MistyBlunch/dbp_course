from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', data=[
    {
      "description" : "item1"
    },
    {
      "description" : "item2"
    },
    {
      "description" : "item3"
    }
  ])

if __name__ == '__main__':
    app.run(debug=True)