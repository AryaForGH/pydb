# Import Library
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import os
from werkzeug.utils import secure_filename

# App name
app = Flask(__name__)

# Fungsi Upload == Akan di push ke folder uploads
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Koneksi Database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_barang'

# Inisialisasi MySQL
mysql = MySQL(app)

# Fungsi Halaman Utama
@app.route('/')
def index():
    # Logika pencarian
    keyword = request.args.get('search')
    # Jika ada keyword, maka cari barang
    cur = mysql.connection.cursor()
    if keyword:
        cur.execute("SELECT * FROM barang WHERE nama_barang LIKE %s", ('%' + keyword + '%',))
    else:
        cur.execute("SELECT * FROM barang")
    data = cur.fetchall()
    # Mengembalikan data ke halaman index.html
    return render_template('index.html', barang=data)

# Fungsi Halaman Tambah Barang
@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    # Jika ada request POST, maka simpan data barang
    if request.method == 'POST':
        nama = request.form['nama']
        harga = request.form['harga']
        detail = request.form['detail']
        stok = request.form['stok']
        file = request.files['gambar']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        cur = mysql.connection.cursor()
        # Simpan data barang ke database
        cur.execute("INSERT INTO barang (nama_barang, harga, detail, gambar, stok) VALUES (%s, %s, %s, %s, %s)",
                    (nama, harga, detail, filename, stok))
        mysql.connection.commit()
        return redirect(url_for('index'))
    return render_template('tambah.html')

# Fungsi Halaman Edit Barang
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        nama = request.form['nama']
        harga = request.form['harga']
        detail = request.form['detail']
        stok = request.form['stok']
        gambar = request.files['gambar']
        if gambar:
            filename = secure_filename(gambar.filename)
            gambar.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            cur.execute("UPDATE barang SET nama_barang=%s, harga=%s, detail=%s, gambar=%s, stok=%s WHERE id=%s",
                        (nama, harga, detail, filename, stok, id))
        else:
            cur.execute("UPDATE barang SET nama_barang=%s, harga=%s, detail=%s, stok=%s WHERE id=%s",
                        (nama, harga, detail, stok, id))
        mysql.connection.commit()
        return redirect(url_for('index'))

    cur.execute("SELECT * FROM barang WHERE id=%s", (id,))
    data = cur.fetchone()
    return render_template('edit.html', barang=data)

# Fungsi Halaman Hapus Barang
@app.route('/hapus/<int:id>')
def hapus(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM barang WHERE id=%s", (id,))
    mysql.connection.commit()
    return redirect(url_for('index'))

# Mulai Aplikasi
if __name__ == '__main__':
    app.run(debug=True)
