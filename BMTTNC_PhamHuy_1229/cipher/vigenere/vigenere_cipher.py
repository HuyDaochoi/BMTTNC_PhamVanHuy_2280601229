class VigenereCipher:
    def vigenere_encrypt(self, plain_text, key):
        # Validate inputs
        if not plain_text or not isinstance(plain_text, str):
            raise ValueError("Plain text must be a non-empty string")
        if not key or not isinstance(key, str):
            raise ValueError("Key must be a non-empty string")
        if not any(c.isalpha() for c in key):
            raise ValueError("Key must contain at least one letter")

        encrypted_text = ""
        key_index = 0

        for char in plain_text:
            if char.isalpha():
                # Get the shift value from the key (key is case-insensitive)
                key_char = key[key_index % len(key)].upper()
                key_shift = ord(key_char) - ord('A')

                # Encrypt the character while preserving case
                if char.isupper():
                    encrypted_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                else:
                    encrypted_text += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))

                key_index += 1
            else:
                # Keep non-alphabetic characters unchanged
                encrypted_text += char

        return encrypted_text

    def vigenere_decrypt(self, encrypted_text, key):
        # Validate inputs
        if not encrypted_text or not isinstance(encrypted_text, str):
            raise ValueError("Encrypted text must be a non-empty string")
        if not key or not isinstance(key, str):
            raise ValueError("Key must be a non-empty string")
        if not any(c.isalpha() for c in key):
            raise ValueError("Key must contain at least one letter")

        decrypted_text = ""
        key_index = 0

        for char in encrypted_text:
            if char.isalpha():
                # Get the shift value from the key (key is case-insensitive)
                key_char = key[key_index % len(key)].upper()
                key_shift = ord(key_char) - ord('A')

                # Decrypt the character while preserving case
                if char.isupper():
                    decrypted_text += chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
                else:
                    decrypted_text += chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))

                key_index += 1
            else:
                # Keep non-alphabetic characters unchanged
                decrypted_text += char

        return decrypted_text