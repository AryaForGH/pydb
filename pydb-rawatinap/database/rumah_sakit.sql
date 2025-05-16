-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 14 Bulan Mei 2025 pada 12.36
-- Versi server: 10.1.38-MariaDB
-- Versi PHP: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rumah_sakit`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `dokter`
--

CREATE TABLE `dokter` (
  `kode_dokter` varchar(20) NOT NULL,
  `nama` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `dokter`
--

INSERT INTO `dokter` (`kode_dokter`, `nama`) VALUES
('D001', 'dr. Michael'),
('D002', 'dr. Jesselyn');

-- --------------------------------------------------------

--
-- Struktur dari tabel `kamar`
--

CREATE TABLE `kamar` (
  `kode_kamar` varchar(20) NOT NULL,
  `jenis` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `kamar`
--

INSERT INTO `kamar` (`kode_kamar`, `jenis`) VALUES
('K001', 'VIP 1'),
('K002', 'VIP 2'),
('K003', 'Ekonomi 1');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pasien`
--

CREATE TABLE `pasien` (
  `nomor_registrasi` varchar(20) NOT NULL,
  `nama` varchar(100) DEFAULT NULL,
  `alamat` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `pasien`
--

INSERT INTO `pasien` (`nomor_registrasi`, `nama`, `alamat`) VALUES
('RSI011', 'Nopal', 'Pagar Alam');

-- --------------------------------------------------------

--
-- Struktur dari tabel `persetujuan_rawat_inap`
--

CREATE TABLE `persetujuan_rawat_inap` (
  `nomor_spri` varchar(20) NOT NULL,
  `tanggal_spri` date DEFAULT NULL,
  `nomor_registrasi` varchar(20) DEFAULT NULL,
  `kode_dokter` varchar(20) DEFAULT NULL,
  `kode_kamar` varchar(20) DEFAULT NULL,
  `nama_penanggung_jawab` varchar(100) DEFAULT NULL,
  `alamat_penanggung_jawab` varchar(200) DEFAULT NULL,
  `telpon_penanggung_jawab` varchar(20) DEFAULT NULL,
  `pekerjaan_penanggung_jawab` varchar(100) DEFAULT NULL,
  `hubungan_dengan_pasien` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `persetujuan_rawat_inap`
--

INSERT INTO `persetujuan_rawat_inap` (`nomor_spri`, `tanggal_spri`, `nomor_registrasi`, `kode_dokter`, `kode_kamar`, `nama_penanggung_jawab`, `alamat_penanggung_jawab`, `telpon_penanggung_jawab`, `pekerjaan_penanggung_jawab`, `hubungan_dengan_pasien`) VALUES
('SPRI01D3591', '2025-05-14', 'RSI011', 'D002', 'K001', 'Sasmita', 'Pagar Alam', '0888', 'Dosen', 'Stepmom');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `dokter`
--
ALTER TABLE `dokter`
  ADD PRIMARY KEY (`kode_dokter`);

--
-- Indeks untuk tabel `kamar`
--
ALTER TABLE `kamar`
  ADD PRIMARY KEY (`kode_kamar`);

--
-- Indeks untuk tabel `pasien`
--
ALTER TABLE `pasien`
  ADD PRIMARY KEY (`nomor_registrasi`);

--
-- Indeks untuk tabel `persetujuan_rawat_inap`
--
ALTER TABLE `persetujuan_rawat_inap`
  ADD PRIMARY KEY (`nomor_spri`),
  ADD KEY `nomor_registrasi` (`nomor_registrasi`),
  ADD KEY `kode_dokter` (`kode_dokter`),
  ADD KEY `kode_kamar` (`kode_kamar`);

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `persetujuan_rawat_inap`
--
ALTER TABLE `persetujuan_rawat_inap`
  ADD CONSTRAINT `persetujuan_rawat_inap_ibfk_1` FOREIGN KEY (`nomor_registrasi`) REFERENCES `pasien` (`nomor_registrasi`),
  ADD CONSTRAINT `persetujuan_rawat_inap_ibfk_2` FOREIGN KEY (`kode_dokter`) REFERENCES `dokter` (`kode_dokter`),
  ADD CONSTRAINT `persetujuan_rawat_inap_ibfk_3` FOREIGN KEY (`kode_kamar`) REFERENCES `kamar` (`kode_kamar`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
