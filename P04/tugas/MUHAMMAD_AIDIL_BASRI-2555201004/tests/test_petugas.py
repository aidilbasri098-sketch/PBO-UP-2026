
"""Pengujian untuk kelas Petugas."""

from dataclasses import FrozenInstanceError

import pytest

from src.model.petugas import JabatanPetugas, Petugas


def test_identitas() -> None:
    petugas = Petugas("PT-01", "Andi", "Ketua")
    assert petugas.identitas() == "Andi (PT-01) — Ketua"


def test_kontak_dengan_telepon() -> None:
    petugas = Petugas("PT-01", "Andi", "Ketua", "08123456789")
    assert petugas.kontak() == "Andi dapat dihubungi di 08123456789"


def test_dua_objek_punya_data_sendiri() -> None:
    andi = Petugas("PT-01", "Andi", "Ketua")
    budi = Petugas("PT-02", "Budi", "Sekretaris")

    assert andi.identitas() != budi.identitas()


def test_id_petugas_baca_saja() -> None:
    petugas = Petugas("PT-01", "Andi", "Ketua")

    with pytest.raises(AttributeError):
        petugas.id_petugas = "PT-02"  # type: ignore[misc]


def test_id_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("", "Andi", "Ketua")


def test_jabatan_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("PT-01", "Andi", "   ")


def test_telepon_tidak_valid_ditolak_konstruktor() -> None:
    with pytest.raises(ValueError):
        Petugas("PT-01", "Andi", "Ketua", "abc")


def test_telepon_tidak_valid_ditolak_setter() -> None:
    petugas = Petugas("PT-01", "Andi", "Ketua")

    with pytest.raises(ValueError):
        petugas.telepon = "123"


def test_telepon_lama_tetap_jika_input_ditolak() -> None:
    petugas = Petugas("PT-01", "Andi", "Ketua", "08123456789")

    with pytest.raises(ValueError):
        petugas.telepon = "abc"

    assert petugas.telepon == "08123456789"


def test_jabatan_merupakan_objek_nilai_beku() -> None:
    petugas = Petugas("PT-01", "Andi", "Ketua")

    assert isinstance(petugas.jabatan, JabatanPetugas)

    with pytest.raises(FrozenInstanceError):
        petugas.jabatan.nama = "Sekretaris"  # type: ignore[misc]
