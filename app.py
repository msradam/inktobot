from flask import Flask, render_template
from inktobot import get_svg_drawing
import os

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

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)