def decodeMorse(morse_code):
    """
    Input: String -> String
    produces ASCII characters based on morse code string
    """
    MORSE_CODE = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', 
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', 
        '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', 
        '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', 
        '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
    }
    
    decodedMorse = ''
    morse = morse_code.split(' ')
    for code in morse:
        if MORSE_CODE.get(code, '0') != '0':
           decodedMorse += MORSE_CODE[code]
        else:
           decodedMorse += ' '
    
    finalDecoded = decodedMorse.strip()
    return finalDecoded.replace('  ', ' ')


#Test
print("Expected result:", 'HEY JUDE')
print("Actual result:", decodeMorse('.... . -.--   .--- ..- -.. .'))
print("Expected result:", 'E')
print("Actual result:", decodeMorse(' . '))