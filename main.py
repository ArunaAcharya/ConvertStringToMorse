print('This program is created to translate string to Morse code')


to_continue= True
Morse_dict={
'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----'
}
def translate(words):
    return "".join(Morse_dict[char] for char in words)

while to_continue:
    words = input("Enter a word or phrase").upper()
    try:
        print(translate(words))
    except KeyError:
        print("The word or phrase you have provided contains invalid characters. Please try again")
    still_want_to_continue= input("Do you want to try any other word or pharse? Type 'YES' or 'NO':\n ").upper()
    if still_want_to_continue =='NO':
        to_continue= False






