
def read_text(filePath):
    file_path = "C:/Users/Mkhitar/Desktop/KRISP/mlk_speech.txt"
    text =""
    with open(file_path) as f:
        text = f.readlines()
    return text[0]

