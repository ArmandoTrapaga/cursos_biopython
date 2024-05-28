from Bio.Seq import Seq
from Bio import SeqIO
import re

archivo_seq = "C:/Users/phoen/OneDrive/Escritorio/cursos_biopython/data/seq.nt.fa"
'''
for seq_record in SeqIO.parse(archivo_seq, "fasta"):
    print('ID {}:'.format(seq_record.id))
    print('len {}'.format(len(seq_record)))
    #print('Traducción {}'.format(seq_record.seq.translate(to_stop=False)))

seqobj = Seq('ATGCGATCGAGC')
seq_str_forward = str(seqobj)  
seq_str_reverse = seq_str_forward[::-1]
print(seqobj.reverse_complement())
'''
for i in range(1):

    with open(f"Frame {i+1}", "w") as file_forward:
        for seq_record in SeqIO.parse(archivo_seq, "fasta"):
            file_forward.write(">{}\n".format(seq_record.id))
            seq_str_forward = str(seq_record.seq)
            for codon in re.findall(r"(.{3})", seq_str_forward[i:]):  # Modificación aquí: Usamos [1:] para empezar desde el segundo carácter
                file_forward.write(codon + " ")
            file_forward.write("\n")      
'''
for i in range(3):
    print(f"Marco {i+4}")
    with open(f"Frame {i + 4}", "w") as file_reverse:
        for seq_record in SeqIO.parse(archivo_seq, "fasta"):
            file_reverse.write(">{}\n".format(seq_record.id))
            seq_str_forward = str(seq_record.seq)
            seq_str_reverse = seq_str_forward[::-1]
        for codon in re.findall(r"(.{3})", seq_str_reverse[i:]):  # Modificación aquí: Usamos [1:] para empezar desde el segundo carácter
            file_reverse.write(codon + "\t")
'''