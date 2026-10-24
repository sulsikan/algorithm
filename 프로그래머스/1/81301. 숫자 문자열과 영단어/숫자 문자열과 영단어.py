def solution(s):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for idx, word in enumerate(numbers):
        s = s.replace(word, str(idx))
        
    return int(s)