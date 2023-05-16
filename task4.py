import re
import string

class StringFormatter(object):
    def __init__(self, str):
        re.sub(r'[^\w\s]', '', str)
        self.str = str

    def DelWords(self, n):
        words = self.str.split(" ")
        result = []
        for word in words:
            if len(word) >= n:
                result.append(word)
        return " ".join(result)

    def replaceNumbers(self):
        result = re.sub('\d', '*', self.str)
        return result

    def addSpace(self):
        result = " ".join(self.str)
        return result

    def sortWords(self):
        sortWords = self.str.split(" ")
        sortWords.sort(key=lambda item: (-len(item), item))
        return sortWords

    def alphabetSort(self):
        result = sorted(self.str.split(' '))
        return result

str = input("Введите строку: ")
f = StringFormatter(str)
print(f.alphabetSort())