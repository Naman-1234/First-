def minion_game(s):
    count1=0
    count2=0
    l=len(s)
    vowels="AEIOU"
    for i in range(0,len(s)):
        if s[i] in vowels:
            count1+=l-i
        else:
            count2+=l-i
    
    if count2>count1:
        print("Stuart {}".format(count2))
    elif count1>count2:
        print("Kevin {}".format(count1))
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
