def DNA_strand(dna):
    new_str = dna.replace('A','%temp%').replace('T','A').replace('%temp%','T').replace('G','%temp%').replace('C','G').replace('%temp%','C')
    return new_str
