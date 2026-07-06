class Solution:

    def encode(self, strs: List[str]) -> str:
        result_str = ""
        for s in strs:
            prefix = f"{len(s):4}"
            result_str += prefix
            result_str += s
        return result_str

    def decode(self, s: str) -> List[str]:
        index = 0
        total_length = len(s)
        result = []
        while index < total_length:
            str_length = int(s[index:index + 4])
            index += 4
            str = s[index:index + str_length]
            result.append(str)
            index += str_length
        return result
