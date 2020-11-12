import flask
import pafy

from flask import Flask, request, jsonify, url_for, abort, render_template
from flask_ngrok import run_with_ngrok
from threading import Timer

app = Flask(__name__)
app.config["DEBUG"] = True
#run_with_ngrok(app)  # Start ngrok when app is run

# Create some test data for our catalog in the form of a list of dictionaries.
# books = [
#     {'id': 0,
#      'title': 'A Fire Upon the Deep',
#      'author': 'Vernor Vinge',
#      'first_sentence': 'The coldsleep itself was dreamless.',
#      'year_published': '1992'},
#     {'id': 1,
#      'title': 'The Ones Who Walk Away From Omelas',
#      'author': 'Ursula K. Le Guin',
#      'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
#      'published': '1973'},
#     {'id': 2,
#      'title': 'Dhalgren',
#      'author': 'Samuel R. Delany',
#      'first_sentence': 'to wound the autumnal city.',
#      'published': '1975'}
# ]


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


# A route to return all of the available entries in our catalog.
# @app.route('/api/v1/resources/books/all', methods=['GET'])
# def api_all():
#     return jsonify(books)

@app.route('/api/v1/download', methods=['POST'])
def download():
    content = request.get_json(force=True)
    ip = request.remote_addr

    vUrl = content['url']
    vType = content['type']
    server_path = './static/' + vType

    if (vType != "video" and vType != "audio"):
        abort(404)

    v = pafy.new(vUrl)

    #logger
    with open('log.txt', 'a') as the_file:
        the_file.write('{0} {1} {2} {3}\n'.format(ip, vType, vUrl, v.title))

    path = 'error'
    if (vType == "video"):
        v.getbest().download(server_path)
        path = v.title + '.mp4'
    else:
        v.getbestaudio('m4a').download(server_path)
        path = v.title + '.m4a'

    return url_for('static', filename = vType + '/' + path)

if __name__ == '__main__':
    app.run(port=3176, debug=True)
    #app.run()

#Steps to put it online:
# 1. lt --port 3176 --subdomain zachan0001
# 2. NameCheap redirect
# 3. python main.py