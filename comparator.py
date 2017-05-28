# the comparison class
import re



class Comparator:


    def __init__(self):
        pass


    def compare(self,posting,lttr):
        letter,len_lttr,counts = self.init_cache(lttr)
        post,len_post,_ = self.init_cache(posting)
        for word in letter:
            if self.word_in_text(word,posting):
                print(word)
                counts += 1



    def init_cache(self,text):
        delims = ''
        for num in range(33,127):
            ascii = chr(num)
            if ascii != '+' and not ascii.isalnum():
                delims += ascii
        cache = [x.strip(delims) for x in text.split()]
        return cache, len(cache), 0



    def word_in_text(self,a,b):
        return re.compile(r'\b({0})\b'.format(a), flags=re.IGNORECASE).search(b)


