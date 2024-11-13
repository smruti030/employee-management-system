from flask import Flask
from models import db, Employee
from routes import main
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Initialize the database with the Flask app
#db.init_app(app)
@app.route('/')
def home():
    return "Welcome to the Employee Management System"

# Register the routes blueprint
app.register_blueprint(main)

# Use a flag to ensure tables are created only once
tables_created = False

@app.before_request
def create_tables():
    global tables_created
    if not tables_created:
        with app.app_context():
            db.create_all()
        tables_created = True



# Create the database tables before the first request
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
