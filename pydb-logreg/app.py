from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret123'

def init_db():
    conn = sqlite3.connect('logreg.db')
    conn.execute("""CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        firstname TEXT,
                        lastname TEXT,
                        email TEXT UNIQUE,
                        password TEXT,
                        company TEXT,
                        team_size TEXT)""")
    conn.close()

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('logreg.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = cur.fetchone()
        conn.close()
        if user:
            session['user'] = email
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid login')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = (
            request.form['firstname'],
            request.form['lastname'],
            request.form['email'],
            request.form['password'],
            request.form['company'],
            request.form['team_size']
        )
        try:
            conn = sqlite3.connect('logreg.db')
            conn.execute("INSERT INTO users (firstname, lastname, email, password, company, team_size) VALUES (?, ?, ?, ?, ?, ?)", data)
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except:
            return render_template('register.html', error='Email already used')
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect('logreg.db')
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return render_template('dashboard.html', users=users)

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit(user_id):
    conn = sqlite3.connect('logreg.db')
    if request.method == 'POST':
        data = (
            request.form['firstname'],
            request.form['lastname'],
            request.form['email'],
            request.form['company'],
            request.form['team_size'],
            user_id
        )
        conn.execute("UPDATE users SET firstname=?, lastname=?, email=?, company=?, team_size=? WHERE id=?", data)
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    user = conn.execute("SELECT * FROM users WHERE id=?", (user_id,)).fetchone()
    conn.close()
    return render_template('register.html', user=user)

@app.route('/delete/<int:user_id>')
def delete(user_id):
    conn = sqlite3.connect('logreg.db')
    conn.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
