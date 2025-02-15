class Solution:
    def reverse(self, x: int) -> int:
        # convert int to string so that we are able to iterate over integer and get each digit
        y = str(x)
        # create empty string to store the reversed integer as a string
        z = ''
        n = len(y)     
        # handle negative integers
        if y[0] == '-': 
            # for each digit in integer, add it to the front of the answer string
            for i in range(1,n):            
                z = y[i] + z
            z = '-' + z    
        # handle positive integers
        else:
            # for each digit in integer, add it to the front of the answer string
            for i in range(0,n):            
                z = y[i] + z
            
        revnum = int(z)
        # TODO: handle edge cases: when reversed integer <-2 raised 31 or >2 raised 31

        return revnum
        
