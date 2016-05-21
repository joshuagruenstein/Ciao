#!/usr/bin/python

import json
from flask import Flask, request

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/getPosts/<int:posts>', methods=['GET'])
def getPosts(posts):
	with open("posts.txt","r") as f:
		lines = f.readlines()

	return json.dumps(lines[len(lines)-posts:], ensure_ascii=False)

@app.route('/post/<postContent>', methods=['POST'])
def post(postContent):
	with open("posts.txt","a") as f:
		f.write("\n"+postContent)

	return 'ok'

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port=9990,debug=True)
