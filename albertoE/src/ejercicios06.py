import logging
import sys
from pathlib import Path

# Agregar la ruta raíz del proyecto al path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from albertoE.src.exeptions.exeption import CustomError


logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='albertoE/src/app.log'
)

# logging.debug("Log nivel debug.")
# logging.info("Log nivel info.")
# logging.warning("Log nivel warning.")
# logging.error("Log nivel error.")
# logging.critical("Log nivel critical.")



def funcion_con_error(n1: int):
    if(n1 < 0):
        raise CustomError("Ocurrió un error.")
    logging.info('El numero es correcto')

try:
    funcion_con_error(-5)
except Exception as e:
    logging.error(f"error: {e}")
else:
    logging.info(f"ejecución correcta")
finally:
    logging.info("Ejecución finalizada.")