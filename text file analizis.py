from text_analyser import *

def preprocessing(textfilename):
    file = open(textfilename)
    rawtext = file.readlines()
    text = remove_newline(rawtext)
    word_list = []
    print()
    for line in text:
        word_list += line.split()
    return rawtext, word_list

def analyse_meaning( textfilename, list_of_words_to_omit = [], silent = False ):
    if not silent:
        print("This simple program attempts to summarise a book in a sentence.")

    rawtext, word_list = preprocessing(textfilename)

    wc = len(word_list)
    if not silent:
        print("Wordcount: ", wc)

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

    if not silent:
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
    before_not = most_freq_after(word_list, "not", -1)
    after_not = most_freq_after(word_list, "not")
    start = most_freq_start(word_list)
    end = most_freq_start(word_list, 0)
    summary = "The " + max_posnoun + " is/are " + max_gerund + " " + max_spverb + " " + max_thirdsingpres + " " + max_modal + " be the " + max_cnum + " " + max_plnoun + " " + before_the + " the " + after_the + "."
    sentence = create_sentence(word_list, start, 10)
    sentence_list = create_sentence_list(create_string(rawtext))
    sentence_dict = create_sentence_dict(sentence_list)
    sentence_dict2 = dictionary_updater(sentence_dict, full_dict)
    powerful = max(sentence_dict2, key=sentence_dict2.get)

    if not silent:
        print("in this textfile the most frequent word after: the is: ",after_the)
        print("in this textfile the most frequent word before: the is: ",before_the)
        print()
        print("in this textfile the most frequent word after: not is: ",after_not)
        print("in this textfile the most frequent word before: not is: ",before_not)
        print()
        print("Most freq. start of sentence:")
        print(start)
        print("Most freq. end of sentence:")
        print(end)
        print()
        print("I think ", textfilename," is about (according to the above statistics) :")
        print(summary)
        print("I might need to work a bit on my grammar.... :)")
        print()
        print("Let me try it again:")
        print("The most 'probable' 10 word sentence:(putting the most frequent word after the most probable start of sentence...)")
        print(sentence)
        print("That might be a bit closer...")
        print()
        print("I have another method, let me show yout the most 'powerful' sentences: (the sentence from the book contaning the most of the most probable words)")
        print(powerful)


def analyse_sentiment( textfilename, positive_words_file_name = "positive-words.txt", negative_words_file_name = "negative-words.txt", silent = False):
    _, word_list = preprocessing(textfilename)
    wc = len(word_list)
    book_dict = create_dict(word_list)

    _, poz_word_list = preprocessing(positive_words_file_name)
    _, neg_word_list = preprocessing(negative_words_file_name)

    no_of_neg = 0
    no_of_poz = 0

    for n_word in neg_word_list:
        if n_word in book_dict:
            no_of_neg += book_dict[n_word]
    for p_word in poz_word_list:
        if p_word in book_dict:
            no_of_poz += book_dict[p_word]

    if not  silent:
        print("Wordcount of the book: ", wc)
        print("Pozitive words in my dictionary: ",len(poz_word_list))
        print("Negative words in my dictionary: ", len(neg_word_list))
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