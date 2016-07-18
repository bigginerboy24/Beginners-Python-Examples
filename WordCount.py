
class WordCount():

    def __init__(self):
        self.vowels = 'aeiou'
        self.count = 0

    def type_sentence(self):
        return input('Please type your sentence: ')

    def checkVowel(self, word):
        return word in self.vowels

    def Add(self):
        for word in self.sentence:
            if self.checkVowel(word):
                self.count += 1
        return (self.count)

    def split(self):
        return len(self.sentence)

    def output(self):
        message = "Sentence:  '{}' vowels: {} Chars: {}"
        vowel = self.Add()

        print(message.format(self.sentence, vowel, self.lenWord))

    def starts(self):
        self.sentence = self.type_sentence()
        self.lenWord = self.split()
        self.output()





if __name__ == '__main__':
    count = WordCount()
    count.starts()