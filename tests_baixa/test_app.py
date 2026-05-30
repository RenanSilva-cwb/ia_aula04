import pytest # type: ignore
from src_alta.app import calcular_rentabilidade, calcular_preco_venda

def test_rentabilidade_50_porcento():
    assert calcular_rentabilidade(100, 150) == 50

def test_rentabilidade_100_porcento():
    assert calcular_rentabilidade(100, 200) == 100

def test_markup_50_porcento():
    assert calcular_preco_venda(100, 50) == 150

def test_markup_100_porcento():
    assert calcular_preco_venda(100, 100) == 200