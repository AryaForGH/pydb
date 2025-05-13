from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Koneksi ke database MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # kosongkan jika pakai XAMPP
    database="formcancel"
)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form

    cursor = db.cursor()
    sql = """
        INSERT INTO pembatalan_pesanan (
            nomor_pesanan, nama_depan, nama_belakang, email,
            kode_area, nomor_telepon, alamat_jalan, alamat_jalan2,
            kota, provinsi, kode_pos, tindakan, alasan, setuju_syarat
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        data.get("nomor_pesanan"),
        data.get("nama_depan"),
        data.get("nama_belakang"),
        data.get("email"),
        data.get("kode_area"),
        data.get("nomor_telepon"),
        data.get("alamat_jalan"),
        data.get("alamat_jalan2"),
        data.get("kota"),
        data.get("provinsi"),
        data.get("kode_pos"),
        data.get("tindakan"),
        data.get("alasan"),
        "setuju_syarat" in data
    )

    cursor.execute(sql, values)
    db.commit()
    cursor.close()

    return "<h3>Data berhasil disimpan!</h3><a href='/'>Kembali</a>"

if __name__ == "__main__":
    app.run(debug=True)
