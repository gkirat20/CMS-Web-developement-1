from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)  # Note: For production use a hashed password

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    contents = Content.query.all()
    return render_template('index.html', contents=contents)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.password == request.form['password']:
            login_user(user)
            return redirect(url_for('manage'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/content/<int:content_id>')
def content_detail(content_id):
    content = Content.query.get_or_404(content_id)
    return render_template('detail.html', content=content)

@app.route('/manage', methods=['GET', 'POST'])
@login_required
def manage():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        content = Content(title=title, body=body)
        db.session.add(content)
        db.session.commit()
        return redirect(url_for('index'))
    contents = Content.query.all()
    return render_template('manage.html', contents=contents)

@app.route('/edit/<int:content_id>', methods=['GET', 'POST'])
@login_required
def edit(content_id):
    content = Content.query.get_or_404(content_id)
    if request.method == 'POST':
        content.title = request.form['title']
        content.body = request.form['body']
        db.session.commit()
        return redirect(url_for('manage'))
    return render_template('manage.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)
