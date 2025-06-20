from flask import Flask, render_template, request, json

from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

# Router routes for caesar cipher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

# Router routes for vigenere cipher
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

# Router routes for rail fence cipher
@app.route("/railfence")
def rail_fence():
    return render_template('railfence.html')

# Router routes for playfair cipher
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

# Router routes for transposition cipher
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

# Caesar Cipher Endpoints
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

# Vigenere Cipher Endpoints
@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']  # Key là chuỗi cho Vigenère
    vigenere = VigenereCipher()
    encrypted_text = vigenere.vigenere_encrypt(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vigenere = VigenereCipher()
    decrypted_text = vigenere.vigenere_decrypt(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

# Rail Fence Cipher Endpoints
@app.route("/railfence/encrypt", methods=['POST'])
def rail_fence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    rail_fence = RailFenceCipher()
    encrypted_text = rail_fence.rail_fence_encrypt(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def rail_fence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    rail_fence = RailFenceCipher()
    decrypted_text = rail_fence.rail_fence_decrypt(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

# Playfair Cipher Endpoints
@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']  # Key là chuỗi cho Playfair
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_encrypt(text, matrix)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    decrypted_text = playfair.playfair_decrypt(text, matrix)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

# Transposition Cipher Endpoints
@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    transposition = TranspositionCipher()
    encrypted_text = transposition.encrypt(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    transposition = TranspositionCipher()
    decrypted_text = transposition.decrypt(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)