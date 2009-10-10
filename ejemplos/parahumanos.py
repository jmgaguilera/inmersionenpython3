'''Convierte un tamaño de fichero en un formato legible por personas

Funciones disponibles:
tamanyo_aproximado(tamanyo, un_kb_es_1024_bytes)
    toma un tamaño de fichero y devuelve una cadena legibel por una persona

Ejemplo:
>>> tamanyo_aproximado(1024)
'1.0 KiB'
>>> tamanyo_aproximado(1000, False)
'1.0 KB'

'''

SUFIJOS = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
           1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def tamanyo_aproximado(tamanyo, un_kilobyte_es_1024_bytes=True):
    '''Convierte un tamaño de fichero en un formato legible por personas

    Argumentos/parámetros:
    tamanyo -- tamaño de fichero en bytes
    un_kilobyte_es_1024_bytes -- si True (por defecto), 
                                 usa múltiplos de 1024
                                 si False, usa múltiplos de 1000

    retorna: string

    '''
    if tamanyo < 0:
        raise ValueError('el número debe ser no negativo')

    multiplo = 1024 if un_kilobyte_es_1024_bytes else 1000
    for sufijo in SUFIJOS[multiplo]:
        tamanyo /= multiplo
        if tamanyo < multiplo:
            return '{0:.1f} {1}'.format(tamanyo, sufijo)

    raise ValueError('número demasiado grande')

if __name__ == '__main__':
    print(tamanyo_aproximado(1000000000000, False))
    print(tamanyo_aproximado(1000000000000))

# Copyright (c) 2009, Mark Pilgrim, All rights reserved.
# Copyright (c) 2009, Traducción: José Miguel González Aguilera.
# 
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS'
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
