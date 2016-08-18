#!/usr/bin/env python3

# -*- coding: utf-8 -*-


import sys

eliminando_filas = False
for linea in sys.stdin:

    if eliminando_filas:
        if "<BR>" in linea:
            eliminando_filas = False
        continue

    if "--Navigation Panel" in linea:
        eliminando_filas = True

    sys.stdout.write(linea)


