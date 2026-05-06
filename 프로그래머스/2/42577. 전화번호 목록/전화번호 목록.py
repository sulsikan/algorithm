def solution(phone_book):
    hash_map = {phone : 1 for phone in phone_book}
    
    for phone in phone_book:
        prefix = ''
        
        for num in phone:
            prefix += num
            if prefix in hash_map and prefix != phone:
                return False
                
    return True
    
    
    