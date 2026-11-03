
"""Model domain: produk yang dijual di kios UMKM."""

from typing import Final


class Kios:
    """Mewakili satu produk yang dijual oleh kios."""

    MARGIN_MINIMUM: Final[int] = 10
    STOK_MINIMUM: Final[int] = 0
    PEMISAH_BARIS: Final[str] = ";"

    _jumlah_produk: int = 0

    def __init__(
        self,
        kode: str,
        nama: str,
        harga_modal: int,
        stok: int,
    ) -> None:
        if not kode.strip():
            raise ValueError("kode produk tidak boleh kosong")

        if not nama.strip():
            raise ValueError("nama produk tidak boleh kosong")

        if harga_modal <= 0:
            raise ValueError("harga modal harus lebih dari nol")

        if stok < self.STOK_MINIMUM:
            raise ValueError("stok tidak boleh negatif")

        self._kode = kode.strip()
        self._nama = nama.strip()
        self._harga_modal = harga_modal
        self._stok = stok

        Kios._jumlah_produk += 1

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def harga_modal(self) -> int:
        return self._harga_modal

    @property
    def stok(self) -> int:
        return self._stok

    @staticmethod
    def harga_wajar(nilai: int) -> bool:
        """Memeriksa apakah harga produk lebih dari nol."""
        return nilai > 0

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        """Mengubah angka menjadi format rupiah."""
        return f"Rp{nilai:,}".replace(",", ".")

    def hitung_harga_jual(self) -> int:
        """Menghitung harga jual berdasarkan margin minimum."""
        return (
            self._harga_modal
            * (100 + self.MARGIN_MINIMUM)
            // 100
        )

    def keterangan(self) -> str:
        """Menampilkan informasi produk dengan format rata."""
        return (
            f"{self._kode:<10} | "
            f"{self._nama:<20} | "
            f"{self.format_rupiah(self.hitung_harga_jual()):>15} | "
            f"{self._stok:>5}"
        )

    @classmethod
    def jumlah_produk(cls) -> int:
        """Mengembalikan jumlah produk yang berhasil dibuat."""
        return cls._jumlah_produk

    @classmethod
    def dari_baris_csv(cls, baris: str) -> "Kios":
        """Membuat produk dari satu baris data."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != 4:
            raise ValueError(
                f"baris harus berisi 4 bagian, diterima {len(bagian)}"
            )

        kode, nama, harga, stok = bagian

        if not harga.strip().isdigit():
            raise ValueError("harga modal harus berupa angka")

        if not stok.strip().isdigit():
            raise ValueError("stok harus berupa angka")

        return cls(
            kode.strip(),
            nama.strip(),
            int(harga),
            int(stok),
        )
