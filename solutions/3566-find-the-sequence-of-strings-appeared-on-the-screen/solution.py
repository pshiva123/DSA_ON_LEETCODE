class Solution:
    def stringSequence(self, target: str) -> List[str]:
        result = []
        s = ""
        current_char = 'a'
        
        for char in target:
            while current_char != char:
                result.append(s + current_char)
                current_char = chr((ord(current_char) - ord('a') + 1) % 26 + ord('a'))
            s += current_char
            result.append(s)
            
           
            current_char = 'a'
        
        return result

