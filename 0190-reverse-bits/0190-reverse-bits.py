class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bits = bin(n)
        
        bits = bits[2:]
        
        bits = bits[::-1] + ("0" * (32-len(bits)))
        
        return int(bits, 2)
    