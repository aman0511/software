list=[]
def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    for v in aDict.values():
        list.append(v)
    lenth=0
    for x in range(len(list)):
        print list[x]
        lenth=lenth+len(list[x])
    return lenth
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print howMany(animals),animals,list