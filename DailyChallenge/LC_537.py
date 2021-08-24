class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a,b = num1.split('+')
        c,d = num2.split('+')
        

        rea = int(a) * int(c) - int(b[:len(b)-1]) * int(d[:len(d)-1])
        img = int(b[:len(b)-1]) * int(c) + int(a) * int(d[:len(d)-1])
        
        return str(rea) +"+" + str(img) +"i"
