def truncateOnlyText(text, position):
    currentPosition = 0
    textCount = 0
    processedText = text
    while textCount < position and currentPosition < len(processedText):
        if processedText[currentPosition] == '<':
            endTagPosition = processedText.find('>', currentPosition)
            if text[currentPosition + 1] == '/':
                currentPosition = endTagPosition + 1
            else:
                #check if closing tag is out of bounds to determine whether to include tags
                
                closingTag = processedText[currentPosition] + '/' + processedText[currentPosition + 1: endTagPosition if processedText.find(' ', currentPosition, endTagPosition) == -1 else processedText.find(' ', currentPosition, endTagPosition)] + '>'
                closingTagPosition = processedText.find(closingTag, currentPosition)
                subCount = 0
                ignoreText = False
                #count the enclosed text
                for i in range(endTagPosition + 1, closingTagPosition + len(closingTag)):
                    if processedText[i] == '<':
                        ignoreText = True
                    elif processedText[i] == '>':
                        ignoreText = False
                    elif not ignoreText:
                        subCount += 1
                #decide whether to keep tags or remove based on length of enclosed text
                if textCount + subCount <= position:
                    currentPosition = closingTagPosition + len(closingTag)
                    textCount += subCount
                else:
                    processedText = processedText[:currentPosition] + processedText[endTagPosition + 1: closingTagPosition] + processedText[closingTagPosition + len(closingTag):]
            
        else:
            currentPosition += 1
            textCount += 1
    return processedText[0: currentPosition]