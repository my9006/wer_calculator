import text_to_speech as tts
import wer_calculator as wer
import levenstein_distance_calculator as ldc


def process_data(testCase):
    recognized_speech = tts.speech_to_text(testCase['audio'])
    text = testCase['text']
    wer_value = wer.calculate_wer(recognized_speech, text)
    levenstein_value = ldc.calculate_levenstein_distance(recognized_speech, text)
    output = {'wer':wer_value, "levenstein_distance":levenstein_value}
    return output

