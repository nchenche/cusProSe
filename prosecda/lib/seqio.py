# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:43:14 2020

@author: nicolas
"""
import shutil

def read_fasta(sequences=None):
    """
    - Input: fasta file
    - Output: dictionary with 1st header part as keys and sequences as values
    """
    if sequences is not None:
        fasta = {}
        with open(sequences, 'r') as sequences_file:
            for l in sequences_file:
                if l.startswith('>'):
                    seq_name = l.split()[0].split('>')[-1]
                    if seq_name not in fasta:
                        fasta[seq_name] = ''
                    continue
                sequence = l.strip().replace('*','')
                fasta[seq_name] = fasta[seq_name]+sequence
                
        return fasta
    else:
        print('Input must be a fasta file...'.format())


def write_fasta(seqfasta=None, output=None):
    """
    - Input: list of fasta sequence(s)
    """
    if seqfasta is not None:
        if output is not None:           
            with open(output, "w") as fasta_file:
                fasta_file.write(''.join(seqfasta))
        else:
            print('No output name provided...'.format())
    else:
        print('Error in the input provided...'.format())


def concat_file(outputfile, inputfilelist):    
    with open(outputfile,'wb') as wfd:
        for f in inputfilelist:
            with open(f,'rb') as fd:
                shutil.copyfileobj(fd, wfd, 1024*1024*10)


def seqnumber(msafile=None):
    if msafile is not None:
        nb = 0
        with open(msafile, 'r') as msa:
            for line in msa:
                if line.startswith('>'):
                    nb+=1
        
        return nb
    else:
        print('Error: msa file required...'.format())


