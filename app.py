from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Todo app class model representing the database table
class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    complete = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<TodoItem {self.id}>'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Creating a new TodoItem object and adding it to the database
        content = request.form['content']
        if content.strip() != '':
            new_item = TodoItem(content=content)
            db.session.add(new_item)
            db.session.commit()
            return redirect('/')
    
    # GET method logic
    items = TodoItem.query.all()
    return render_template('index.html', items=items)

@app.route('/complete/<int:item_id>')
def complete(item_id):
    item = TodoItem.query.get_or_404(item_id)
    item.complete = True
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:item_id>')
def delete(item_id):
    item = TodoItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
