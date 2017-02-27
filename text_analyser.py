import re

books = {
                'bible' : 'bible.txt',
                'stars' : 'stars.txt'
            }

stop_words = ["has", "This", "had", "I", "you", "for", "or", "on", "from", "be", "at", "are", "it", "he", "as", "The",
              "was", "by", "is", "with", "which", "in", "the", "of", "to", "and", "a", "an", "another", "no", "the",
              "a", "an", "no", "another", "some", "any", "my", "our", "their", "her", "his", "its", "another", "each",
              "every", "certain", "its", "another", "this", "that"]

def create_dict(word_list):
    '''Returns dictionary from list input format { word : no_of_occurance_in_the_list} '''
    dict = {}
    for word in word_list:
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 1
    return dict


def ignore_words(dictionary, word_list):
    '''Removes the worlds in the world_list from the dictionary'''
    for word in word_list:
        if word in dictionary:
            del dictionary[word]
    return dictionary

def select_matching(dict, pattern):
    '''Returns the elemets as a dictionary from a dictionary where the elements match the given pattern'''
    return_dict = {}
    keylist = dict.keys()
    for k in keylist:
        matching = re.search(pattern, k)
        if matching:
            return_dict[k] = dict[k]
    return return_dict

def most_freq(word_list):
    '''Returns the most frequent word in a list of words.'''
    dict = {}
    for word in word_list:
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 1
    return max(dict, key = dict.get)

def most_freq_after(word_list, word_to_check, step = 1):
    '''Returns the most frequent word after a given word (word_to_check). Step means how many words after.'''
    result = "The textfile doesn't contain this word: " +word_to_check
    dict = {}
    #populate the dictionary
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


def most_freq_start(word_list, step = 1):
    result = ""
    dict = {}
    #populate the dictionary
    for i in range (len(word_list) - step):
        matching = re.search("\w+\.", word_list[i])
        if matching:
            word_after = word_list[i+step]
            if word_after in dict:
                dict[word_after] = dict[word_after] +1
            else:
                dict[word_after] = 1

    if dict:
        result =  max(dict, key = dict.get)
        #print(max(dict.values()))
    return result

def create_sentence(wlist, start, size):
    sentence = []
    sentence.append(start)
    for i in range(size):
        sentence.append(most_freq_after(wlist, sentence[len(sentence)-1]))
        #sentence.append(" ")
    return sentence

def remove_newline( sentencelist ):
    for sentence in sentencelist:
        if (sentence == "\n"):
            sentencelist.remove(sentence)
        sentencelist.remove(sentence)
        sentence.replace("\n","").replace("\r","")
        sentencelist.append(sentence)
    return sentencelist

def create_string (textlist):
    ret_string = ""
    for t in textlist:
        ret_string += t
    return ret_string

def create_sentence_list (textstring):
    sentence_list = textstring.split(".")
    return sentence_list

def create_sentence_dict (sentencelist):
    dict = {}
    for sentence in sentencelist:
        dict[sentence] = 0
    return dict

def dictionary_updater(sentence_dict, word_dict):
    for sentence in sentence_dict.keys():
        val = 0
        words = sentence.split()
        for word in words:
            if word in word_dict:
                val += word_dict[word]
        sentence_dict[sentence] = val
    return sentence_dict