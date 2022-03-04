from flask import Flask, request, jsonify
from flask_restx import Api, Resource
from flask_cors import CORS #comment this on deployment
from werkzeug.exceptions import BadRequest
from werkzeug.datastructures import ImmutableMultiDict
from flask.json import JSONEncoder
# from sqlalchemy import create_engine, text
import db_config as db
# from deeplearning import DeepLearningHelper as helper
import base64
from io import BytesIO
import json
from history import loss, accuracy
# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt

app = Flask(__name__)

CORS(app) #comment this on deployment

api = Api(app)


@api.route('/i')
class test(Resource):
    def get(self):
        return {"hello":"react"}

@api.route('/register')
class test(Resource):
    def post(self):
        id, pw = request.json.get('email'), request.json.get('password')

        if db.info(id):
            raise BadRequest()
        db.insert(id, pw)

@api.route('/login')
class test2(Resource):
    def get(self):
        id = request.args.get("email")
        pw = request.args.get("password")
        
        if db.info(id) and db.info(id)[0]["password"] == pw:
            return True
        return BadRequest()

@api.route('/ts')
class test2(Resource):
    def get(self):
        return db.testinfo()
        

@api.route('/hist')
class test2123(Resource):
    def get(self):
        path = "react/mlweb/backend/deep_learning_models/TESTID_model_history.json"
        with open(path, 'r') as file:
            history = file.read()
        history = json.loads(history)
        img1, img2 = loss(history), accuracy(history)
        img_str1 = base64.b64encode(img1.getvalue())
        img_str1 = img_str1.decode('UTF-8')

        img_str2 = base64.b64encode(img2.getvalue())
        img_str2 = img_str2.decode('UTF-8')

        value = { "img1": img_str1, "img2": img_str2}
        return value


@api.route('/test')
class test2112(Resource):
    def post(self):
        # id = request.json.get('id')
        options = request.json.get('hyperParameters')
        epoch = options["epoch"]
        batch = options["batch"]
        learning_rate = options["learningRate"]

        print(options)
        # data = db.test()
        # deep_learning = helper(data)

        # deep_learning.set_hyper_parameters_option(batch, learning_rate, epoch)
        # deep_learning.preprocessing()

        # deep_learning.create_model()
        # deep_learning.training()
        # deep_learning.save("TESTID")
        del deep_learning

        return True


@api.route('/imgupload')
class test222(Resource):
    def post(self):
        for data in request.files.getlist("image[]"):
            img = BytesIO()
            data.save(img)
            img_str = base64.b64encode(img.getvalue())
            img_str = img_str.decode('UTF-8')
            db.img(data.filename, img_str)
            img.close()
            # return True

        # print(request.files.getlist("image[]")[0].filename )
        # print(request.form)
        # print(request.)

        # return BadRequest()
        return True

# 클라우드 서버 내 파일 목록 출력
@api.route('/imginfo')
class test21232(Resource):
    def get(self):
        return db.imginfo("test", "test")

# 이용중인 클라우드의 사용량 출력
@api.route('/diskinfo')
class test2123(Resource):
    def get(self):
        return db.diskinfo()

if __name__=="__main__":
    app.run(host="0.0.0.0", port="4000",debug=True, threaded=True)
    # app.run(port="3000", debug=True, threaded=True)
    # app.config['TEMPLATES_AUTO_RELOAD'] = True
    # app.run(host="127.0.0.1", port="5000", debug=True)


#     import os

# from flask 			import Flask, request
# from werkzeug.utils import secure_filename					# 1)

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = './profile_pictures'			# 2)

# @app.route('/profile-picture', methods=['POST'])
# def uplaod_profile_picture():
# 	if 'profile_pic' not in request.files:
#     	return 'File is missing', 404						# 3)
        
#     profile_pic = request.files['profile_pic']				# 4)
    
#     if profile_pic.filename = '':
#     	return 'File is missing', 404						# 5)
    
#     filename = secure_filename(profile_pic.filename)		# 6)
#     profile_pic.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))												   # 7)
    
#     return '', 200