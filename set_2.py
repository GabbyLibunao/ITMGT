def shift_letter(letter, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    location = alphabet.find(letter) + shift
    if location > 25:
        location = location % 26
    final_letter = alphabet[location]
    if letter == " ":
        final_letter = " "
    return(final_letter)

def caesar_cipher(message, shift):
    final_message = ""
    for x in range(0, len(message)):
        letter = message[x]
        shifted_letter = shift_letter(letter, shift)
        final_message = final_message + shifted_letter
    return(final_message)

def shift_by_letter(letter, letter_shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shift_value = alphabet.find(letter_shift)
    return(shift_letter(letter, shift_value))
           
def vigenere_cipher(message, key):
    key_index = 0
    final_message = ""
    for i in range(0, len(message)):
        letter = message[i]
        if key_index >= len(key):
            key_letter = key[key_index % len(key)]
        else:
            key_letter = key[key_index]
        key_index += 1
        shifted_letter = shift_by_letter(letter, key_letter)
        final_message = final_message + shifted_letter
    return(final_message)

def scytale_cipher(message, shift):
    if len(message)%shift != 0:
        x = 0
        while x == 0:
            message = message + "_"
            if len(message)%shift == 0:
                x = 1
    new_shift = len(message)/shift
    new_message = ""
    for i in range(0, len(message)):
        new_location = i*new_shift
        new_message = new_message + message[int(new_location - int(new_location/len(message))*len(message) + int(new_location/len(message)))]
    return(new_message)

def scytale_decipher(message, shift):
    new_message = ""
    for i in range(0, len(message)):
        new_location = i*shift
        if new_location >= len(message):
            new_location = new_location % len(message) + 1*int(new_location/len(message))
        new_message = new_message + message[new_location]
    return(new_message)



        


        

