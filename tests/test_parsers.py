# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    fasta = FastaParser("data/test.fa")
    seqs = list(fasta)
    assert len(seqs) == 100
    assert seqs[0] == ("seq0", "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA")
    assert seqs[99] == ("seq99", "CAAACCGGCGATGCGGGTACTCCCTACAAGTTGGACTCCGCAGCGAACGCCGCAGGGGCCATTATACGGCGGTCTTGGCGGCGTCGACCAGGCCGGTCCA")
    
    fasta = FastaParser("tests/bad.fa")
    with pytest.raises(ValueError):
        list(fasta)
    fasta = FastaParser("tests/blank.fa")
    with pytest.raises(ValueError):
        list(fasta)


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    fasta_real = FastaParser("data/test.fa")
    fasta_wrong = FastaParser("data/test.fq")

    unwanted_none = False
    for seq in fasta_real:
        if seq[0] is None or seq[1] is None:
            unwanted_none = True
    found_none = False
    for seq in fasta_wrong:
        if seq[0] is None or seq[1] is None:
            found_none = True
    assert not unwanted_none
    assert found_none


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    fastq = FastqParser("data/test.fq")
    seqs = list(fastq)
    assert len(seqs) == 100
    assert seqs[0] == ("seq0", "TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG", "*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7\"94(>7='(!5\"2/!%\"4#32=")
    assert seqs[99] == ("seq99", "CCGAGTTTTGTAGTGGGCTCAACTGAAATCCTATTCTTAGACGATTGGTCATAAAACCCTTTCACTGTACGGACGTAGACCCTGCTCCGTCTTCCAGCAG", "2$7)*5:\"=+++!:.=>!5>79)8!566$!3*/4$=4.%=//;900$9)!%)4%$=0\":02\"0=!0#/>+*1$1$39!.8+9<'1$*1$321&<'&9,)2")
    
    fastq = FastqParser("tests/bad.fq")
    with pytest.raises(ValueError):
        list(fastq)
    fastq = FastqParser("tests/blank.fq")
    with pytest.raises(ValueError):
        list(fastq)

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fastq_real = FastqParser("data/test.fq")
    fastq_wrong = FastqParser("data/test.fa")

    unwanted_none = False
    for seq in fastq_real:
        if seq[0] is None or seq[1] is None or seq[2] is None:
            unwanted_none = True
    found_none = False
    for seq in fastq_wrong:
        if seq[0] is None or seq[1] is None or seq[2] is None:
            found_none = True
    assert not unwanted_none
    assert found_none