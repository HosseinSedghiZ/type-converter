# in the name of God

# ========================= Libraries ========================= #
# ========================= Varaibles ========================= #
# ========================= Methods ========================= #

class Converter:
    def __init__(self, chars:dict, text:str):
        self.chars = chars
        self.text = text

    def convert_english_to_persian(self): # ✔
        conv_text = ""

        for char in self.text:
            for key, value in self.chars.items():
                if char == "H":
                    if char == key:
                        conv_text += value
                        break
                else:
                    if char.lower() == key:
                        conv_text += value
                        break

        return conv_text
    
    def convert_persian_to_english(self): # ✔
        conv_text = ""

        for char in self.text:
            for key, value in self.chars.items():
                if char == value:
                    conv_text += key
                    break

        return conv_text

# ========================= Main body ========================= #