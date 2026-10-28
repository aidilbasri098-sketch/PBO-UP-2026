
"""Pengujian untuk kelas Alamat."""

import dataclasses

import pytest

from src.model.alamat import Alamat


def test_alamat_lengkap() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    assert alamat.lengkap() == "Dusun Pulau Jambu, Desa Kuok, Kec. Kuok"


def test_alamat_singkat() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    assert alamat.singkat() == "Kuok, Kuok"


def test_desa_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Pulau Jambu", "   ", "Kuok")


def test_kecamatan_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Pulau Jambu", "Kuok", "   ")


def test_alamat_tidak_dapat_diubah() -> None:
    alamat = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(dataclasses.FrozenInstanceError):
        alamat.desa = "Salo"  # type: ignore[misc]
