import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import os
import re


# Descargar los recursos necesarios de nltk
nltk.download('stopwords')
nltk.download('punkt')

# Carpeta de entrada que contiene los archivos de texto sucios
input_folder = 'G:\\Mi unidad\\96 UdeA - RUG\\01 TDG Dora Alzate\\Corpus V2\\Nivel 3'

# Carpeta de salida para los archivos de texto limpios
output_folder = 'G:\\Mi unidad\\96 UdeA - RUG\\01 TDG Dora Alzate\\Corpus V2\\Nivel 5'

# Expresión regular para encontrar los caracteres no alfabéticos
non_alpha = re.compile(r'[^a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s\d/]+')

num = 1



# Recorre cada archivo en la carpeta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        # Abre el archivo de entrada y crea un nuevo archivo de salida
        with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as infile, \
             open(os.path.join(output_folder, filename), 'w', encoding='utf-8') as outfile:
                 
                 texto1 = infile.read()
                 
                 # Elimina los caracteres no alfabéticos del texto
                 texto = non_alpha.sub('', texto1)
                 
                 # Tokenizar el texto en palabras
                 palabras = word_tokenize(texto, language='spanish')
                 # Convertir todas las palabras a minúsculas
                 palabras = [palabra.lower() for palabra in palabras]
                 
                 # Eliminar las palabras de parada y los signos de puntuación
                 #stop_words = set(stopwords.words('spanish') + list(string.punctuation))
                 stop_words = {'que',
                                'y',
                                'de',
                                'a',
                                'la',
                                'en',
                                'el',
                                'le',
                                'un',
                                'con',
                                'lo',
                                'una',
                                'se',
                                'por',
                                'las',
                                'como',
                                'los',
                                'su',
                                'al',
                                'muy',
                                'del',
                                'eso',
                                'ese',
                                'ya ',
                                'este ',
                                'está ',
                                'esto',
                                'algo',
                                'algún',
                                'alguna ',
                                'alguno',
                                'algunos',
                                'ante',
                                'cual',
                                'cuales',
                                'del',
                                'desde',
                                'e',
                                'el',
                                'en',
                                'entonces'}
                 palabras = [palabra for palabra in palabras if palabra not in stop_words]
                 
                 # Unir las palabras limpias en una cadena de texto
                 texto_limpio = ' '.join(palabras)
                 
                 # Escribe la línea limpia en el archivo de salida
                 print ("Texto limpio:")
                 print(texto_limpio)
                 
                 outfile.write(texto_limpio) 
                 
                 print ("Voy en el archivo ")
                 print (num)
                 num = num + 1
             
