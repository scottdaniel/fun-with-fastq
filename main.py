#!/usr/bin/env python

from __future__ import print_function
import os
from Bio import SeqIO

os.chdir("/Users/Scott/fun-with-fastq/fastq/")

#TIL how to walk
for path,subdir,file in os.walk("./"):
    print(file[0])
    source_fastq = open(path+file[0],'r')

os.getcwd()
thing = {}
thing.update({"key1":"value1"})
thing.update({"key2":"value2"})
thing

#TIL how to iterate over keys
for key in thing.iterkeys():
    print(key)
    
#lets split up the fastq with plumbum and gnu-split
from plumbum.cmd import split
split("-n","l/10","DNA_1_CGATGT_L002_R2_008.fastq.trimmed.clipped")

#now can we do that with Biopython?
