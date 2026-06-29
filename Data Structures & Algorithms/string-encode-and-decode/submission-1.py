class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for str in strs:
            result += f"{len(str):4}"
            result += str
        return result

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        index = 0
        total_length = len(s)
        while index < total_length:
            str_length = int(s[index:index + 4])
            index += 4
            curr_str = s[index:index + str_length]
            decoded_strings.append(curr_str)
            index += str_length
        return decoded_strings