# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 01:56:47 2022

@author: João Araújo
"""
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def home():
	return render_template('index_copy.html')

@app.route('/game', methods = ['GET', 'POST', 'DELETE'])
def user():
    if request.method == 'POST':
        print('I got a POST')
        data = request.get_json()
        print(data)
        return jsonify({"ball_x": 0.5, "ball_y": 0.5, "p1_x": 0.1, "p1_y": 0.5, "p2_x": 0.8, "p2_y": 0.5, "score_p1": 0, "score_p2": 2})

    if request.method == 'GET':
        #data = request.form # a multidict containing POST data
        print('I got a GET')
        return "FAIL"

    # # if request.method == 'DELETE':
    # #     """delete user with ID <user_id>"""

    # # else:
    # #     # POST Error 405 Method Not Allowed
    # #     pass
    # # def postME():
    # data = request.get_json()
    # print(data)
    # data = jsonify(data)
    # return data


if __name__ == '__main__':
    app.run()
    
