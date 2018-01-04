export FLASK_DEBUG=1
export FLASK_APP=app.py
export RULES_JSON="{\"first_name_not_null\":{\"type\":\"not_null\",\"fields\":[\"first_name\"]},\"age_cant_be_missing\":{\"type\":\"missing\",\"fields\":[\"age\"]}}"
flask run
