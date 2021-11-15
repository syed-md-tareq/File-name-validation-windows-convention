def validator(passed):
    import random
    passed = passed
    invalids = r'<>?/"|:\*!'
    inv1 = []
    for chars in passed:
        if chars in invalids:
            inv1.append(chars)
    if inv1 != []:
        print('You have entered invalid character for folder name')
        print(r'The followings are invalid characters for folder/file names')
        print('and a file/folder can not be created using these one or more of these characters:\n')
        for chars in invalids:
            print(chars+' ',end = '')
        print('\n')
        print('Please enter a new name for the folder') 
        passed2 = input('or press enter to automatically generate a name: ')
        if passed2 == '':
            import random
            passed2 = '@'
            for x in range(7):
                passed2 += random.choice('abcdefghijklmnopqrstuvwxyz')
            #print(passed2)
            return passed2
        inv1 = []
        for chars in passed2:
            if chars in invalids:
                inv1.append(chars)
        if inv1 == []:
            #print(passed2)
            return passed2
    else:
        #print(passed)
        return passed
    
    while inv1 != []:
        print('You have again entered invalid character again for the folder name!')
        print('Type a new name or press enter to automatically fix the error:')
        passed3 = input()
        #print('Passed2 = ',passed2)
        #print('Passed3 = ',passed3)
        #print('inv1 = ',inv1)
        if passed3 == '':
            
            if len(inv1) > 1:                # For replacing all same invalid chars with different valids
                if len(list(set(inv1))) == 1:   # Wheel reinvented !
                    passed2 = list(passed2)     # Many lines can be erased
                    for chrs in range(len(passed2)):
                        if passed2[chrs] == inv1[0]:
                            
                            passed2[chrs] = random.choice('@#$%&_+')
                    passed2 = ''.join(passed2)
                    #print(passed2)
                    return passed2
                else:
                    for invs in inv1:
                        passed2 = passed2.replace(invs,random.choice('@#$%&_+'))
                    #print(passed2)
                    return passed2
            else:
                for invs in inv1:
                    passed2 = passed2.replace(invs,random.choice('@#$%&_+'))
                #print(passed2)
                return passed2
        else:
            passed2 = passed3
            inv1 = []
            for chars in passed3:
                if chars in invalids:
                    inv1.append(chars)
            #inv1 = list(set(inv1))
            if inv1 == []:
                #print(passed3)
                return passed3
        passed2 = passed3

       

validator('?Babor')
