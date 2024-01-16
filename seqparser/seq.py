# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    reverse_transcript = reverse_transcribe(seq)
    if reverse:
        return reverse_transcript
    else:
        return reverse_transcript[::-1]

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    transcript = ''
    seq = seq.upper()
    for letter in seq:
        if letter not in TRANSCRIPTION_MAPPING.keys():
            raise ValueError("seq contains an unrecognized charater")
        transcript += TRANSCRIPTION_MAPPING.get(letter)
    return transcript[::-1]