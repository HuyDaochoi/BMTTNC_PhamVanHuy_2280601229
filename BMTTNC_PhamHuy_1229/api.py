from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

# VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

# RAIL FENCE CIPHER ALGORITHM
rail_fence_cipher = RailFenceCipher()

# PLAYFAIR CIPHER ALGORITHM
playfair_cipher = PlayFairCipher()

# TRANSPOSITION CIPHER ALGORITHM
transposition_cipher = TranspositionCipher()

# Caesar Cipher Endpoints
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.get_json()
    plain_text = data["plain_text"]
    key = int(data["key"])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({"encrypted_message": encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.get_json()
    cipher_text = data["cipher_text"]
    key = int(data["key"])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({"decrypted_message": decrypted_text})

# Vigenere Cipher Endpoints
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.get_json()
    plain_text = data["plain_text"]
    key = data["key"]
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.get_json()
    cipher_text = data["cipher_text"]
    key = data["key"]
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({"decrypted_text": decrypted_text})

# Rail Fence Cipher Endpoints
@app.route("/api/railfence/encrypt", methods=["POST"])
def rail_fence_encrypt():
    data = request.get_json()
    plain_text = data["plain_text"]
    key = int(data["key"])
    encrypted_text = rail_fence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})

@app.route("/api/railfence/decrypt", methods=["POST"])
def rail_fence_decrypt():
    data = request.get_json()
    cipher_text = data["cipher_text"]
    key = int(data["key"])
    decrypted_text = rail_fence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({"decrypted_text": decrypted_text})

# Playfair Cipher Endpoints
@app.route("/api/playfair/creatematrix", methods=["POST"])
def playfair_creatematrix():
    data = request.get_json()
    key = data["key"]
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})

@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    data = request.get_json()
    plain_text = data["plain_text"]
    key = data["key"]
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, matrix)
    return jsonify({"encrypted_text": encrypted_text})

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    data = request.get_json()
    cipher_text = data["cipher_text"]
    key = data["key"]
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, matrix)
    return jsonify({"decrypted_text": decrypted_text})

# Transposition Cipher Endpoints
@app.route("/api/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get("plain_text")
    key = int(data.get("key"))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})

@app.route("/api/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get("cipher_text")
    key = int(data.get("key"))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({"decrypted_text": decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)