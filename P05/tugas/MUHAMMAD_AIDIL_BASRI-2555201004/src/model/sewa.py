"""Model domain: transaksi penyewaan alat pertanian."""

from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.baris_sewa import BarisSewa

class Sewa:
    """Transaksi sewa milik seorang penyewa."""

    BATAS_ALAT_PER_SEWA: int = 10

    def __init__(self, nomor: str, penyewa: Penyewa) -> None:
        if not nomor.strip():
            raise ValueError("nomor sewa tidak boleh kosong")

        self._nomor = nomor
        self._penyewa = penyewa
        self._baris: list[BarisSewa] = []

    @property
    def nomor(self) -> str:
        return self._nomor

    @property
    def penyewa(self) -> Penyewa:
        return self._penyewa

    @property
    def baris(self) -> tuple[BarisSewa, ...]:
        return tuple(self._baris)

    def tambah_alat(self, alat: AlatTani, jumlah_hari: int) -> None:
        if len(self._baris) >= self.BATAS_ALAT_PER_SEWA:
            raise ValueError("jumlah alat dalam satu sewa maksimal 10")

        for item in self._baris:
            if item.kode_alat == alat.kode:
                raise ValueError("alat tersebut sudah ada dalam transaksi")

        self._baris.append(BarisSewa(alat, jumlah_hari))

    def total(self) -> int:
        return sum(item.subtotal() for item in self._baris)