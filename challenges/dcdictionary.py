#!/usr/bin/env python3
  
import argparse, socket
from datetime import datetime

dc= {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}




#answer= " "

#while answer != "q":
 # try:
  #  char_name= input("Which character do you want to know about? (Flash, Batman, Superman) ")

   # char_stat= input("What statistic do you want to know about? (strength, speed, or intelligence) ")

   # print(f"{char_name.capitalize()}'s {char_stat} is: {dc[char_name][char_stat].capitalize()}")
 # except:
  #  print("You surely don't know your superheros!")

 # answer= input("Press ENTER to choose another hero, or press Q to quit!").lower()
def printhero(heroinput, statinput):
    print(f'{heroinput.capitalize()}\'s {statinput} is: {str(heros[heroinput][statinput])}')

if __name__ == '__main__':
    people = {'flash': flash, 'batman': batman, 'superman': superman}
    stat= {'strength': strength, 'speed': speed, 'intelligence': intelligence}
    maker = argparse.ArgumentParser(description='finding strength and intelligence of your hero')
    maker.add_argument('-h', choices= people, help='which hero do you want to pick')
    maker.add_argument('-s', choices= stat, metavar='STAT', default='strength', help='what stat do you want to know about (default=strength)')

args =maker.parse_args()
function = people[args.hero]

printhero(-h, -s))
~                                                                                 
