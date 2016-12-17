from crawlers.one337x import One337x
from flask import Flask, request, Response, render_template
from jsonpickle import encode
app = Flask(__name__)
app.secret_key = '\xb0\xf6\x86K\x0c d\x15\xfc\xdd\x96\xf5\t\xa5\xba\xfb6\x1am@\xb2r\x82\xc1'


@app.route('/')
def index():
    return render_template('index.html')
    # data = {"message": 'Welcome to osprey'}
    # json_str = encode(data, unpicklable=False)
    # return Response(json_str, mimetype='application/json')


@app.route('/search/<search_term>', methods=['GET'])
def search(search_term):
    crawler = One337x()
    torrents = list(crawler.fetch_torrents(search_term))
    json_str = encode(torrents, unpicklable=False)
    return Response(json_str, mimetype="application/json")


if __name__ == '__main__':
    crawler = One337x()
    torrents = list(crawler.fetch_torrents('designated'))
    json_string = encode(torrents[:2], unpicklable=False)
    print(json_string)
