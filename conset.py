# in the name of God

# ========================= Libraries ========================= #
from converter import Converter
# ========================= Varaibles ========================= #
chars = {
    'a' : 'ش',
    'b' : 'ذ',
    'c' : 'ز',
    'd' : 'ی',
    'e' : 'ث',
    'f' : 'ب',
    'g' : 'ل',
    'h' : 'ا',
    'H' : 'آ',
    'i' : 'ه',
    'j' : 'ت',
    'k' : 'ن',
    'l' : 'م',
    'm' : 'ئ',
    'n' : 'د',
    'o' : 'خ',
    'p' : 'ح',
    'q' : 'ض',
    'r' : 'ق',
    's' : 'س',
    't' : 'ف',
    'u' : 'ع',
    'v' : 'ر',
    'w' : 'ص',
    'x' : 'ط',
    'y' : 'و',
    'z' : 'ظ',
    ',' : 'و',
    '[' : 'ج',
    ']' : 'چ',
    ';' : 'ک',
    "'" : 'گ',
    ' ' : ' ',
}

# ========================= Methods ========================= #

text = "Hf o,F hSj"

if __name__ == "__main__":
    con = Converter(chars, text)

    # converted_text = con.convert_english_to_persian() ✔
    converted_text = con.convert_english_to_persian()
    # converted_text = con.convert_persian_to_english()
    
    print(converted_text)