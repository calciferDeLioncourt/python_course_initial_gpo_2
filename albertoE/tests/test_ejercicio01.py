import sys
from pathlib import Path

# Agregar la ruta raíz del proyecto al path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from albertoE.src.ejercicios11 import Notificador


def test_enviar():
    notifica = Notificador()

    msj = notifica.enviar_mensaje("Alberto")

    assert "Alberto" in msj

def test_cancelar():
    notifica = Notificador()

    msj = notifica.cancelar()

    assert "Cancelado" in msj