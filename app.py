import json
from flask import Flask, render_template, request
from pyMap import process_latlng

app = Flask(__name__)

DICT = {
    "高德影像": "gaode.image",
    "天地图影像": "tianditusat",
    "esrisat": "gaode.image",
    "MapQuest影像": "gaode.image",
    "谷歌影像": "gaode.image",
}

@app.route('/')
def index():
    app.logger.debug("index")
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    form = request.form
    name = str(form.get('name'))
    mtype = str(form.get('type'))
    bound = str(form.get('bound'))
    zoom = int(form.get('zoom'))
    bounds = bound.split(',')
    bounds = list(map(float, bounds))
    process_latlng(bounds[0], bounds[1], bounds[2], bounds[3], zoom, name, DICT[mtype])
    return "success"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
