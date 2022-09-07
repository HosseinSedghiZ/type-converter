# in the name of God

# ========================= Libraries ========================= #
# ========================= Varaibles ========================= #
# ========================= Methods ========================= #

class Converter:
    def __init__(self, chars:dict):
        self.chars = chars

    def to_persian(self, text): # ✔
        conv_text = ""

        for char in text:
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
    
    def to_english(self, text): # ✔
        conv_text = ""

        for char in text:
            for key, value in self.chars.items():
                if char == value:
                    conv_text += key
                    break

        return conv_text

# ========================= Main body ========================= #