# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 16:37:53 2023

@author: MARIA
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
import string

# Descargar los recursos necesarios de nltk
nltk.download('stopwords')
nltk.download('punkt')

# Definir la función para limpiar el corpus
def limpiar_corpus(corpus):
    # Tokenizar el texto en palabras
    palabras = word_tokenize(corpus, language='spanish')
    
    # Convertir todas las palabras a minúsculas
    palabras = [palabra.lower() for palabra in palabras]
    
    # Eliminar las palabras de parada y los signos de puntuación
    stop_words = set(stopwords.words('spanish') + list(string.punctuation))
    palabras = [palabra for palabra in palabras if palabra not in stop_words]
    
    # Obtener la raíz de las palabras
    stemmer = SnowballStemmer('spanish')
    palabras = [stemmer.stem(palabra) for palabra in palabras]
    
    # Unir las palabras limpias en una cadena de texto
    corpus_limpio = ' '.join(palabras)
    
    return corpus_limpio

# Ejemplo de uso
corpus = "Este es un ejemplo de texto de prueba para la limpieza del corpus 3 de ella. ¡Hola Mundo!"
corpus_limpio = limpiar_corpus(corpus)
print(corpus_limpio)
