"""Model domain: petugas yang melayani penyewaan alat."""

from dataclasses import dataclass


@dataclass(frozen=True)
class JabatanPetugas:
    """Objek nilai jabatan petugas yang tidak dapat diubah."""

    nama: str

    def __post_init__(self) -> None:
        if not self.nama.strip():
            raise ValueError("jabatan tidak boleh kosong")

    def __str__(self) -> str:
        return self.nama


class Petugas:
    """Pengurus UPJA yang melayani proses penyewaan alat."""

    def __init__(
        self,
        id_petugas: str,
        nama: str,
        jabatan: str,
        telepon: str = "-",
    ) -> None:
        if not id_petugas.strip():
            raise ValueError("ID petugas tidak boleh kosong")

        self._id_petugas = id_petugas
        self._nama = nama
        self._jabatan = JabatanPetugas(jabatan)
        self._telepon = "-"
        self.telepon = telepon

    # ID petugas tetap setelah terdaftar, sehingga hanya boleh dibaca.
    @property
    def id_petugas(self) -> str:
        """ID petugas yang tidak dapat diubah melalui property."""
        return self._id_petugas

    # Nama petugas disediakan untuk dibaca tanpa setter perubahan.
    @property
    def nama(self) -> str:
        """Nama petugas."""
        return self._nama

    # Jabatan menggunakan objek nilai beku agar nilainya tidak dapat diubah.
    @property
    def jabatan(self) -> JabatanPetugas:
        """Jabatan petugas sebagai objek nilai yang beku."""
        return self._jabatan

    # Nomor telepon boleh berubah, tetapi setiap perubahan harus divalidasi.
    @property
    def telepon(self) -> str:
        """Nomor telepon petugas."""
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        """Memvalidasi nomor telepon sebelum disimpan."""
        if nilai == "-":
            self._telepon = "-"
            return

        bersih = nilai.replace("-", "").replace(" ", "")
        if not bersih.isdigit() or len(bersih) < 10:
            raise ValueError(
                f"nomor telepon tidak sah, diterima '{nilai}'"
            )

        self._telepon = nilai

    def identitas(self) -> str:
        """Mengembalikan identitas petugas."""
        return f"{self._nama} ({self._id_petugas}) — {self._jabatan}"

    def kontak(self) -> str:
        """Mengembalikan informasi kontak petugas."""
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"
