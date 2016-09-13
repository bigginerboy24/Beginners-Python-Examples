# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:46:47 2016

@author: kilicm
"""

import time
import random
import sys

class Game():
    def __init__(self, name, health=5, energy = 100):
        self.name = name
        self.health = health
        self.energy = energy
        self.hit = 0
        
    def current_condition(self):
        print('Hit: ', self.hit)
        print('Energy: ', self.energy)
        print('Health: ', self.health)
        
    def attack(self, opponent):
        print('You perform an attack')
        print('Attack is in progress. Wait.')
        
        for i in range(10):
            time.sleep(.3)
            print('.', end='', flush=True)
        
        result = self.calculate_attack_result()
        
        if result == 0:
            print('\nResult: no one win')
            
        if result == 1:
            print('\nResult: You got punch from your opponent')
            self.punch(opponent)
        
        if result == 2:
            print('\nREsult: You punch from your opponent')
            self.punch(self)
            
    def calculate_attack_result(self):
        return random.randint(0, 2)
 
    def run_away(self):
        print('Running away...')
        for i in range(10):
            time.sleep(.3)
            print('\n', flush=True)
            
        print('Your opponent caught you')
        
       
    def punch(self, punched):
        punched.hit += 1
        punched.energy -= 1
        if (punched.hit % 5)== 0:
            punched.health -= 1
        if punched.health < 1:
            punched.energy = 0
            print('{} is the winner!'.format(self.name))
            self.exit_game()
            

    
    def exit_game(self):
        print('Exiting game..')
        sys.exit()
        
    
you = Game('MT')
opponent = Game('John')


while True:
    print('Currently, you are facing your opponent',
          'Move you want to make:',
          'Attack:    s',
          'Run away:  k',
          'Exit:      q', sep='\n')

    move = input('\n>')
    if move == 's':
        you.attack(opponent)
        
        print('Opponent condition')
        opponent.current_condition()
        
        print('Your condition')
        you.current_condition()
        
    if move == 'k':
        you.run_away()
        
    if move == 'q':
        you.exit_game()
        

