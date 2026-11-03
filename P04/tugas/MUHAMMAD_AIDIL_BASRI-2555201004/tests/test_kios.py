
import pytest

from src.model.kios import Kios


def test_membuat_produk_valid() -> None:
    produk = Kios("BR001", "Beras Ramos", 15000, 20)

    assert produk.kode == "BR001"
    assert produk.nama == "Beras Ramos"
    assert produk.harga_modal == 15000
    assert produk.stok == 20


def test_harga_jual_dengan_margin_minimum() -> None:
    produk = Kios("BR002", "Gula", 20000, 10)

    assert produk.hitung_harga_jual() == 22000


def test_format_rupiah() -> None:
    assert Kios.format_rupiah(15000) == "Rp15.000"


def test_format_keterangan_produk() -> None:
    produk = Kios("BR003", "Minyak Goreng", 20000, 15)

    hasil = produk.keterangan()

    assert "BR003" in hasil
    assert "Minyak Goreng" in hasil
    assert "Rp22.000" in hasil
    assert "15" in hasil


def test_jumlah_produk_bertambah() -> None:
    sebelum = Kios.jumlah_produk()

    Kios("BR004", "Tepung", 12000, 8)

    sesudah = Kios.jumlah_produk()

    assert sesudah == sebelum + 1


def test_harga_wajar() -> None:
    assert Kios.harga_wajar(15000) is True


def test_harga_tidak_wajar() -> None:
    assert Kios.harga_wajar(0) is False


def test_menolak_kode_kosong() -> None:
    with pytest.raises(ValueError):
        Kios("", "Beras", 15000, 10)


def test_menolak_nama_kosong() -> None:
    with pytest.raises(ValueError):
        Kios("BR005", "", 15000, 10)


def test_menolak_harga_modal_nol() -> None:
    with pytest.raises(ValueError):
        Kios("BR006", "Beras", 0, 10)


def test_menolak_stok_negatif() -> None:
    with pytest.raises(ValueError):
        Kios("BR007", "Beras", 15000, -1)


def test_menolak_baris_csv_tidak_lengkap() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_csv("BR008;Beras;15000")


def test_menolak_harga_csv_bukan_angka() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_csv("BR009;Beras;mahal;10")


def test_menolak_stok_csv_bukan_angka() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_csv("BR010;Beras;15000;banyak")


def test_membuat_produk_dari_baris_csv() -> None:
    produk = Kios.dari_baris_csv("BR011;Beras Ramos;15000;20")

    assert produk.kode == "BR011"
    assert produk.nama == "Beras Ramos"
    assert produk.harga_modal == 15000
    assert produk.stok == 20
