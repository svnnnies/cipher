"""
encrypt.py
HIC-HomeWork4-Encrypt full name
using caesar cipher mehthod
"""
import random
import string

def caesar_encrypt(plaintext: str, shift: int) -> str:
    result = []
    for character in plaintext:
        if 'A' <= character <= 'Z': #test for upper
            base = ord('A')
            result.append(chr((ord(character) - base + shift) % 26 + base))
        elif 'a' <= character <= 'z': #for lower
            base = ord('a')
            result.append(chr((ord(character) - base + shift) % 26 + base))
        else:
            result.append(character)
    return ''.join(result)

def caesar_decrypt(ciphertext: str, shift: int) -> str:
    return caesar_encrypt(ciphertext, (-shift) % 26)

def main():
    plaintext = input("Enter your full name (plaintext): ").rstrip("\\n")
    secret_key = random.randint(1, 25)
    ciphertext = caesar_encrypt(plaintext, secret_key)
    print("\nEncrypted ciphertext (Caesar shift applied)")
    print(ciphertext)
    print("\nTry to guess the secret key (an integer between 1 and 25).")
    attempts = 0 #keeps track of how many attempts the user guessed it in
    while True:
        guess = input("Enter your guess (or type 'hint' for a hint, 'show' to show ciphertext again) (if hint is used it will weaken the security): ").strip().lower()
        attempts += 1 #updates the attempt for every wrong answer
        if guess == 'hint':
            half = "1-12" if secret_key <= 12 else "13-25"
            print(f"Hint: the secret key is in the range {half}. (This hint weakens security!)")
            continue
        if guess == 'show':
            print("Ciphertext:", ciphertext) #reshows the cipher text
            continue
        if not guess.isdigit():
            print("Please enter an integer between 1 and 25 (or 'hint'/'show').")
            continue
        g = int(guess)
        if g < 1 or g > 25:
            print("Key must be between 1 and 25.")
            continue
        if g == secret_key:
            print(f"Correct! The secret key is {secret_key}.")
            print("Decrypted plaintext:")
            print(caesar_decrypt(ciphertext, secret_key))
            print(f"You guessed it in {attempts} attempts.")
            break
        else:
            print("Incorrect key. Try again.")

if __name__ == '__main__':
    main()
