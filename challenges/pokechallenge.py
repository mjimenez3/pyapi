#!/usr/bin/env python3

import requests

def api_pull():
    choice= input("What Pokemon would you like a picture of? ")
    
        
 
    p = 'https://pokeapi.co/api/v2/pokemon/'
    
    o = p + choice

    k = requests.get(o).json()
    return(k)



#    return pokedict # the value of pokedict is the translated JSON returned from a valid url concatenated with user input!






#if __name__ == "__main__":
    
