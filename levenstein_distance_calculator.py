import Levenshtein


def calculate_levenstein_distance(speech, text):
    return Levenshtein.distance(speech, text)
