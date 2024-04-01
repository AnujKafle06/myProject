from database import db
from flask import Flask, render_template
from flask_migrate import migrate
from flask_login import LoginManager




app = Flask(__name__)

dbName = "./database.db"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbName
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def create_db():
    with app.app_context():
        db.create_all()


@app.route("/")
def Basefile():
   return render_template("index.html")


if __name__ == "__main__":
 from model import User
 
 create_db()
 app.run(debug=True , host='0.0.0.0' ,  port=600)






