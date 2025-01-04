with open("books/frankenstein.txt") as f:
    file_contents = f.read()

char_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
count_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in file_contents:
    i = i.lower()
    for j in range(len(char_list)):
        if i == char_list[j]:
            count_list[j] += 1

for i in range(len(char_list)):
    print("The ", char_list[i], " character was found ", count_list[i], " times")