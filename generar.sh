#!/bin/bash
pdflatex -output-directory=./output ./inmersionEnPython.tex
latex2html -dir=./output_html -html_version 4.0,latin,unicode ./inmersionEnPython.tex
latex2html -split=0 -dir=./output_html_full -html_version 4.0,latin,unicode ./inmersionEnPython.tex
