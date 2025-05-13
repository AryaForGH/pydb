-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 13 Bulan Mei 2025 pada 10.13
-- Versi server: 10.4.10-MariaDB
-- Versi PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `formcancel`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `pembatalan_pesanan`
--

CREATE TABLE `pembatalan_pesanan` (
  `id` int(11) NOT NULL,
  `nomor_pesanan` varchar(50) DEFAULT NULL,
  `nama_depan` varchar(50) DEFAULT NULL,
  `nama_belakang` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `kode_area` varchar(10) DEFAULT NULL,
  `nomor_telepon` varchar(20) DEFAULT NULL,
  `alamat_jalan` varchar(255) DEFAULT NULL,
  `alamat_jalan2` varchar(255) DEFAULT NULL,
  `kota` varchar(50) DEFAULT NULL,
  `provinsi` varchar(50) DEFAULT NULL,
  `kode_pos` varchar(10) DEFAULT NULL,
  `tindakan` varchar(50) DEFAULT NULL,
  `alasan` text DEFAULT NULL,
  `setuju_syarat` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `pembatalan_pesanan`
--

INSERT INTO `pembatalan_pesanan` (`id`, `nomor_pesanan`, `nama_depan`, `nama_belakang`, `email`, `kode_area`, `nomor_telepon`, `alamat_jalan`, `alamat_jalan2`, `kota`, `provinsi`, `kode_pos`, `tindakan`, `alasan`, `setuju_syarat`) VALUES
(1, 'PB0001SH', 'Andhika', 'Perkasa', 'andhika@example.com', '20000', '080000000000', 'Jalanin aja dulu', 'biar enak', 'Pagar Alam', 'Sumatra Selatan', '20000', 'batal', 'Duit nya untuk kebutuhan lain yang lebih penting', 1),
(2, 'PS002LN', 'Zaskia', 'Cahaya', 'zaskia@example.com', '900', '080101010101', 'Jalan baru', 'baru dibikin', 'Pagar Alam', 'Sumatra Selatan', '21210', 'batal', 'Gada uangnya ternyata', 1);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `pembatalan_pesanan`
--
ALTER TABLE `pembatalan_pesanan`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `pembatalan_pesanan`
--
ALTER TABLE `pembatalan_pesanan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
