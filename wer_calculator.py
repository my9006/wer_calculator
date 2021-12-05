from jiwer import wer


def calculate_wer(speech, text):
    return wer(speech, text)
