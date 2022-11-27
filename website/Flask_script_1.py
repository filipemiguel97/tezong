# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 01:56:47 2022

@author: João Araújo
"""
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

import pygame
from paddle import Paddle
from ball import Ball
from Player import Player


scoreA = 0
scoreB = 0
pygame.init()
size = (700, 500)
power_ups = {'Fireball' : 100, 'Lazers' : 100, 'Barricades' : 100}
player1 = Player(power_ups,'Mohith',(20,200))
player2 = Player(power_ups,'Filipe',(670  ,200 ))
WHITE = (255,255,255)
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195 
clock = pygame.time.Clock()

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
 
# Add the 2 paddles and the ball to the list of objects
all_sprites_list.add(player1.getPaddle())
all_sprites_list.add(player2.getPaddle())
all_sprites_list.add(ball)
# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def home():
	return render_template('index.html')

@app.route('/game')
def game():
	return render_template('game.html')

@app.route('/game', methods = ['POST'])
def user():
    if request.method == 'POST':
        #print('I got a POST')
        data = request.get_json()
        #data["1234"] = "334"
        #return jsonify(data)
        
        #Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B) 
        if data['player_hash'] == 'p1':
            if data['ArrowUp'] == True:
                player1.moveUp(5)
            if data['ArrowDown'] == True:
                player1.moveDown(5)
            if data['ArrowLeft']== True:
                player1.moveLeft(5)
            if data['ArrowRight']== True:
                player1.moveRight(5)
            
        elif data['player_hash'] == 'p2':
            if data['ArrowUp'] == True:
                player2.moveUp(5)
            if data['ArrowDown'] == True:
                player2.moveDown(5)
            if data['ArrowLeft']== True:
                player2.moveLeft(5)
            if data['ArrowRight']== True:
                player2.moveRight(5)
     
        # --- Game logic should go here
        all_sprites_list.update()
        
        #Check if the ball is bouncing against any of the 4 walls:
        score_p1 = data['score_p1']
        score_p2 = data['score_p2']
        if ball.rect.x>=690:
            ball.velocity[0] = -ball.velocity[0]
            score_p1 +=1
        if ball.rect.x<=0:
            ball.velocity[0] = -ball.velocity[0]
            score_p2 +=1
        if ball.rect.y>490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y<0:
            ball.velocity[1] = -ball.velocity[1]     
     
        #Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, player1.getPaddle()):
            ball.bounce(player1.getPaddle())
            player1.getPaddle().setFire(False)
        if pygame.sprite.collide_mask(ball, player2.getPaddle()):
            ball.bounce(player2.getPaddle())
            player2.getPaddle().setFire(False)

        player1.chargePowerups()
        
        if score_p1 > 9 or score_p2 >9:
            isover = True
            #print('over')
        else:
            isover = False
        
        return {'ball_x':ball.rect.x/700, 'ball_y': ball.rect.y/500, 'p1_x':player1.getPaddle().rect.x/700, 'p1_y':player1.getPaddle().rect.y/500,'p2_x': player2.getPaddle().rect.x/700, 'p2_y': player2.getPaddle().rect.y/500, 'score_p1': score_p1, 'score_p2': score_p2, 'isover': isover}


if __name__ == '__main__':
    app.run()
    print()
    
