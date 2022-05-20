def conference(actions, parties):
    laws = list()
    ans = True

    for action, partie in zip(actions, parties):
        if action == 'A':
            laws.append(partie)
            ans = True  
        elif action == 'V':
            ans = False
            if len(laws) > 0:
                if laws.pop() == partie:
                    ans = True
        if ans is False:
            break
    
    if ans is True:
        return 'Yes'
    return 'No'

print(conference("AVAAAVVV", "aabybbyb"))
print(conference("AAVV", "abab"))

