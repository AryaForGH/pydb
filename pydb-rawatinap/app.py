from flask import Flask, render_template, request, jsonify
from models import db, Pasien, Dokter, Kamar, PersetujuanRawatInap
from datetime import datetime
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/rumah_sakit'
db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def form():
    pasien_list = Pasien.query.all()
    dokter_list = Dokter.query.all()
    kamar_list = Kamar.query.all()
    return render_template('form.html', pasien_list=pasien_list, dokter_list=dokter_list, kamar_list=kamar_list)

@app.route('/get_pasien/<nomor>')
def get_pasien(nomor):
    pasien = Pasien.query.get(nomor)
    return jsonify({'nama': pasien.nama, 'alamat': pasien.alamat}) if pasien else {}

@app.route('/get_dokter/<kode>')
def get_dokter(kode):
    dokter = Dokter.query.get(kode)
    return jsonify({'nama_dokter': dokter.nama}) if dokter else {}

@app.route('/get_kamar/<kode>')
def get_kamar(kode):
    kamar = Kamar.query.get(kode)
    return jsonify({'jenis_kamar': kamar.jenis}) if kamar else {}

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    nomor_spri = "SPRI01" + uuid.uuid4().hex[:5].upper()
    spri = PersetujuanRawatInap(
        nomor_spri=nomor_spri,
        tanggal_spri=datetime.now(),
        nomor_registrasi=data['nomor_registrasi'],
        kode_dokter=data['kode_dokter'],
        kode_kamar=data['kode_kamar'],
        nama_penanggung_jawab=data['nama_penanggung_jawab'],
        alamat_penanggung_jawab=data['alamat_penanggung_jawab'],
        telpon_penanggung_jawab=data['telpon_penanggung_jawab'],
        pekerjaan_penanggung_jawab=data['pekerjaan_penanggung_jawab'],
        hubungan_dengan_pasien=data['hubungan_dengan_pasien']
    )
    db.session.add(spri)
    db.session.commit()
    return "Data berhasil disimpan"

if __name__ == '__main__':
    app.run(debug=True)
