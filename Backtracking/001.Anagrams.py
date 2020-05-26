def anagrams(input_string, anagram, used, index):
    if index == len(input_string):
        print(anagram)
        return
    for i in range(0, len(input_string)):
        if not used[i] :#and input_string[i]!=input_string[i-1]:
            used[i] = True
            anagram[index] = input_string[i]
            anagrams(input_string, anagram, used, index + 1)
            used[i] = False


input_string = "abc"
anagram = ['a' for _ in range(0, len(input_string))]
used = [False for i in range(0, len(input_string))]
anagrams(input_string, anagram, used, 0)
