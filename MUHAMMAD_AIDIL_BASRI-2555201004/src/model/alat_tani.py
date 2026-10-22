
"""Model domain: alat yang disewakan UPJA."""


class AlatTani:
    """Satu unit alat pertanian beserta tarif hariannya."""

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        self._kode = kode
        self._nama = nama
        self._tarif_harian = 0
        self.tarif_harian = tarif_harian

    @property
    def kode(self) -> str:
        """Kode alat. Tidak dapat diubah setelah alat dibuat."""
        return self._kode

    @property
    def nama(self) -> str:
        """Nama alat. Tidak dapat diubah setelah alat dibuat."""
        return self._nama

    @property
    def tarif_harian(self) -> int:
        """Tarif sewa harian alat."""
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        """Menolak tarif yang tidak lebih besar dari nol."""
        if nilai <= 0:
            raise ValueError(
                f"tarif harus lebih dari nol, diterima {nilai}"
            )
        self._tarif_harian = nilai

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa untuk sejumlah hari tertentu."""
        return self._tarif_harian * jumlah_hari

    def keterangan(self) -> str:
        """Mengembalikan baris keterangan alat untuk daftar sewa."""
        rupiah = f"{self._tarif_harian:,}".replace(",", ".")
        return f"[{self._kode}] {self._nama} — Rp{rupiah}/hari"
