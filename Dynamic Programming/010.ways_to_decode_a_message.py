
#Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
#count the number of ways it can be decoded.

#For example, the message '111' would give 3, 
#since it could be decoded as 'aaa', 'ka', and 'ak'.

# O(n) time and O(n) space

def ways_to_decode(s):
    memo = [-1]*(len(s)+1)
    
    return ways_to_decode_util(s,len(s),memo)

def ways_to_decode_util(data,k,memo):
    if k == 0:
        return 1
    l = len(data) - k
    
    if data[l] == "0":
        return 0
    if memo[k] != -1:
        return memo[k]
    
    result = ways_to_decode_util(data,k-1,memo)
    
    if k>=2 and int(data[l:l+2]) <=26:
        result = result + ways_to_decode_util(data,k-2,memo)
        memo[k] = result
    
    return result

if __name__ == "__main__":
    s = "231"
    print(ways_to_decode(s))
