from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Correct the configuration keys
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Corrected the key to SQLALCHEMY_TRACK_MODIFICATIONS

# Initialize the database
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():  # Ensure the app context is pushed
        db.create_all()  # Create the database tables
    app.run(debug=True)  # Enable debug mode for easier troubleshooting
