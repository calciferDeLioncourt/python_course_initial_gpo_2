import sys
from pathlib import Path
 
# Agregar la ruta raíz del proyecto al path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from albertoE.src.ejercicios14 import Servicio


def test_service(mocker):
    mock_logger = mocker.Mock()

    service = Servicio(logger=mock_logger)

    service.procesar_data()

    mock_logger.info.assert_called_once_with("Procesar data...")