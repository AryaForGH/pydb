from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", 
    database="perpustakaan"
)

@app.route("/", methods=["GET"])
def index():
    keyword = request.args.get("keyword", "")
    cursor = db.cursor(dictionary=True)
    if keyword:
        query = "SELECT * FROM buku WHERE judul LIKE %s OR pengarang LIKE %s"
        cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
    else:
        cursor.execute("SELECT * FROM buku")
    buku = cursor.fetchall()
    return render_template("index.html", buku=buku, keyword=keyword)

@app.route("/tambah", methods=["GET", "POST"])
def tambah():
    if request.method == "POST":
        data = (
            request.form["judul"],
            request.form["pengarang"],
            request.form["penerbit"],
            request.form["tahun_terbit"],
            request.form["kategori"]
        )
        cursor = db.cursor()
        cursor.execute("INSERT INTO buku (judul, pengarang, penerbit, tahun_terbit, kategori) VALUES (%s, %s, %s, %s, %s)", data)
        db.commit()
        return redirect(url_for("index"))
    return render_template("tambah.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    cursor = db.cursor(dictionary=True)
    if request.method == "POST":
        data = (
            request.form["judul"],
            request.form["pengarang"],
            request.form["penerbit"],
            request.form["tahun_terbit"],
            request.form["kategori"],
            id
        )
        cursor.execute("UPDATE buku SET judul=%s, pengarang=%s, penerbit=%s, tahun_terbit=%s, kategori=%s WHERE id=%s", data)
        db.commit()
        return redirect(url_for("index"))
    cursor.execute("SELECT * FROM buku WHERE id=%s", (id,))
    buku = cursor.fetchone()
    return render_template("edit.html", buku=buku)

@app.route("/hapus/<int:id>")
def hapus(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM buku WHERE id=%s", (id,))
    db.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
