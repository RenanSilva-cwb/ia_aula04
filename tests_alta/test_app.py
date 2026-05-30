import pytest # type: ignore
from src_alta.app import calcular_rentabilidade, calcular_preco_venda

def test_rentabilidade_50_porcento():
    assert calcular_rentabilidade(100, 150) == 50

def test_rentabilidade_100_porcento():
    assert calcular_rentabilidade(100, 200) == 100

def test_custo_zero():
    with pytest.raises(ValueError):
        calcular_rentabilidade(0, 100)

def test_markup_50_porcento():
    assert calcular_preco_venda(100, 50) == 150

def test_markup_100_porcento():
    assert calcular_preco_venda(100, 100) == 200

def test_markup_zero():
    assert calcular_preco_venda(100, 0) == 100

def test_custo_decimal():
    assert calcular_preco_venda(99.90, 20) == 119.88

def test_valor_alto():
    assert calcular_preco_venda(1000, 30) == 1300

def test_custo_zero():
    try:
        calcular_preco_venda(0, 50)
        assert False
    except ValueError:
        assert True

def test_custo_negativo():
    try:
        calcular_preco_venda(-100, 50)
        assert False
    except ValueError:
        assert True

def test_markup_negativo():
    try:
        calcular_preco_venda(100, -10)
        assert False
    except ValueError:
        assert True