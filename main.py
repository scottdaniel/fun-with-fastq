#!/usr/bin/env python

from __future__ import print_function
import os

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
split("--additional-suffix=.fastq","-d","-n","l/10","DNA_1_CGATGT_L002_R2_008.fastq.trimmed.clipped","split")

#now can we do that with Biopython?
#yup, from http://biopython.org/wiki/Split_large_file 

def batch_iterator(iterator, batch_size):
    """Returns lists of length batch_size.

    This can be used on any iterator, for example to batch up
    SeqRecord objects from Bio.SeqIO.parse(...), or to batch
    Alignment objects from Bio.AlignIO.parse(...), or simply
    lines from a file handle.

    This is a generator function, and it returns lists of the
    entries from the supplied iterator.  Each list will have
    batch_size entries, although the final list may be shorter.
    """
    entry = True  # Make sure we loop once
    while entry:
        batch = []
        while len(batch) < batch_size:
            try:
                entry = iterator.next()
            except StopIteration:
                entry = None
            if entry is None:
                # End of file
                break
            batch.append(entry)
        if batch:
            yield batch

from Bio import SeqIO

record_iter = SeqIO.parse(open("DNA_1_CGATGT_L002_R2_008.fastq.trimmed.clipped"),"fastq")

from plumbum.cmd import wc
wc("-l","DNA_1_CGATGT_L002_R2_008.fastq.trimmed.clipped")
558128/10
#Not the actual amound of records because each fastq needs 4 lines
#this gives you the actual amount of records
my_fastq = SeqIO.index("DNA_1_CGATGT_L002_R2_008.fastq.trimmed.clipped","fastq")
len(my_fastq)
len(my_fastq)/10

i=0
count=0
batch=0
for i, batch in enumerate(batch_iterator(record_iter, 13953)):
    filename = "split_%i.fastq" % (i + 1)
    handle = open(filename, "w")
    count = SeqIO.write(batch, handle, "fastq")
    handle.close()
    print("Wrote %i records to %s" % (count, filename))

#It's neat, but split is a lot easier

#Now, let's build the list of files again but only those that begin with split
fastqs={}
for dirpath,dirnames,files in os.walk("."):
    for fname in files:
        if fname.startswith('split'):
            fastqs[fname] = os.sep.join([dirpath,fname])
fastqs
