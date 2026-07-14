class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            str_length = len(s)
            prefix = f"{len(s):4}"
            encoded_string += prefix
            encoded_string += s
        return encoded_string


    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        while index < len(s):
            str_length = int(s[index:index + 4])
            index += 4
            extracted_str = s[index:index + str_length]
            index += str_length
            result.append(extracted_str)
        return result

