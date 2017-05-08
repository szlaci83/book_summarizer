# Book summariser

Python program using my custom API in order to summarise a 
book using various algorithms to achive different level of
confidentiality.

The program is not using the nltk library for python, but 
the second version is coming using the above mentioned
poweful tool.

It has two main functions, one analises the meaning the other 
analiises the sentiment of the text.

# API endpoints:
 
## To get the available books:
* GET/books
* Returns the available books as a JSON object

## To got meaning analisys on a specific book:
* POST/meaning 
* Analyses the meaning of the book, and returns the result as a JSON object.
* request format: { "bookname" : "BOOK.txt"} format

## To get sentiment analisys on a specific book:
* POST/sentiment 
* Analyses the snetiment of the book, and returns the result as a JSON object.
* request format: { "bookname" : "BOOK.txt"} format

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

#Sources:
- Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
  Proceedings of the ACM SIGKDD International Conference on Knowledge 
  Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
  Washington, USA, (positive and negative words list) 
  
- The Astronomy of Milton's 'Paradise Lost' by Thomas Orchard
  Project Gutenberg @ www.gutenberg.org  (book.txt)