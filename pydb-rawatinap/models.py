from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pasien(db.Model):
    nomor_registrasi = db.Column(db.String, primary_key=True)
    nama = db.Column(db.String)
    alamat = db.Column(db.String)

class Dokter(db.Model):
    kode_dokter = db.Column(db.String, primary_key=True)
    nama = db.Column(db.String)

class Kamar(db.Model):
    kode_kamar = db.Column(db.String, primary_key=True)
    jenis = db.Column(db.String)

class PersetujuanRawatInap(db.Model):
    nomor_spri = db.Column(db.String, primary_key=True)
    tanggal_spri = db.Column(db.Date)
    nomor_registrasi = db.Column(db.String)
    kode_dokter = db.Column(db.String)
    kode_kamar = db.Column(db.String)
    nama_penanggung_jawab = db.Column(db.String)
    alamat_penanggung_jawab = db.Column(db.String)
    telpon_penanggung_jawab = db.Column(db.String)
    pekerjaan_penanggung_jawab = db.Column(db.String)
    hubungan_dengan_pasien = db.Column(db.String)
