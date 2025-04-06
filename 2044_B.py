t = int(input())
while t>0:
    word = input()
    reversed_word = word[::-1]
    # p will be replced by q and q will be replaced by p
    for i in range(len(reversed_word)):
        if reversed_word[i] == 'p':
            reversed_word = reversed_word[:i] + 'q' + reversed_word[i+1:]
        elif reversed_word[i] == 'q':
            reversed_word = reversed_word[:i] + 'p' + reversed_word[i+1:]
    print(reversed_word)
    t -= 1