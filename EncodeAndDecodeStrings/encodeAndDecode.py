class Solution:
#To encode the string assign a variable, iterate through list,
#append the length of string number first then string, return string. 

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += f"{len(s)}#{s}"
        return encodedStr


#To decode, assign an array, with a variable i to extract indexes, loop 
#till end of string, find where # is to indicate the string of the string
#append the string of list to start after length and end at the end of the
#found string length. return list. 
    def decode(self, s: str) -> List[str]:
        decodedString = []
        i = 0
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            decodedString.append(s[j + 1:j+1 + length])
            i = j + 1 + length
        return decodedString
