from flask import Flask, render_template, request, redirect, url_for, session
from flask_cors import CORS
from models import db, User
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
CORS(app)  # 如果前端跨域需要

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_user.html', user=user)

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(email=email).first():
            error = 'Email already registered'
        else:
            
            new_user = User(name=name, email=email,  password=password)
            db.session.add(new_user)
            db.session.commit()
            
            return redirect(url_for('login'))
    return render_template('register.html', error=error)


app.secret_key = 'your_secret_key'  # 用于session

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and password == user.password:
            # 密码和数据库中该用户的密码一致，允许登录
            session['user_id'] = user.id
            session['user_name'] = user.name
            return redirect(url_for('index'))
        else:
            error = 'Invalid email or password'

    return render_template('login.html', error=error)



if __name__ == '__main__':
    with app.app_context():
        db.drop_all() 
        db.create_all()
    app.run(debug=True)
