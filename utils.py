import os
from flask import send_from_directory, abort
import pymongo
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename

__author__ = 'alexandreferreira'

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
MEDIA_ROOT = os.path.join(ROOT_PATH, "media")
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def connect_mongo():
    connection = pymongo.MongoClient("localhost")
    db = connection.tata
    return db


def get_params(request):
    info = {}
    if request.method == 'GET':
        for key, value in request.args.lists():
            info[key] = value[0]
    else:
        for key, value in request.form.lists():
            info[key] = value[0]
    if request.files:
        info['post_file'] = {}
        for key, value in request.files.lists():
            info['post_file'][key] = value[0]
    return info


import json


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def save_file(file_image):
    if file and allowed_file(file_image.filename):
        filename = secure_filename(file_image.filename)
        file_image.save('%s/%s' % (MEDIA_ROOT, str(filename)))
        return filename
    else:
        abort(500)


def get_image(file_name):
    return send_from_directory(MEDIA_ROOT,
                                    file_name)