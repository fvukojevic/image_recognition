from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource
import requests
import subprocess
import json

app = Flask(__name__)
api = Api(app)

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'
    response.headers['Access-Control-Expose-Headers'] = '*'
    return response

class Classify(Resource):
    def post(self):
        data = request.get_json()

        url = data['url']
        r = requests.get(url)
        with open('temp.jpg', "wb") as f:
            f.write(r.content)
            process = subprocess.Popen(['python classify_image.py --model_dir=. --image_file=./temp.jpg'], shell=True)
            process.communicate()[0]
            process.wait()
            with open("response.txt") as g:
                res = json.load(g)

        return make_response(jsonify(res), 200)


api.add_resource(Classify, '/classify')

if __name__ == "__main__":
    app.run(host='0.0.0.0')