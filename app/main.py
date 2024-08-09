from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Set up the database URI for SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///birthyears.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the database model for storing birth years
class BirthYear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year_of_birth = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<BirthYear {self.year_of_birth}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    age = None
    if request.method == 'POST':
        year_of_birth = int(request.form['year_of_birth'])
        current_year = datetime.now().year
        age = current_year - year_of_birth

        # Save the birth year to the database
        new_entry = BirthYear(year_of_birth=year_of_birth)
        db.session.add(new_entry)
        db.session.commit()

    return render_template('index.html', age=age)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
