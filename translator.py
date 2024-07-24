# Mapping dictionary for simple Latin to Hangul conversion
latin_to_hangul = {
    'a': '아', 'b': '비', 'c': '시', 'd': '디', 'e': '이', 'f': '에프',
    'g': '지', 'h': '에이치', 'i': '아이', 'j': '제이', 'k': '케이', 'l': '엘',
    'm': '엠', 'n': '엔', 'o': '오', 'p': '피', 'q': '큐', 'r': '알',
    's': '에스', 't': '티', 'u': '유', 'v': '브이', 'w': '더블유', 'x': '엑스',
    'y': '와이', 'z': '제트', 'A': '아', 'B': '비', 'C': '시', 'D': '디', 
    'E': '이', 'F': '에프', 'G': '지', 'H': '에이치', 'I': '아이', 'J': '제이', 
    'K': '케이', 'L': '엘', 'M': '엠', 'N': '엔', 'O': '오', 'P': '피', 
    'Q': '큐', 'R': '알', 'S': '에스', 'T': '티', 'U': '유', 'V': '브이', 
    'W': '더블유', 'X': '엑스', 'Y': '와이', 'Z': '제트'
}

def translate_to_hangul(name):
    translated_name = ""
    for letter in name:
        translated_name += latin_to_hangul.get(letter, letter)
    return translated_name


user_input = input("Enter your name: ")

translate_to_korean = input("Do you want to translate the name to Korean letters? (yes/no): ").strip().lower()

if translate_to_korean == 'yes':
    print("Korean Translation:", translate_to_hangul(user_input))
else:
    print("Goodbye")


