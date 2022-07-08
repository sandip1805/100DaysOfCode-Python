
def isValid(parenthesis):

    tracker = []

    openining_parenthesis = ['(', '{', '[']
    closing_parenthesis = [')', '}', ']']

    for element in parenthesis:
        if (element in openining_parenthesis):
            tracker.append(element)
        elif(element in closing_parenthesis):
            pos = closing_parenthesis.index(element)
            n = len(tracker)
            if(n > 0 and openining_parenthesis[pos] == tracker[n-1]):
                tracker.pop()
            else:
                return "Unbalanced"
    
    if (len(tracker) == 0):
        return "Balanced"
    else:
        return "UnBalanced"


if __name__ == "__main__":
    print('parenthis problem!!!!')
    print(isValid('{{}}'))
    print(isValid('{{}'))
    print(isValid('{{()}}'))