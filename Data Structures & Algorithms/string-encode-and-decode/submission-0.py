class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_parts = [] 
        for s in strs:
            temp = f"{len(s):4}" # Prefix current string with its length (if its length is less than 4 digits, add empty spaces in front of the digit until the length of the prefix is 4 chars)
            encoded_parts.append(temp + s) # Add prefixes + current string to the encoded_parts array
        return "".join(encoded_parts) # Join all the prefix + string combos from the array into a single string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        index = 0
        total_length = len(s)
        while index < total_length:
            string_length = int(s[index:index + 4]) # Read the 4 character prefix that contains the current string's length
            index += 4 # Move the index to the first character of the actual string
            decoded_string = s[index:index + string_length] # Get actual string
            decoded_strings.append(decoded_string) # Add actual string to the decoded_strings array
            index += string_length # Move index to first index of the next 4 character prefix
        return decoded_strings

