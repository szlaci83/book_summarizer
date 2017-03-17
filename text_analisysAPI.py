from text_analyser import BookAnalyser
from flask import *

#return the available currencies
@app.route("/books", methods=['GET'])
def get_books():
    return jsonify(text_analyser.books)


#expecting : { "bookname" : "BOOK.txt"} format
@app.route("/meaning", methods=['POST', 'GET'])
def meaning():
    if not request.json or not 'bookname' in request.json:
        abort(4)
    bookname = request.json['bookname']
    response = BookAnalyser(bookname, "positive-words.txt", "negative-words.txt").analyse_sentiment()

    return jsonify(response), 201



#expecting : { "bookname" : "BOOK.txt"} format
@app.route("/sentiment", methods=['POST', 'GET'])
def sentiment():
    if not request.json or not 'bookname' in request.json:
        abort(4)
    bookname = request.json['bookname']
    response = 'call the right function to get response'

    return jsonify(response), 201


if __name__ == "__main__":
    app.run(host='0.0.0.0')