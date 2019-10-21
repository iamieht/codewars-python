def namelist(names):
    """
    Input: Array -> String
    produces a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
    """
    listOfNames = []
    stringOfNamesA = ''
    stringOfNamesB = ''

    for name in names:
        listOfNames += name.values()
    
    if len(listOfNames) > 1:
        listOfNames.insert(len(listOfNames)-1, '&')
    
    if len(listOfNames) > 3:    
        stringOfNamesA = ', '.join(listOfNames[:-3] + ['']).rstrip(' ')
        stringOfNamesB = ' '.join(listOfNames[-3:] + ['']).rstrip(' ')
        return stringOfNamesA + ' ' + stringOfNamesB
    else:
        return ' '.join(listOfNames + ['']).rstrip(' ')
    
    
def namelist_better(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''



#Test
print("Expected result:", 'Bart, Lisa & Maggie')
print("Actual result:", namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
print("Expected result:", 'Bart & Lisa')
print("Actual result:", namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ]))
print("Expected result:", 'Bart')
print("Actual result:", namelist([ {'name': 'Bart'} ]))
print("Expected result:", '')
print("Actual result:", namelist([]))
print("Expected result:", 'Bart, Lisa, Maggie, Homer & Marge')
print("Actual result:", namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]))