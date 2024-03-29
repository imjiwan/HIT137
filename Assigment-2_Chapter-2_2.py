cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR ORFG ZNEVYLA ZBAEBR"
# Taking a cryptogram and a shift value as input and returning the decrypted text
def decrypt_cryptogram(cryptogram, shift):
    decrypted_text = ""

    for char in cryptogram:
        if char.isalpha():
            is_upper = char.isupper()   # Determine whether the character is uppercase or lowercase
            decrypted_char = chr((ord(char) - shift - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a')) # Apply the shift to the character and handle wrap-around
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # Keep non-alphabetic characters unchanged
    return decrypted_text

# Taking a cryptogram as input and iterating through all possible shift values (from 0 to 25) to find the one that gives the original quote
def find_shift_key(cryptogram):
    for shift in range(26):
        decrypted_text = decrypt_cryptogram(cryptogram, shift)
        print(f"Shift {shift}: {decrypted_text}")

# Find the shift key(s)
find_shift_key(cryptogram)

# The shift key is 13

# The original quote is : IM SELFISH IMPATIENT AND A LITTLE INSECURE I MAKE MISTAKES I AM OUT OF CONTROL ANDAT TIMES HARD TO HANDLE BUT IF YOU CANT HANDLE ME AT MY WORST THEN YOU SURE AS HELLDONT DESERVE ME BEST MARILYN MONROE