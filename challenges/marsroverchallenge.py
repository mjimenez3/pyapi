#!/usr/bin/python3

import requests


def main():
    r = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY").json()
    


    for pics in r["photos"]:
        #hard
        #print(pics["img_src"])
        
        #harder
#        print(pics["rover"]["name"])
#        print(f"Rover: {pics['rover']['name']}")
#        print(f"Date: {pics['earth_date']}")
#        print(f"Link: {pics['img_src']}")
        
        #hardest
        cam = input("Which Camera FHAZ, RHAZ, MAST, CHEMCAM, or NAVCAM?").upper(o)

        if pics["camera"]["name"] == cam:
            print(f"Rover: {pics['rover']['name']}")
            print(f"Date: {pics['earth_date']}")
            print(f"Camera: {pics['camera']['name']}")
            print(f"Link: {pics['img_src']}")



if __name__ == "__main__":
    main()
