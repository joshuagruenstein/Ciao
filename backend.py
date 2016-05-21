#!/usr/bin/python

import json
from flask import Flask, request

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/post/<int:posts>', methods=['GET'])
def getPosts(posts):
	with open("posts.txt","r") as f:
		lines = f.readlines()

	return json.dumps(lines[len(lines)-posts:], ensure_ascii=False)

@app.route('/post', methods=['POST'])
def post():
	contents = request.get_data().decode('iso-8859-1')
	print("Contents: " + contents)
	with open("posts.txt","a") as f:
		f.write("\n"+contents)

	return 'ok'

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port=9990,debug=True)
