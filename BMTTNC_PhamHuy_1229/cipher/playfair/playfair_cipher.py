class PlayFairCipher:
    def __init__(self) -> None:
        pass

    def init(self):
        pass

    def create_playfair_matrix(self, key):
        # Replace 'J' with 'I' in the key (Playfair standard)
        key = key.upper().replace('J', 'I')
        key_set = set(key)

        # Define the alphabet (excluding J, since J is replaced by I)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        # Create the initial matrix with unique letters from key
        remaining_letters = [letter for letter in alphabet if letter not in key_set]
        matrix = list(key)

        # Add remaining letters to the matrix until it has 25 letters (5x5 grid)
        for letter in remaining_letters:
            matrix.append(letter)
            if len(matrix) == 25:
                break

        # Convert the flat list into a 5x5 matrix
        playfair_matrix = [matrix[i:i + 5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        # Find the coordinates (row, col) of a letter in the matrix
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return None  # Should never happen with a valid matrix

    def playfair_encrypt(self, plain_text, matrix):
        # Prepare plain text: convert to uppercase, replace J with I, remove non-letters
        plain_text = plain_text.upper().replace('J', 'I')
        # Remove non-letters and keep only valid characters
        plain_text = ''.join(c for c in plain_text if c in 'ABCDEFGHIKLMNOPQRSTUVWXYZ')
        encrypted_text = ""

        # Process the text in pairs
        i = 0
        while i < len(plain_text):
            # Get the pair of letters
            if i + 1 >= len(plain_text):
                # If the last character is alone, append 'X'
                pair = plain_text[i] + 'X'
                i += 1
            else:
                pair = plain_text[i:i + 2]
                i += 2

            # If the pair has identical letters, insert 'X' and reprocess
            if pair[0] == pair[1]:
                pair = pair[0] + 'X'
                i -= 1  # Reprocess the second letter in the next iteration

            # Find the coordinates of each letter in the pair
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            # Apply Playfair cipher rules
            if row1 == row2:
                # Same row: shift right (wrap around using modulo)
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                # Same column: shift down (wrap around using modulo)
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:
                # Rectangle: swap columns
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        # Prepare cipher text: convert to uppercase, replace J with I
        cipher_text = cipher_text.upper().replace('J', 'I')
        decrypted_text = ""

        # Process the text in pairs
        for i in range(0, len(cipher_text), 2):
            # Get the pair of letters
            pair = cipher_text[i:i + 2]
            # Find the coordinates of each letter in the pair
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            # Apply Playfair cipher rules for decryption
            if row1 == row2:
                # Same row: shift left (wrap around using modulo)
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                # Same column: shift up (wrap around using modulo)
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:
                # Rectangle: swap columns
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        # Clean up the decrypted text by removing filler 'X' characters
        i = 0
        result = ""
        while i < len(decrypted_text):
            if i + 2 < len(decrypted_text) and decrypted_text[i + 1] == 'X' and decrypted_text[i] == decrypted_text[i + 2]:
                result += decrypted_text[i]
                i += 2  # Skip the 'X' and the repeated letter
            else:
                result += decrypted_text[i]
                i += 1

        # Handle edge cases for remaining 'X' at the end
        if len(result) >= 2 and result[-1] == 'X':
            result = result[:-1]

        return result