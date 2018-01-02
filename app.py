from flask import Flask,request
import json
import yaml
from validator import validate
from rule import ValidationException

app = Flask(__name__)

RULES_FILE_NAME='rules.yml'

@app.route('/')
def hello_world():
    return 'Hello, Validator, CD pipeline test!'

@app.route('/validate', methods=['POST'])
def validate_endpoint():
    documents = request.get_json(force=True)
    rules = read_yaml_rules(RULES_FILE_NAME)
    try:
        validate(docs=documents, rule_definitions=rules)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    except ValidationException as e:
        return json.dumps({'success': False, 'msg': e.__str__()}), 500, {'ContentType': 'application/json'}



def read_yaml_rules(filename):
    with open(filename) as f:
        rules = yaml.load(f)
        return rules
