# import modules
import string
import random
import waitress
from flask import Flask, render_template, request, jsonify
import pyperclip

def generate_password(length, special_chars=True):
    # define the characters to be used in the password
    chars = string.ascii_letters + string.digits
    if special_chars:
        chars += string.punctuation

    # generate the password
    password = ''.join(random.choice(chars) for i in range(length))
    return password

# print(generate_password(11))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form.get('length', 12))
    use_special_chars = 'special_chars' in request.form
    password = generate_password(length, use_special_chars)
    return jsonify(password=password)

@app.route('/copy', methods=['POST'])
def copy():
    password = request.form.get('password', '')
    pyperclip.copy(password)
    return jsonify(message="Copied!")

if __name__ == '__main__':
    app.run(debug=True)


