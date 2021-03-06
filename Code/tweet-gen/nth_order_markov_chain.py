import random
import re
from dictogram import Dictogram
import string

class MarkovChain(Dictogram):
    def __init__(self, word_list, order):
        # super().__init__()
        self.order = order
        self.start_tokens = Dictogram()
        self.stop_tokens = Dictogram()

        ##### for first order MarkovChain
        # word_list[0] = re.sub("[^a-zA-Z]", '', word_list[0])
        # self.start_tokens.add_count(word_list[0].lower(), 1)
        for i in range(1, len(word_list)-1, 1):
            try:
                if((word_list[i][0].isupper()) and word_list[i-1][len(word_list[i-1])-1] in string.punctuation):
                    # word_list[i] = re.sub("[^a-zA-Z]", '', word_list[i])
                    if self.order > 1:
                        temp = list()
                        for j in range(self.order):
                            word_list[i+j] = re.sub("[^a-zA-Z]", '', word_list[i+j])
                            temp.append(word_list[i+j].lower())
                        if len(temp) > 1:
                            temp = tuple(temp)
                    else:
                        word_list[i] = re.sub("[^a-zA-Z]", '', word_list[i])
                        temp = word_list[i].lower()
                    self.start_tokens.add_count(temp, 1)
            except:
                pass

        for i in range(len(word_list)):
            try:
                if(word_list[i][len(word_list[i])-1] in string.punctuation):
                    word_list[i] = re.sub("[^a-zA-Z]", '', word_list[i])
                    # word_list[i] = word_list[i][:len(word_list[i])-1]
                    self.stop_tokens.add_count(word_list[i], 1)
            except:
                pass
        for i in range(len(word_list)-self.order):
            if self.order > 1:
                temp = list()
                for j in range(self.order):
                    word_list[i+j] = re.sub("[^a-zA-Z]", '', word_list[i+j])
                    temp.append(word_list[i+j].lower())
                if len(temp) > 1:
                    temp = tuple(temp)
            else:
                word_list[i] = re.sub("[^a-zA-Z]", '', word_list[i])
                temp = word_list[i].lower()
            if temp in self:
                self[temp].add_count(word_list[i+self.order].lower(), 1)
            else:
                self[temp] = Dictogram([word_list[i+self.order].lower()])

    def random_walk(self, length=10):
        sentence = ""
        # print("55")
        # print(self.start_word())
        if self.order > 1:
            sentence = str(self.start_word()).capitalize() + " "
        else:
            sentence = self.start_word().capitalize() + " "
        for i in range(length-self.order-1):
            next_word = self.sample(sentence)
            sentence += next_word + " "
        sentence += self.end_word() + "."
        return sentence

    def start_word(self):
        tokens = 0
        for elm in self.start_tokens:
            tokens += self.start_tokens[elm]
        dart = random.randrange(0, tokens)
        fence = 0
        for elm in self.start_tokens:
            fence += self.start_tokens[elm]
            if fence > dart:
                if self.order > 1:
                    sentence = ""
                    for i in range(len(elm)):
                        sentence += elm[i] + " "
                    return sentence
                else:
                    return elm

    def end_word(self):
        tokens = 0
        for elm in self.stop_tokens:
            tokens += self.stop_tokens[elm]
        dart = random.randrange(0, tokens)
        fence = 0
        for elm in self.stop_tokens:
            fence += self.stop_tokens[elm]
            if fence > dart:
                return elm

    def sample(self, sentence):
        sentence = sentence.split()
        sentence[0] = sentence[0].lower()
        if self.order > 1:
            key = list()
            for i in range(len(sentence)-1, len(sentence)-1-self.order, -1):
                key.append(sentence[i])
            key = tuple(key)
        else:
            key = sentence[len(sentence)-1]
        tokens = 0
        for elm in self[key]:
            tokens += self[key][elm]
        dart = random.randint(0, tokens)
        fence = 0
        for elm in self[key]:
            fence += self[key][elm]
            if fence >= dart:
                if(self.order > 1):
                    return key[len(key)-1]
                else:
                    return elm

if __name__ == '__main__':
    words = "Blue fish blue fish. Blue fish blue fish."
    word_list = words.split()
    print(word_list)
    # word_list = ["Blue", "One.", "fish.", "One", "two","blue", "fish", "two", "red", "fish", "blue", "red", "blue", "fish", "red", "blue", "fish"]
    markovChain = MarkovChain(word_list, 4)
    print(markovChain)
    print(markovChain.random_walk(10))
