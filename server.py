from flask import Flask, redirect, render_template, url_for, request, flash, Markup
from forms import URLForm
import os
from url_shortener import url_shortener, get_long_url

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=['POST', 'GET'])
def index():
    
    form = URLForm()
    if request.method == 'POST':
        short_url = url_shortener(form.url.data)
        link = f'<a href="{form.url.data}" class="copy-url" target="_blank">{short_url}</a>' 
        flash_msg = f"The shortened URL: {link}"
        flash(Markup(flash_msg))
        return redirect(url_for('index'))

    return render_template('index.html', form=form)

@app.route('/<url_code>')
def redirect_to_long_url(url_code):
    
    long_url = get_long_url(url_code)
    if long_url:
        return redirect(long_url)
    
    return redirect(url_for("error"))

@app.route('/error')
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)
