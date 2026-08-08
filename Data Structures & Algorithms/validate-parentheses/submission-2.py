class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:  # if one of the defined chars  
                # check if the first and last element in stack are
                # the same as the character in our mapping 
                if stack and stack[-1] == mapping[char]: 
                    stack.pop() # remove and move forward
                else:
                    return False
            else: # assuming nothing and add to stack
                stack.append(char)
        
        # we have to check that there is nothing left
        return len(stack) == 0