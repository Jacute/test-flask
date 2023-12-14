from app import app
from flask import render_template, request


@app.route('/', methods=['GET'])
def index():
    name = request.args.get('name')
    xss = request.args.get('checkbox')
    
    return render_template('index.html', name=name, xss=xss)
