class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        # Validate inputs
        if not plain_text or not isinstance(plain_text, str):
            raise ValueError("Plain text must be a non-empty string")
        if not isinstance(num_rails, int) or num_rails < 1:
            raise ValueError("Number of rails must be a positive integer")
        if num_rails == 1:
            return plain_text  # If only 1 rail, no encryption needed

        # Initialize rails as a list of empty strings
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: down, -1: up

        # Distribute characters into rails
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Join characters in each rail and then join all rails
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Validate inputs
        if not cipher_text or not isinstance(cipher_text, str):
            raise ValueError("Cipher text must be a non-empty string")
        if not isinstance(num_rails, int) or num_rails < 1:
            raise ValueError("Number of rails must be a positive integer")
        if num_rails == 1:
            return cipher_text  # If only 1 rail, no decryption needed

        # Step 1: Determine the length of each rail
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Step 2: Distribute the cipher text into rails based on lengths
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length

        # Step 3: Reconstruct the plain text by following the zigzag pattern
        plain_text = ''
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index].pop(0)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return plain_text