def find_longest_word(text):
    words = text.split()
    longest = max(words, key=len)
    return longest

print(find_longest_word("Python programming is powerful"))


def replace_middle_with_star(s):
    if len(s) <= 2:
        return s
    return s[0] + '*' * (len(s) - 2) + s[-1]
print(replace_middle_with_star("apple")) 


def is_isogram(word):
    word = word.lower()
    return len(set(word)) == len(word)
print(is_isogram("machine"))  
print(is_isogram("letter"))  

def every_nth_char(s, n):
    return s[::n]
print(every_nth_char("abcdefghijk", 3))  

def reverse_by_words(s):
    return ' '.join(word[::-1] for word in s.split())
print(reverse_by_words("hello world python")) 

def compress_consecutive(s):
    if not s:
        return ""
    
    result = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = s[i]
            count = 1
    
    result.append(current_char + str(count))
    return "".join(result)

print(compress_consecutive("aaabbccccc")) 

def count_islands(grid):
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    islands = 0
    def dfs(i, j):
        if (i < 0 or i >= rows or j < 0 or j >= cols or 
            grid[i][j] == 0 or (i, j) in visited):
            return
        visited.add((i, j))
        dfs(i-1, j)  
        dfs(i+1, j) 
        dfs(i, j-1)  
        dfs(i, j+1) 
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and (i, j) not in visited:
                dfs(i, j)
                islands += 1
    
    return islands
grid = [
    [1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
]
print(count_islands(grid))