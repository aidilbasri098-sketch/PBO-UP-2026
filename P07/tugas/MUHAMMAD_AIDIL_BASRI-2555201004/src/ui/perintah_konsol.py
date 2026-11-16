
"""Interpreter perintah konsol untuk daftar harga alat pertanian."""

from typing import Final

from src.model.daftar_harga import DaftarHarga

BANTUAN: Final[str] = (
    "Perintah tersedia:\n"
    "  bantuan              Menampilkan bantuan\n"
    "  daftar <hari>        Menampilkan semua harga sewa\n"
    "  harga <kode> <hari>  Menampilkan harga satu alat\n"
    "  termurah <hari>      Menampilkan alat termurah"
)


class PerintahKonsol:
    """Memproses perintah pengguna menggunakan pattern matching."""

    def __init__(self, daftar: DaftarHarga) -> None:
        self._daftar = daftar

    def jalankan(self, perintah: str) -> str:
        """Memproses satu perintah dan mengembalikan hasilnya."""
        bagian = perintah.strip().lower().split()
        hasil = ""

        match bagian:
            case []:
                hasil = "Perintah kosong. Ketik 'bantuan'."

            case ["bantuan"] | ["?"]:
                hasil = BANTUAN

            case ["daftar", hari] if hari.isdigit():
                hasil = self._daftar.tabel(int(hari))

            case ["harga", kode, hari] if hari.isdigit():
                hasil = self._harga_satu_alat(kode.upper(), int(hari))

            case ["termurah", hari] if hari.isdigit():
                alat = self._daftar.termurah(int(hari))
                hasil = f"Termurah untuk {hari} hari: {alat.nama}"

            case [perintah_pertama, *_]:
                hasil = (
                    f"Perintah '{perintah_pertama}' tidak dikenal. "
                    "Ketik 'bantuan'."
                )

            case _:
                hasil = "Format perintah tidak valid. Ketik 'bantuan'."

        return hasil

    def _harga_satu_alat(self, kode: str, jumlah_hari: int) -> str:
        """Menampilkan harga alat berdasarkan kode."""
        hasil = self._daftar.harga_satu_alat(kode, jumlah_hari)

        if hasil is None:
            return f"Alat berkode {kode} tidak ada dalam daftar."

        nama, biaya = hasil
        rupiah = f"Rp{biaya:,}".replace(",", ".")
        return f"{nama}, {jumlah_hari} hari: {rupiah}"
