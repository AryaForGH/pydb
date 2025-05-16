from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Koneksi ke database MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",       # Ganti jika bukan localhost
        user="root",            # Sesuaikan username
        password="",            # Kosongkan jika tanpa password
        database="karyawan" # Ganti dengan nama database Anda
    )

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        data = (
            request.form['nik'],
            request.form['nama'],
            request.form['jenis_kelamin'],
            request.form['jabatan'],
            request.form['departemen'],
            request.form['tempat_lahir'],
            request.form['tanggal_lahir'],
            request.form['golongan_darah'],
            request.form['agama'],
            request.form['status_pernikahan'],
            request.form['no_telepon']
        )
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO karyawan (
                nik, nama, jenis_kelamin, jabatan, departemen,
                tempat_lahir, tanggal_lahir, golongan_darah,
                agama, status_pernikahan, no_telepon
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', data)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/insert')

    return render_template('insert.html')

@app.route('/')
def home():
    return redirect('/insert')


if __name__ == '__main__':
    app.run(debug=True)
