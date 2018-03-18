import re
from texttable import Texttable

def load_data(filepath):
    try:
        f = open(filepath, 'r')
        text = f.read()
    except All:
        print (e)
    finally:
        f.close
        return text

def get_words_from_text(text):
    regex = re.compile(r"[^a-zа-я]", re.IGNORECASE)
    text = text.lower();
    text = re.sub(regex, ' ', text)
    return [x for x in re.split(' +', text) if x]

def get_most_frequent_words(text):
    words = get_words_from_text(text)
    dictionary = []
    words_num = []
    t = Texttable()
    t.add_row(["Word", "Number uf uses"])
    for word in words:
        try:
            i = dictionary.index(word)
            words_num[i] += 1
        except ValueError:
            dictionary.append(word)
            words_num.append(1)
    for i in range(len(dictionary)):
        t.add_row([dictionary[i], str(words_num[i])])
    print (t.draw())


if __name__ == '__main__':
    print ("Please input path for analized file")
    text = load_data (input())
    get_most_frequent_words(text)
