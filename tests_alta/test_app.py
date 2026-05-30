import pytest # type: ignore
from src_alta.app import calcular_rentabilidade

def test_rentabilidade_50_porcento():
    assert calcular_rentabilidade(100, 150) == 50

def test_rentabilidade_100_porcento():
    assert calcular_rentabilidade(100, 200) == 100

def test_custo_zero():
    with pytest.raises(ValueError):
        calcular_rentabilidade(0, 100)