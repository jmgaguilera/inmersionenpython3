#!/bin/bash
mkdir ./intermedio
cp ./imagen/* ./intermedio
cp *.tex ./intermedio
cp ./output/* ./intermedio
cp ./python-powered.png ./intermedio
cp ./by-nc-sa.png ./intermedio

cd intermedio

ACCENT_IMAGES='large'

latex2html -split 3 -show_section_numbers -nocontents_in_navigation -local_icons -iso_language ES -prev_title "Anterior" -no_math -dir=../output_html -html_version 4.0,latin,unicode,math ./inmersionEnPython.tex

cd ../output_html

# Pendiente de quitar los saltos de más en los html
for fich in *.html
do
   echo $fich
  filename=$(basename "$fich")
  extension="${filename##*.}"
  filename="${filename%.*}"
   cat "$filename.$extension" | ../suprbtnnaveg.py | sed -e 's/Contents/Tabla de contenido/g' | sed -e 's/Next/Siguiente/g' -e 's/Previous/Anterior/g' -e 's/Up/Subir a/g' -e 's/Subsections/Apartados/g' | sed -e 's/<pre>/<pre>\n/' | sed -e '/language=Python/d' | sed -e '/breaklines=true/d' | sed  -e '/mathescape/d' | sed -e ':a;N;$!ba;s/-->\n<SPAN/--><SPAN/g' >"$filename.tmp"
   rm "$filename.$extension"
   mv "$filename.tmp" "$filename.$extension"
done


cd ..

rm -Rf ./intermedio
