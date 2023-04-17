#!/bin/python3.10
from googletrans import Translator

translator = Translator()

texto = input("Ingrese el texto a traducir: ")
traduccion = translator.translate(texto, dest="es")
print("\n---", traduccion.text, "---\n")
