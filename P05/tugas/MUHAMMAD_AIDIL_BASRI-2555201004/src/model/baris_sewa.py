
"""Model domain: satu baris alat dalam transaksi penyewaan."""

from src.model.alat_tani import AlatTani


class BarisSewa:
    """Menyimpan alat dan tarif saat transaksi dibuat."""

    def __init__(self, alat: AlatTani, jumlah_hari: int) -> None:
        if jumlah_hari <= 0:
            raise ValueError("jumlah hari harus lebih dari 0")

        self._alat = alat
        self._jumlah_hari = jumlah_hari

        # Menyimpan salinan data untuk menjaga riwayat transaksi.
        self._kode_alat = alat.kode
        self._nama_alat = alat.nama
        self._tarif_saat_sewa = alat.tarif_harian

    @property
    def alat(self) -> AlatTani:
        """Mengembalikan referensi alat yang disewa."""
        return self._alat

    @property
    def jumlah_hari(self) -> int:
        """Mengembalikan lama penyewaan."""
        return self._jumlah_hari

    @property
    def kode_alat(self) -> str:
        """Kode alat saat transaksi dibuat."""
        return self._kode_alat

    @property
    def nama_alat(self) -> str:
        """Nama alat saat transaksi dibuat."""
        return self._nama_alat

    @property
    def tarif_saat_sewa(self) -> int:
        """Tarif harian saat transaksi dibuat."""
        return self._tarif_saat_sewa

    def subtotal(self) -> int:
        """Menghitung subtotal berdasarkan tarif saat transaksi."""
        return self._tarif_saat_sewa * self._jumlah_hari
