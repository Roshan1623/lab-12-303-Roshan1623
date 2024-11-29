import time
from adafruit_circuitplayground import cp

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
    '0': '-----', ' ': ' '
}

def blink_dot():
    cp.pixels.fill((0, 0, 255))  # Blue for dot
    time.sleep(0.2)
    cp.pixels.fill((0, 0, 0))
    time.sleep(0.2)

def blink_dash():
    cp.pixels.fill((255, 0, 0))  # Red for dash
    time.sleep(0.6)
    cp.pixels.fill((0, 0, 0))
    time.sleep(0.2)

def text_to_morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
    return morse_code

def flash_morse(morse_code):
    for symbol in morse_code:
        for char in symbol:
            if char == '.':
                blink_dot()
            elif char == '-':
                blink_dash()
                
        time.sleep(0.6)
    
    time.sleep(1.2)


while True:
    text = input("Enter text to convert to Morse code (or 'quit' to exit): ")
    if text.lower() == 'quit':
        break
    morse_code = text_to_morse(text)
    print(f"Morse Code: {' '.join(morse_code)}")
    flash_morse(morse_code)

