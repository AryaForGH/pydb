from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Koneksi database
db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="mahasiswa_db",
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/')
def index():
    keyword = request.args.get('keyword')
    cursor = db.cursor()
    if keyword:
        cursor.execute("SELECT * FROM mahasiswa WHERE nama LIKE %s", ('%' + keyword + '%',))
    else:
        cursor.execute("SELECT * FROM mahasiswa")
    mahasiswa = cursor.fetchall()
    return render_template('index.html', mahasiswa=mahasiswa)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        nama = request.form['nama']
        nim = request.form['nim']
        jurusan = request.form['jurusan']
        
        cursor = db.cursor()
        cursor.execute("INSERT INTO mahasiswa (nama, nim, jurusan) VALUES (%s, %s, %s)", (nama, nim, jurusan))
        db.commit()
        return redirect(url_for('index'))

    return render_template('tambah.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cursor = db.cursor()
    if request.method == 'POST':
        nama = request.form['nama']
        nim = request.form['nim']
        jurusan = request.form['jurusan']
        cursor.execute("UPDATE mahasiswa SET nama=%s, nim=%s, jurusan=%s WHERE id=%s", (nama, nim, jurusan, id))
        db.commit()
        return redirect(url_for('index'))
    
    cursor.execute("SELECT * FROM mahasiswa WHERE id=%s", (id,))
    mhs = cursor.fetchone()
    return render_template('edit.html', mhs=mhs)

@app.route('/hapus/<int:id>')
def hapus(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM mahasiswa WHERE id=%s", (id,))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
