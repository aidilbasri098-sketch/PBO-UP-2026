"""Contoh menjalankan aplikasi SIPALA dari terminal."""

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa


def main() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kampar")
    penyewa = Penyewa("1406012509900001", "Budi Santoso", alamat)
    sewa = Sewa("SW-2026-001", penyewa)

    traktor = AlatTani("TR-01", "Traktor Roda Dua Kubota", 150_000)
    pompa = AlatTani("PA-01", "Pompa Air 3 Inci", 75_000)
    sewa.tambah_alat(traktor, 3)
    sewa.tambah_alat(pompa, 5)

    print(sewa.nota())


if __name__ == "__main__":
    main()
