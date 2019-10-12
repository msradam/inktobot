from flask import Flask, render_template
from inktobot import get_svg_drawing

app = Flask(__name__)

@app.route('/')
def index(drawing=None, currentPrompt=None):
    try:
        drawing_and_prompt = get_svg_drawing()
        drawing, currentPrompt = drawing_and_prompt
    except:
        drawing = None
        currentPrompt = None
    return render_template('index.html', drawing=drawing, currentPrompt=currentPrompt)