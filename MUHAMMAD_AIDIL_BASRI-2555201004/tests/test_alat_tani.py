
"""Pengujian untuk kelas AlatTani."""

import pytest

from src.model.alat_tani import AlatTani


def test_biaya_sewa_tiga_hari() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_keterangan_alat() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.keterangan() == "[TR-01] Traktor — Rp150.000/hari"


def test_tarif_minus_ditolak_sejak_konstruktor() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", -5000)


def test_tarif_nol_ditolak_sejak_konstruktor() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 0)


def test_tarif_minus_ditolak_lewat_setter() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(ValueError):
        alat.tarif_harian = -5000
    assert alat.tarif_harian == 150000


def test_tarif_nol_ditolak_lewat_setter() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(ValueError):
        alat.tarif_harian = 0
    assert alat.tarif_harian == 150000


def test_kode_tidak_dapat_diubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.kode = "TR-99"  # type: ignore[misc]


def test_nama_tidak_dapat_diubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.nama = "Pompa"  # type: ignore[misc]


def test_dua_objek_memiliki_tarif_sendiri() -> None:
    traktor = AlatTani("TR-01", "Traktor", 150000)
    pompa = AlatTani("PA-01", "Pompa", 75000)
    assert traktor.biaya_sewa(1) != pompa.biaya_sewa(1)
