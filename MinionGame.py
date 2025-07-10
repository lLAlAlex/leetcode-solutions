def minion_game(string):
    stuart = 0
    kevin = 0
    
    vowels = ['A', 'I', 'U', 'E', 'O']
    
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    
    if kevin < stuart:
        print(f"Stuart {stuart}")
    elif stuart < kevin:
        print(f"Kevin {kevin}")
    else:
        print("Draw")

print(minion_game("BANANA"))