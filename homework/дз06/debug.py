stroke = str(input())

max_len = 0
biggest_word = None 

for word in stroke.split(): 
    if len(word) > max_len :
        max_len = word
        biggest_word = word

print(biggest_word)