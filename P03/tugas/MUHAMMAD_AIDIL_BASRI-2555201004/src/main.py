
"""Titik masuk program. Satu-satunya berkas yang boleh mencetak."""

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def main() -> None:
    alamat_budi = Alamat("Pulau Jambu", "Kuok", "Kuok")
    alamat_siti = Alamat("Salo", "Salo", "Salo")

    budi = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        alamat_budi,
        "0812-3456-7890",
    )
    siti = Penyewa(
        "1406014403950002",
        "Siti Aminah",
        alamat_siti,
    )

    traktor = AlatTani("TR-01", "Traktor Roda Dua Kubota", 150000)

    print(budi.identitas())
    print(budi.alamat.lengkap())
    print(budi.kontak())
    print(siti.kontak())
    print(traktor.keterangan())

    print("\n--- Percobaan menembus penjagaan ---")
    for tarif in (0, -5000):
        try:
            traktor.tarif_harian = tarif
        except ValueError as galat:
            print(f"Ditolak (tarif {'nol' if tarif == 0 else 'minus'}): {galat}")

    print(f"Tarif tetap utuh: {traktor.keterangan()}")


if __name__ == "__main__":
    main()
