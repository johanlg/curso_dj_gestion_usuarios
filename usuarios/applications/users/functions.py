# Funciones extra de nuestra aplicacion Users

import random
import string

# Funcion para generar codigo random de 6 caracteres
def generador_codigo_validacion_email_login(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))