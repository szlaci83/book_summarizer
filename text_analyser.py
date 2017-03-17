import re

books = {
                'bible' : 'bible.txt',
                'stars' : 'stars.txt'
            }

class BookAnalyser():
    stop_words = ["has", "This", "had", "I", "you", "for", "or", "on", "from", "be", "at", "are", "it", "he", "as",
                  "The", "was", "by", "is", "with", "which", "in", "the", "of", "to", "and", "a", "an", "another", "no",
                  "the", "a", "an", "no", "another", "some", "any", "my", "our", "their", "her", "his", "its",
                  "another", "each", "every", "certain", "its", "another", "this", "that"]

    def __init__(self, book):
        self.rawtext, self.wordlist = self.preprocessing(book)
        self.word_dict = self.create_dict(self.wordlist)

    def __init__(self, book_file, pos_file, neg_file):
        self.rawtext, self.wordlist = self.preprocessing(book_file)
        self.word_dict = self.create_dict(self.wordlist)
        _, self.neg_words = self.preprocessing(neg_file)
        _, self.pos_words = self.preprocessing(pos_file)

    @property
    def word_count(self):
        return len(self.wordlist)

    @property
    def total_no_of_neg(self):
        return len(self.neg_words)

    @property
    def total_no_of_pos(self):
        return len(self.pos_words)

    @property
    def neg_occurence(self):
        return self.getOccurence(self.word_dict, self.neg_words)

    @property
    def pos_occurence(self):
        return self.getOccurence(self.word_dict, self.pos_words)

    @property
    def cleaned_dict(self):
        return self.ignore_words(self.word_dict, self.stop_words)

    # classifying words:
    # with regex  matching word classes
    @property
    def gerunds(self):
        return self.select_matching(self.cleaned_dict, ".*ing$")

    @property
    def simple_past_verbs(self):
        return self.select_matching(self.cleaned_dict, ".*ed$")

    @property
    def third_singular_presents(self):
        return self.select_matching(self.cleaned_dict, ".*es$")

    @property
    def modals(self):
        return self.select_matching(self.cleaned_dict, ".*ould$")

    @property
    def posessive_nouns(self):
        return self.select_matching(self.cleaned_dict, ".*\'s$")

    @property
    def plural_nouns(self):
        return self.select_matching(self.cleaned_dict, ".*s$")

    @property
    def cardinal_numbers(self):
        return self.select_matching(self.cleaned_dict, "^-?[0-9]+(.[0-9]+)?$")

    @property
    def sentence_list(self):
        return self.create_sentence_list(self.create_string(self.rawtext))

    def preprocessing(self, textfilename):
        file = open(textfilename)
        rawtext = file.readlines()
        text = self.remove_newline(rawtext)
        word_list = []
        print()
        for line in text:
            word_list += line.split()
        return rawtext, word_list

    def getOccurence(self, word_dict, word_list):
        '''get the number of occurance of words in the list in the dictionary?'''
        result = 0
        for word in word_list:
            if word in word_dict:
                result += word_dict[word]
        return result

    def create_dict(self, word_list):
        '''Returns dictionary from list input format { word : no_of_occurance_in_the_list} '''
        dict = {}
        for word in word_list:
            if word in dict:
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1
        return dict

    def ignore_words(self, dictionary,word_list):
        '''Removes the worlds in the world_list from the dictionary'''
        for word in word_list:
            if word in dictionary:
                del dictionary[word]
        return dictionary

    def select_matching(self, dict,pattern):
        '''Returns the elemets as a dictionary from a dictionary where the elements match the given pattern'''
        return_dict = {}
        keylist = dict.keys()
        for k in keylist:
            matching = re.search(pattern, k)
            if matching:
                return_dict[k] = dict[k]
        return return_dict

    def most_freq(self, word_list):
        '''Returns the most frequent word in a list of words.'''
        dict = {}
        for word in word_list:
            if word in dict:
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1
        return max(dict, key = dict.get)

    def most_freq_after(self, word_list, word_to_check, step = 1):
        '''Returns the most frequent word after a given word (word_to_check). Step means how many words after.'''
        result = "The textfile doesn't contain this word: " +word_to_check
        dict = {}
        for i in range (len(word_list)):
            if word_list[i] == word_to_check:
                word_after = word_list[i+step]
                if word_after in dict:
                    dict[word_after] = dict[word_after] +1
                else:
                    dict[word_after] = 1

        if dict:
            result =  max(dict, key = dict.get)
        return result


    def most_freq_start(self, word_list, step = 1):
        '''
        Returns the most frequent start of sentence.
        :param step:
        :return: the most frequent start of sentence.
        '''
        result = ""
        dict = {}
        for i in range (len(word_list) - step):
            matching = re.search("\w+\.", word_list[i])
            if matching:
                word_after = word_list[i+step]
                if word_after in dict:
                    dict[word_after] = dict[word_after] +1
                else:
                    dict[word_after] = 1

        if dict:
            result = max(dict, key = dict.get)
        return result

    def create_sentence(self, wlist, start, size):
        '''
        Creates a sentence starting with the 'start' following the most frequent word after each word.
        :param wlist: list of words to build the sentence from.
        :param start: the word to start with
        :param size: the length of the sentence to be created.
        :return: list of words separated with space.
        '''
        sentence = []
        sentence.append(start)
        for i in range(size):
            sentence.append(self.most_freq_after(wlist, sentence[len(sentence)-1]))
            sentence.append(" ")
        return sentence

    def remove_newline(self,sentencelist):
        '''
        Removes the new lines, and the \n and \r from the end of each list element.
        :return: list of sentences without \n \r
        '''
        for sentence in sentencelist:
            if (sentence == "\n"):
                sentencelist.remove(sentence)
            sentencelist.remove(sentence)
            sentence.replace("\n","").replace("\r","")
            sentencelist.append(sentence)
        return sentencelist

    def create_string (self, textlist):
        '''
        Creates a string from a list of strings.
        :return: string concatenated from the list elements.
        '''
        ret_string = ""
        for text in textlist:
            ret_string += text
        return ret_string

    def create_sentence_list (self, textstring):
        '''
        Creates a list of senteces separated by . (dot) from a text string.
        :return list of sentences
        '''
        sentence_list = textstring.split(".")
        return sentence_list

    def create_sentence_dict (self, sentencelist):
        '''Cresates a dict from a list of sentences and zeros out the value fields.'''
        sentence_dict = {}
        for sentence in sentencelist:
            sentence_dict[sentence] = 0
        return sentence_dict

    def dictionary_updater(self, sentence_dict, word_dict):
        '''
        Fills sentence dict with value as occurence of words in the text.
        (Updates the zeros in the sentence dict according to a word dict)
        :return Dictionary of sentences in {sentence : occurence value} format
        '''
        for sentence in sentence_dict.keys():
            val = 0
            words = sentence.split()
            for word in words:
                if word in word_dict:
                    val += word_dict[word]
            sentence_dict[sentence] = val
        return sentence_dict

    def analyse_sentiment(self, silent = True):
        wc = self.word_count
        total_pos = self.total_no_of_pos
        total_neg = self.total_no_of_neg
        no_of_neg = self.neg_occurence
        no_of_pos = self.pos_occurence
        if not silent:
            print("Wordcount of the book: ", wc)
            print("Pozitive words in my dictionary: ", total_pos)
            print("Negative words in my dictionary: ", total_neg)
            print()
            print("Negative : Positive ratio")
            print(no_of_neg, " : ", no_of_pos)
        result = {
            'wc' : wc,
            'total_pos' : total_pos,
            'total_neg' : total_neg,
            'no_of_pos' : no_of_pos,
            'no_of_neg': no_of_neg,
            }
        return result

    def word_type_stat(self, silent):
        max_word = max(self.cleaned_dict, key=self.cleaned_dict.get)
        max_gerund = max(self.gerunds, key=self.gerunds.get)
        max_spverb = max(self.simple_past_verbs, key=self.simple_past_verbs.get)
        max_thirdsingpres = max(self.third_singular_presents, key=self.third_singular_presents.get)
        max_modal = max(self.modals, key=self.modals.get)
        max_posnoun = max(self.posessive_nouns, key=self.posessive_nouns.get)
        max_plnoun = max(self.plural_nouns, key=self.plural_nouns.get)
        max_cnum = max(self.cardinal_numbers, key=self.cardinal_numbers.get)
        summary = "The " + max_posnoun + " is/are " + max_gerund + " " + max_spverb + " " + max_thirdsingpres + " " \
                  + max_modal + " be the " + max_cnum + " " + max_plnoun + "."

        if not silent:
            print("A bit of statistics:")
            print("The most frequent:")
            print("word is: ", max_word)
            print("gerund is: ", max_gerund)
            print("simple past verb :", max_spverb)
            print("3rd singular present is : ", max_thirdsingpres)
            print("modal is : ", max_modal)
            print("posessive noun is : ", max_posnoun)
            print("plural noun is :", max_plnoun)
            print("cardinal number  is : ", max_cnum)
            print("I think this book is about (according to the above statistics) :")
            print(summary)

        return {
            'max_word' : max_word,
            'max_gerund' : max_gerund,
            'max_spverb' : max_spverb,
            'max_thirdsingpres' : max_thirdsingpres,
            'max_modal' : max_modal,
            'max_posnoun' : max_posnoun,
            'max_plnoun' : max_plnoun,
            'max_cnum' : max_cnum,
            'summary' : summary
        }

    def word_frequency_stat(self, silent):
        # Most freq words after a specific word
        after_the = self.most_freq_after(self.wordlist, "the")
        before_the = self.most_freq_after(self.wordlist, "the", -1)
        before_not = self.most_freq_after(self.wordlist, "not", -1)
        after_not = self.most_freq_after(self.wordlist, "not")
        start = self.most_freq_start(self.wordlist)
        end = self.most_freq_start(self.wordlist, 0)

        if not silent:
            print("in this textfile the most frequent word after: the is: ", after_the)
            print("in this textfile the most frequent word before: the is: ", before_the)
            print()
            print("in this textfile the most frequent word after: not is: ", after_not)
            print("in this textfile the most frequent word before: not is: ", before_not)
            print()
            print("Most freq. start of sentence:")
            print(start)
            print("Most freq. end of sentence:")
            print(end)

        result = {
            'after_the'  : after_the,
            'before_the' : before_the,
            'after_not'  : after_not,
            'before_not' : before_not,
            'start'      : start,
            'end'        : end
         }
        return result

    def sentence_builder(self, silent):
        start = self.most_freq_start(self.wordlist)
        sentence = self.create_sentence(self.wordlist, start, 10)
        sentence_dict = self.create_sentence_dict(self.sentence_list)
        sentence_dict2 = self.dictionary_updater(sentence_dict, self.word_dict)
        powerful = max(sentence_dict2, key=sentence_dict2.get)

        if not silent:
            print("The most 'probable' 10 word sentence:(putting the most frequent word after the most probable start "
                  "of sentence...)")
            print(sentence)
            print("That might be a bit closer...")
            print()
            print("I have another method, let me show yout the most 'powerful' sentences: (the sentence from the book "
                  "contaning the most of the most probable words)")
            print(powerful)

        result = {
            'sentence' : sentence,
            'powerful' : powerful
        }
        return result

    def analyse_meaning(self, silent=True):
        if not silent:
            print("This simple program attempts to summarise a book in a sentence.")
            print("Wordcount: ", self.word_count)
        self.word_frequency_stat(False)
        self.word_type_stat(False)
        self.sentence_builder(False)


def main():
    txt_file        = "book.txt"
    positive_file   = "positive-words.txt"
    negative_file   = "negative-words.txt"

    book = BookAnalyser(txt_file, positive_file, negative_file)
    book.analyse_sentiment()
    book.analyse_meaning()
    #book.analyse_sentiment(silent=False)
    #print(book)

if __name__ == '__main__':
    main()