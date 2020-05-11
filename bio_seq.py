from bio_structs import DNA_Codons, DNA_Nucleotides
from collections import Counter
import random
import array as arr 
import numpy as np


class bio_seq:
    #Clase bio_seq. Valores por defecto: ATCG, DNA, No label

    def __init__(self, seq="ATCG", seq_type="DNA", label='No Label'):
        #Inicialización de la secuencia y validación
        self.seq = seq.upper()
        self.label = label
        self.seq_type = seq_type
        self.is_valid = self.__validate()
        assert self.is_valid, f"Provided data does not seem to be a correct {self.seq_type} sequence"

    # Funciones ADN para que el programa pueda funcionar:

    def __validate(self):
        #Comprueba si la secuencia es una cadena de ADN valida
        return set(DNA_Nucleotides).issuperset(self.seq)

    def get_seq_biotype(self):
        #Devuelve el tipo de la secuencia
        return self.seq_type

    def get_seq_info(self):
        #Información de la secuencia. Devuelve 4 strings
        return f"[Label]: {self.label}\n[Sequence]: {self.seq}\n[Biotype]: {self.seq_type}\n[Length]: {len(self.seq)}"

    def get_seq_info_array(self):
        #Información de la secuencia.Similar al anterior pero con otro formato.
        label = self.label
        sequence = self.seq
        biotype = self.seq_type
        length = len(self.seq)
        seqarray = label,sequence,biotype,length
        return seqarray

    def generate_rnd_seq(self, length=10, seq_type="DNA"):
        #Genera una secuencia aleatoria de ADN partiendo de la longitud
        seq = ''.join([random.choice(DNA_Nucleotides)
                       for x in range(length)])
        self.__init__(seq, seq_type, "Randomly generated sequence")

    def nucleotide_frequency(self):
        #Cuenta de cuantos nucleotidos hay de cada tipo dentro de la secuencia
        countseq = self.seq
        a = 0
        t = 0
        c = 0
        g = 0
        for carac in countseq:
            if carac == 'A':
                a += 1
            if carac == 'T':
                t += 1
            if carac == 'C':
                c += 1
            if carac == 'G':
                g += 1
        res = a, t,c,g
        return res

    def transcription(self):
        #Trancripcion de ADN a ARN. Reemplaza la Timina por Uracil
        return self.seq.replace("T", "U")

    def reverse_complement(self):
        #Intercambio Adenina con Timina y Guanina con Citosina. Revierte la cadena recién generada
        mapping = str.maketrans('ATCG', 'TAGC')
        return self.seq.translate(mapping)[::-1]

    def gc_content(self):
        #Contenido GC en la secuencia
        return round((self.seq.count('C') + self.seq.count('G')) / len(self.seq) * 100)

    def translate_seq(self, init_pos=0):
        #Traduce una secuencia ADN en una secuencia de aminoacidos
        return [DNA_Codons[self.seq[pos:pos + 3]] for pos in range(init_pos, len(self.seq) - 2, 3)]

    def codon_usage(self, aminoacid):
        #Proporciona la frecuencia de cada codón que codifica un aminoácido dado en una secuencia de ADN
        tmpList = []
        for i in range(0, len(self.seq) - 2, 3):
            if DNA_Codons[self.seq[i:i + 3]] == aminoacid:
                tmpList.append(self.seq[i:i + 3])

        freqDict = dict(Counter(tmpList))
        totalWight = sum(freqDict.values())
        for seq in freqDict:
            freqDict[seq] = round(freqDict[seq] / totalWight, 2)    

        freqDict = list(freqDict.items())
        freqDict = np.array(freqDict)

        return freqDict

    
 
