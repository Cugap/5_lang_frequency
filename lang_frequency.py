import re
from collections import Counter
from texttable import Texttable


def load_data(filepath):
    text = None
    try:
        with open(filepath, "r") as loading_file:
            text = loading_file.read()
    except FileNotFoundError as ex:
        print(ex)
    return text

def get_words_from_text(text):
    if text == None or len(text) == 0:
        return text
    text = text.lower()
    regex = re.compile(r"[^a-zа-я]", re.IGNORECASE)
    text = re.sub(regex, ' ', text)
    
    return [x for x in re.split(" +", text) if x]

def get_most_frequent_words(text):
    if text == None or len(text) == 0:
        return
    words = get_words_from_text(text)
    counter = Counter(words)
    
    table = Texttable()
    table.add_row(["Word", "Number uf uses"])
    for word, cnt in counter.items():
        table.add_row([word, cnt])

    print(table.draw())


if __name__ == "__main__":
    print("Please input path for analized file")
    text = load_data(input())
    get_most_frequent_words(text)
