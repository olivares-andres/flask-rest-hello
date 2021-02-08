from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import CORS
from models import db
from myQueue import Queue
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
CORS(app)
Migrate(app,db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

_queue = Queue()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/new', methods= ['POST'])
def new_e():
    if not request.is_json:
        return jsonify({"msg": "No JSON return"}), 400
    
    name = request.json.get('name', None)
    phone = request.json.get('phone', None)
    
    if not name or name == '':
        return jsonify({"msg": "No name in request"}), 400
    if not phone or phone == '':    
        return jsonify({"msg": "No phone in request"}), 400   
    
    element = {
        "name": name,
        "phone": phone
    }
    
    result = _queue.enqueue(element)    
    return jsonify({"msg": "user added", "result": result}), 200

@app.route('/next', methods = ['DELETE'])
def next_e():
    result = _queue.dequeue()    
    return jsonify({"msg": "user deleted", "result": result}), 200
    
@app.route('/all')
def all_e():
    users = _queue.get_queue()
    return jsonify(users),200




if __name__ == '__main__':
    manager.run()
