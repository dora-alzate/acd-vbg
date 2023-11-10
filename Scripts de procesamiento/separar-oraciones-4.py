# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 18:17:44 2023

@author: MARIA
"""

import os
import stanza
import pandas as pd

def separar_oraciones(nlp, texto):
    doc = nlp(texto)
    oraciones = [sent.text for sent in doc.sentences]
    return oraciones

def analizar_oracion(oracion):
    agente = ""
    verbo = ""
    paciente = ""
    voz_activa = True

    for word in oracion.words:
        if word.upos == "VERB":
            verbo = word.text
            voz_activa = word.deprel != "aux:pass"
        elif word.deprel == "nsubj" or word.deprel == "nsubj:pass":
            agente = oracion.words[word.head - 1].text
        elif word.deprel == "obj" or word.deprel == "iobj":
            paciente = oracion.words[word.head - 1].text

    return agente, verbo, paciente, voz_activa

def procesar_archivos(input_folder, output_folder):
    stanza.download('es')
    nlp = stanza.Pipeline('es', processors='tokenize,mwt,pos,lemma,depparse', use_gpu=True)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as f:
                texto = f.read()

            oraciones = separar_oraciones(nlp, texto)

            data = []
            for oracion_text in oraciones:
                oracion = nlp(oracion_text).sentences[0]
                agente, verbo, paciente, voz_activa = analizar_oracion(oracion)
                data.append([oracion_text, agente, verbo, paciente, voz_activa])

            df = pd.DataFrame(data, columns=["Oración", "Agente", "Verbo", "Paciente", "Voz activa"])
            df.to_csv(os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_oraciones.csv"), index=False, encoding='utf-8', sep='\t')

if __name__ == "__main__":
    input_folder = "G:\\Mi unidad\\96 UdeA - RUG\\01 TDG Dora Alzate\\Corpus V2\\Subcorpus1"
    output_folder = "G:\\Mi unidad\\96 UdeA - RUG\\01 TDG Dora Alzate\\Corpus V2\\Subcorpus1"
    procesar_archivos(input_folder, output_folder)
