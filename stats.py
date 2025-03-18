def get_num_words(s):
    return f"Found {len(s.split())} total words"

def character_count(s):
    hash_map = {}
    
    for c in s:
        c = c.lower()
        if c in hash_map:
            hash_map[c] += 1
        else:
            hash_map[c] = 1

    return hash_map

def sorted_dics(d):
    for key, value in sorted(d.items(), key=lambda item: item[1], reverse=True):
        if key.isalpha():
            print(f"{key}: {value}")
