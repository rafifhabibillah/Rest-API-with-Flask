from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# inisiasi object flask
app = Flask(__name__)

# inisiasi object flask restful
api = Api(app)

# insisiasi object flask cors
CORS(app)

# inisiasi variabel kosong bertipe dictionary
identitas = {} #varable global

# membuat class resource
class ContohResource(Resource):
    # metode get dan post
    def get(self):
        #response = {"msg":"test flask api pertama"}
        return identitas

    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg" : "Data berhasil dimasukkan"}
        return response

# setup resource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)
