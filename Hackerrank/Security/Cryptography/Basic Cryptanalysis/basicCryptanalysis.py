import string

class TreeNode:
    def __init__(self, alphamap):
        self.alphamap = alphamap
    def isConsistent(self, garbled, plain):
        result = True
        for i, letter in enumerate(garbled):
            result = result and (self.alphamap[letter] == plain[i] or self.alphamap[letter] == '')
        return result
                                 
    def newNode(self, garbled, plain):
        if self.isConsistent(garbled, plain):
            newMap = dict(self.alphamap)
            for i, l in enumerate(garbled):
                newMap[l] = plain[i]
            return TreeNode(newMap)
        
        

def main():
    enciphered = input()
    alpha = string.ascii_lowercase
    dictionary =  open('dictionary.lst', 'r').read().lower().split('\n')
    alphamap = dict(zip(string.ascii_lowercase, ['']*26))
    bucketDict = dict();
    for word in dictionary:
        l = len(word)
        if l in bucketDict.keys():
            bucketDict[l].append(word)
        else:
            bucketDict[l] = [word]           
    inputs = sorted(list(set(enciphered.split(' '))),reverse=True)
    root = TreeNode(alphamap)
    prevLevel = [root]
    cipher = None
    while len(inputs) != 0:
        word = inputs.pop()
        currentLevel = []
        for dictWord in bucketDict[len(word)]:
            for parent in prevLevel:
                newNode = parent.newNode(word, dictWord)
                if newNode:
                    currentLevel.append(newNode)
        prevLevel = currentLevel
        if len(inputs) == 0:
            cipher = currentLevel[0].alphamap
    result = ''
    for letter in enciphered:
        result += ' ' if letter == ' ' else cipher[letter]
    print(result)
            
    

if __name__ == '__main__':
    main()