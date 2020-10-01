#!/usr/bin/env

import wget

def wget_pic(imagelink):
   # name =imagelink.split('/')[-1] #splits file in list so name is xxx.png  from Didi
    wget.download(imagelink, '/home/student/static/') # + name) 
    




def main()
    link = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png'
    wget_pic(link)

#if __name__ == "__main__":
 #   main()



    # code goes here!
    # image must be saved to /home/student/mycode
