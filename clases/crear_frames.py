'''
NAME 

Creador de archivos frames

VERSION
        
2.0

AUTHOR

Armando Gael Gonzalez Trapaga       

DESCRIPTION

Crea un total de 6 archivos evaluando un archivo fasta, donde cada archivo contiene los codones de sus secuencias 
separados por espacios segun sea su marco de lectura

CATEGORY

Biología Computacional

USAGE

    % python crear_frames.py

ARGUMENTS

- archivo: La ruta del archivo que contiene la cadena de ADN a analizar.

METHOD

1.- Se parsea el archivo fasta dado por el usario al llamar al programa
2.- Se llama la funcion crear_frames con el archivo parseado y guardado en una variable 
3.- La funcion hace un for para crear un archivo donde establece su titulo segun el marco de lectura  
4.- Se abre un for anidado que asigna a la variable seq_str_forward la secuencia segun su id en el archivo
5.- Se abre otro for anidado que separa los condones de la cadena cambiando su inicio en i para cambiar el marco
6.- Se realiza los mismos pasos del 3 al 5 con la diferencia que invierte la cadena para el resto de marcos
'''
#===========================================================================
#=================================Imports===================================
from Bio.Seq import Seq
from Bio import SeqIO
import re
import argparse
#============================================================================

# ===========================================================================
# ================================Funtions===================================

parser = argparse.ArgumentParser(description="Lee archivo de entrada y salida")

parser.add_argument("input_file", type=str, help="El archivo de texto que quieres procesar.")

args = parser.parse_args()

#Asignamos el parseo a una variable del main
archivo_seq = args.input_file
#archivo_seq = "C:/Users/phoen/OneDrive/Escritorio/cursos_biopython/data/seq.nt.fa"
def crear_frames(archivo):
    try:
        for i in range(3):
            #Se establece el titulo i + 1 
            with open(f"Frame {i+1}", "w") as file_forward:
                for seq_record in SeqIO.parse(archivo, "fasta"):
                    #Conseguimos el ID de la secuencia 
                    file_forward.write(">{}\n".format(seq_record.id))
                    #Volvemos cadena a la secuencia
                    seq_str_forward = str(seq_record.seq)
                    for codon in re.findall(r"(.{3})", seq_str_forward[i:]): 
                        #Escribimos el codon en el archivo separados por un espacio
                        file_forward.write(codon + " ")
                    file_forward.write("\n")      
        #Mismo proceso para la cadena invertida
        for i in range(3):
            with open(f"Frame {i + 4}", "w") as file_reverse:
                for seq_record in SeqIO.parse(archivo, "fasta"):
                    file_reverse.write(">{}\n".format(seq_record.id))
                    seq_str_forward = str(seq_record.seq)
                    seq_str_reverse = seq_str_forward[::-1]
                    for codon in re.findall(r"(.{3})", seq_str_reverse[i:]): 
                        file_reverse.write(codon + " ")
                    file_reverse.write("\n")
    except IOError:
        print("IOERROR: No se pudo abrir el archivo. Por favor, asegúrate de que el archivo existe y que has proporcionado la ruta correcta.")

#=========================================================================
#============================Main=========================================
#Se llama a la funcion
crear_frames(archivo_seq)
#=========================================================================