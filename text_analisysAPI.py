from text_analyser import BookAnalyser
from flask import *

#available books to analyse
books = {
                'bible' : 'bible.txt',
                'stars' : 'stars.txt',
                'book'  : 'book.txt'
            }

sentiment = {
                'positive' : 'positive-words.txt',  #the file containing the positive words list for sentiment analysis
                'negative' : 'negative-words.txt'   #the file containing the negativ words list for sentiment analysis
            }

#return the available books
@app.route("/books", methods=['GET'])
def get_books():
    return jsonify(books)

#analise the meaning expecting : { "bookname" : "BOOK.txt"} format
@app.route("/meaning", methods=['POST', 'GET'])
def meaning():
    if not request.json or not 'bookname' in request.json:
        abort(4)
    bookname = request.json['bookname']
    response = BookAnalyser(bookname).analyse_meaning()

    return jsonify(response), 201


#analise the sentiment expecting : { "bookname" : "BOOK.txt"} format
@app.route("/sentiment", methods=['POST', 'GET'])
def sentiment():
    if not request.json or not 'bookname' in request.json:
        abort(4)
    bookname = request.json['bookname']
    response = BookAnalyser(bookname, sentiment['positive'], sentiment['negative']).analyse_sentiment()

    return jsonify(response), 201


if __name__ == "__main__":
    app.run(host='0.0.0.0')