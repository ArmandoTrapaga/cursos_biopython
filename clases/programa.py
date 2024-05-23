from Bio import SeqIO
#dirección de archivo
filename = "C:/Users/phoen/OneDrive/Escritorio/cursos_biopython/seq.nt.fa"
#por cada record queremos ID, longitud seq y traducción
for seq_record in SeqIO.parse(filename, "fasta"):
    print('ID {}'.format(seq_record.id))
    print('len {}'.format(len(seq_record)))
    print('Traducción {}'.format(seq_record.seq.translate(to_stop=False)))