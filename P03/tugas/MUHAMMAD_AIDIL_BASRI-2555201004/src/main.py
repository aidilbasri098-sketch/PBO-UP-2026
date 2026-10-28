
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

   
    print("\n--- Memeriksa tarif tanpa membuat objek ---")

    for calon in (5_000, 150_000, 6_000_000):
        status = "wajar" if AlatTani.tarif_wajar(calon) else "ditolak"
        print(f" {AlatTani.format_rupiah(calon):>14} → {status}")


if __name__ == "__main__":
    main()
