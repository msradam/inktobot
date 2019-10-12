import os
from datetime import datetime
import random
import requests
from dotenv import load_dotenv
from requests_oauthlib import OAuth1

load_dotenv()

prompts = [
    "ring", "mindless", "bait", "freeze", "build", "husky", "enchanted", 
    "frail", "swing", "pattern", "snow", "dragon", "ash", "overgrown",
    "legend", "wild", "ornament", "misfit", "sling", "tread", "treasure", 
    "ghost", "ancient", "dizzy", "tasty", "dark", "coat", "ride", 
    "injured", "catch", "ripe"
    ]

def get_svg_drawing():
    '''
    Retrieves an SVG drawing from the Noun Project icon collection
    with the current Inktober prompt as a search term
    
    Returns: A string representing an SVG object
    '''
    currentPrompt = random.choice(prompts)

    endpoint =  'http://api.thenounproject.com/icons/{}?limit_to_public_domain=1&limit=200'.format(currentPrompt)

    auth = OAuth1(os.getenv("API_KEY"), os.getenv("API_SECRET"))
    
    try:
        response = requests.get(endpoint, auth=auth)
        response_dict = dict(response.json())

        drawing_urls = [ icon['icon_url'] for icon in response_dict['icons'] if 'icon_url' in icon.keys() ]

        random_url = random.choice(drawing_urls)

        svg_response = (requests.get(random_url)).text
        
        scaled_svg = svg_response[:4] + ' x="0px" y="0px" width="500px" height="500px" xml:space="preserve"' + svg_response[4:]

        return (scaled_svg, currentPrompt.capitalize())
    except: 
        None
