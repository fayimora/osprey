from crawlers.one337x import One337x
from flask import Flask, request, Response, render_template
from flask_cors import CORS, cross_origin
from jsonpickle import encode
from opbeat.contrib.flask import Opbeat

app = Flask(__name__, template_folder='static', static_folder='static')
app.secret_key = '\xb0\xf6\x86K\x0c d\x15\xfc\xdd\x96\xf5\t\xa5\xba\xfb6\x1am@\xb2r\x82\xc1'

CORS(app)

opbeat = Opbeat(
    app,
    organization_id='02f5f35ab2ff4076a4cb9cf1614e5dc0',
    app_id='00aa53c50c',
    secret_token='44954c630c0a6f6438dc4fb211533fc622ba64b4',
)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/<search_term>', methods=['GET'])
def search(search_term):
    crawler = One337x()
    torrents = list(crawler.fetch_torrents(search_term))
    json_str = encode(torrents, unpicklable=False)
    return Response(json_str, mimetype="application/json")


if __name__ == '__main__':
    app.run(port=8090)
#     crawler = One337x()
#     torrents = list(crawler.fetch_torrents('designated'))
#     json_string = encode(torrents[:2], unpicklable=False)
#     print(json_string)
