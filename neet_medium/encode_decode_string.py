from typing import List

class BruteEncodeDecode:
    #switch to using non-ascii with char(257) then add the number of characters to help speed up decoding

    def encode(self, strs: List[str]) -> str:
        encoded_text = ""
        for index, s in enumerate(strs):
            if s == "":
                encoded_text = encoded_text + "%E"
            else:
                for index in range(len(s)):
                    if s[index] == "|":
                        encoded_text = encoded_text + "%|"
                    elif s[index] == "%" :
                        encoded_text = encoded_text + "%%"
                    else:
                        encoded_text = encoded_text + s[index]
                    if index == len(s) -1 and index < len(s):
                        encoded_text = encoded_text + "|"


        return encoded_text

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        char_cache:List[str] = []
        for index in range(len(s)):
            char_cache.append(s[index])
            if len(char_cache) > 1:
                if char_cache[len(char_cache) -2] == "%":
                    if char_cache[len(char_cache) -1] == "E":
                        char_cache = []
                        decoded_list.append("")
                    elif char_cache[len(char_cache) -1] in ["|", "%"]:
                        char_cache.pop(len(char_cache) -2)
                elif char_cache[len(char_cache) -1] == "|":
                    char_cache.pop(len(char_cache) -1)
                    decoded_list.append("".join(char_cache))
                    char_cache = []
            if index == len(s) -1 and len(char_cache) > 0:
                decoded_list.append("".join(char_cache))
        return decoded_list

class NonAsciiEncodeDecode:
    #switch to using non-ascii with char(257) then add the number of characters to help speed up decoding

    def encode(self, strs: List[str]) -> str:
        separator = chr(257)
        notated_strs = [f'{s}{separator}' for s in strs ]

        encoded_string = "".join(notated_strs)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        separator = chr(257)
        decoded_list:List[str] = s.split(separator)
        decoded_list.pop()
        return  decoded_list

class OptimalSolution:
    def encode(self, strs: List[str]) -> str:
        notated_strs = [f'{len(s)}{s}' for s in strs]
        encoded_string = "".join(notated_strs)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        # Think about changing to a slice rather than iteration

        if not s:
            return []
        string_builder:List[str] = []
        decoded_list:List[str] = []
        counter = int(s[0])
        for i in range(len(s) +1):
            if counter == -1:
                string_builder.pop(0)
                decoded_list.append("".join(string_builder))
                string_builder = []
                if i < len(s):
                    counter = int(s[i])
                    string_builder.append(s[i])
            elif i < len(s):
                string_builder.append(s[i])
            counter -= 1

        return decoded_list


if __name__ == "__main__":
    reg_input = ["Hel%lo", "Wor|ld"]
    test_input = ["we","say",":","yes","!@#$%^&*()"]
    blank_input = []

    # brute_soltuion = BruteEncodeDecode()
    # nonAsciiEncodeDecode = NonAsciiEncodeDecode()
    optimalSolution = OptimalSolution()
    encoded_string = optimalSolution.encode(test_input)
    decoded_string = optimalSolution.decode(encoded_string)

    print(decoded_string)
