# Book summariser

Python program trying to summarise a book using various 
algorithms to achive different level of confidentiality.

The program is not using the nltk library for python, but 
the second version is coming using the above mentioned
poweful tool.

It has two main functions, one analises the meaning the other 
analiises the sentiment of the text.

#How it works:

#The meaning analiser: 

- Reads in the book as textfile
- separates words into word classes using regexes
- finds the most frequent of each class
- Identifies the most frequent word after and before "the", "not"
- Identifies the most frequent start and end of sentence.
- Tries to create sentences using the above classified words.

#The sentiment analiser:

- Reads in the book
- reads in the positive and negative words in two dictionaries
- counts each classes
- prints the ratio of negative : positive words
