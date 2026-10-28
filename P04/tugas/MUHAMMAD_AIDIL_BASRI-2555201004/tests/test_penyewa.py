
"""Pengujian untuk kelas Penyewa."""

import dataclasses

import pytest

from src.model.alamat import Alamat
from src.model.penyewa import Penyewa


def buat_penyewa() -> Penyewa:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    return Penyewa(
        "1406012509900001",
        "Budi Santoso",
        alamat,
        "0812-3456-7890",
    )


def test_identitas_penyewa() -> None:
    penyewa = buat_penyewa()
    assert "Budi Santoso" in penyewa.identitas()
    assert "Kuok" in penyewa.identitas()


def test_kontak_penyewa() -> None:
    penyewa = buat_penyewa()
    assert "0812-3456-7890" in penyewa.kontak()


def test_telepon_default() -> None:
    penyewa = Penyewa(
        "1406014403950002",
        "Siti Aminah",
        Alamat("Salo", "Salo", "Salo"),
    )
    assert "belum mencantumkan" in penyewa.kontak()


def test_nik_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        Penyewa("123", "Budi", Alamat("Dusun", "Kuok", "Kuok"))


def test_nik_tidak_dapat_diubah() -> None:
    penyewa = buat_penyewa()
    with pytest.raises(AttributeError):
        penyewa.nik = "1406012509900002"  # type: ignore[misc]


def test_telepon_tidak_valid_ditolak() -> None:
    penyewa = buat_penyewa()
    with pytest.raises(ValueError):
        penyewa.telepon = "abc"


def test_alamat_tidak_dapat_diubah() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(dataclasses.FrozenInstanceError):
        alamat.desa = "Salo"  # type: ignore[misc]
