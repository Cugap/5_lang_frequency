import re
from collections import Counter
from texttable import Texttable

def load_data(filepath):
    try:
        file = open(filepath, "r")
        text = file.read()
    except Exception as ex:
        print (ex)
    finally:
        file.close
        return text

def get_words_from_text(text):
    text = text.lower()
    regex = re.compile(r"[^a-zа-я]", re.IGNORECASE)
    text = re.sub(regex, ' ', text)
    
    return [x for x in re.split(" +", text) if x]

def get_most_frequent_words(text):
    words = get_words_from_text(text)
    counter = Counter(words)
    
    table = Texttable()
    table.add_row(["Word", "Number uf uses"])
    for word, cnt in counter.items():
        table.add_row([word, cnt])

    print (table.draw())


if __name__ == "__main__":
    print ("Please input path for analized file")
    text = load_data(input())
    get_most_frequent_words(text)
