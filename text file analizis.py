import re

def create_dict(word_list):
    dict = {}
    for word in word_list:
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 1
    return dict


def ignore_words(dictionary, word_list):
    #dict = dictionary
    for word in word_list:
        if word in dictionary:
            del dictionary[word]
    return dictionary

def select_matching(dict, pattern):
    return_dict = {}
    keylist = dict.keys()
    for k in keylist:
        matching = re.search(pattern, k)
        if matching:
            #return_dict[k : ""]
            return_dict[k] = dict[k]
    return return_dict

def most_freq(word_list):
    dict = {}
    for word in word_list:
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 1
    return max(dict, key = dict.get)

def most_freq_after(word_list, word_to_check, step = 1):
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
        #print(max(dict.values()))
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


def analyse_meaning( textfilename, list_of_words_to_omit = [] ):
    print("This simple program attempts to summarise a book in a sentence.")
    #txtfile = input("Which book you want me to summarize?(ie: book.txt):")
    file = open(textfilename)
    #words_to_omit = list_of_words_to_omit

    rawtext = file.readlines()

    text = remove_newline(rawtext)
    #print(text)
    word_list = []
    #print(text)
    print("Reading ", textfilename," ...")
    print()
    for line in text:
        word_list +=line.split()

    print("Wordcount: ",len(word_list))

    #print(word_list)

    full_dict = create_dict(word_list)
    cleaned_dict = ignore_words(full_dict, list_of_words_to_omit)

    #classifying words:
    #some regex  matching word classes
    gerunds = select_matching(cleaned_dict, ".*ing$")
    simple_past_verbs = select_matching(cleaned_dict, ".*ed$")
    third_singular_presents = select_matching(cleaned_dict, ".*es$")
    modals = select_matching(cleaned_dict, ".*ould$")
    posessive_nouns = select_matching(cleaned_dict, ".*\'s$")
    plural_nouns = select_matching(cleaned_dict, ".*s$")
    cardinal_numbers = select_matching(cleaned_dict,"^-?[0-9]+(.[0-9]+)?$")

    max_word = max(cleaned_dict, key = cleaned_dict.get)
    max_gerund = max(gerunds, key = gerunds.get)
    max_spverb = max(simple_past_verbs, key = simple_past_verbs.get)
    max_thirdsingpres = max(third_singular_presents, key = third_singular_presents.get)
    max_modal = max(modals, key = modals.get)
    max_posnoun = max(posessive_nouns, key = posessive_nouns.get)
    max_plnoun = max(plural_nouns, key = plural_nouns.get)
    max_cnum = max(cardinal_numbers, key = cardinal_numbers.get)

    print("A bit of statistics:")
    print("The most frequent:")
    print("word is: ", max_word)
    print("gerund is: ", max_gerund)
    print("simple past verb :",max_spverb )
    print("3rd singular present is : ", max_thirdsingpres )
    print("modal is : ", max_modal)
    print("posessive noun is : ",max_posnoun )
    print("plural noun is :", max_plnoun)
    print("cardinal number  is : ", max_cnum )


    #Most freq words after a specific word
    after_the = most_freq_after(word_list, "the" )
    before_the = most_freq_after(word_list, "the", -1 )

    print("in this textfile the most frequent word after: the is: ",after_the)
    print("in this textfile the most frequent word before: the is: ",before_the)


    before_not = most_freq_after(word_list, "not", -1)
    after_not = most_freq_after(word_list, "not")

    print()
    print("in this textfile the most frequent word after: not is: ",after_not)
    print("in this textfile the most frequent word before: not is: ",before_not)


    print()
    print("Most freq. start of sentence:")
    start = most_freq_start(word_list)
    print(start)

    print("Most freq. end of sentence:")
    end = most_freq_start(word_list,0)
    print(end)


    summary = "The " + max_posnoun + " is/are " + max_gerund + " " + max_spverb +" "+max_thirdsingpres +" " + max_modal+ " be the " +max_cnum+ " " + max_plnoun + " " +before_the + " the " + after_the +"."

    print()
    print("I think ", textfilename," is about (according to the above statistics) :")
    print(summary)
    print("I might need to work a bit on my grammar.... :)")
    print()
    print("Let me try it again:")
    print("The most 'probable' 10 word sentence:(putting the most frequent word after the most probable start of sentence...)")
    print(create_sentence(word_list, start, 10))

    print("That might be a bit closer...")
    print()
    print("I have another method, let me show yout the most 'powerful' sentences: (the sentence from the book contaning the most of the most probable words)")
    sentence_list = create_sentence_list(create_string(rawtext))
    sentence_dict = create_sentence_dict(sentence_list)
    sentence_dict2 = dictionary_updater(sentence_dict, full_dict)
    print(max(sentence_dict2, key = sentence_dict2.get))


def analyse_sentiment( text_filename, positive_words_file_name = "positive-words.txt", negative_words_file_name = "negative-words.txt"):
    file = open(text_filename)
    rawtext = file.readlines()
    text = remove_newline(rawtext)
    word_list = []
    #print("Reading ", txtfile," ...")
    print()
    for line in text:
        word_list +=line.split()

    print("Wordcount of the book: ",len(word_list))

    book_dict = create_dict(word_list)

    poz_file = open(positive_words_file_name)
    poztext = poz_file.readlines()
    poz_word_list = []
    #2219
    for line in poztext:
        if not line.startswith(";"):
            poz_word_list +=line.split()

    print("Pozitive words in my dictionary: ",len(poz_word_list))
    #print(poz_word_list)

    neg_file = open(negative_words_file_name)
    negtext = neg_file.readlines()
    neg_word_list = []

    for line in negtext:
        if not line.startswith(";"):
            neg_word_list +=line.split()
    print("Negative words in my dictionary: ",len(neg_word_list))

    no_of_neg = 0
    no_of_poz = 0

    for n_word in neg_word_list:
        if n_word in book_dict:
            no_of_neg += book_dict[n_word]
    for p_word in poz_word_list:
        if p_word in book_dict:
            no_of_poz += book_dict[p_word]

    print()
    print("Negative : Positive ratio")
    print(no_of_neg," : ", no_of_poz)

def main():
    txtfile = "book.txt"
    stop_words = ["has","This","had","I","you","for","or","on","from","be","at","are","it","he","as","The","was","by","is","with","which","in","the","of","to","and","a","an","another","no","the","a","an","no","another","some","any","my","our","their","her","his","its","another","each","every","certain","its","another","this","that"]
    analyse_meaning(txtfile, stop_words)
    analyse_sentiment(txtfile)

if __name__ == '__main__':
    main()


