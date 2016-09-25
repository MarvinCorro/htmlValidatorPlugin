import re

def checkIfSelfClosingTag(line):
    expression = r''

def getAllTagsInBuffer(current_buffer)
    expression = r'(^(<.*>)?(?:.*)?((((<.*>)?(\/)?)$)?))' #LOLCODE FIX THIS MESS HAHA
    #found </?\w+((\s+\w+(\s*=\s*(?:".*?"|'.*?'|[\^'">\s]+))?)+\s*|\s*)/?>))
    #updated </?\w+((\s+\w+(\s*=\s*(?:"(.|\n)*?"|'(.|\n)*?'|[^'">\s]+))?)+\s*|\s*)/?>")')
    #thanks to http://haacked.com/archive/2004/10/25/usingregularexpressionstomatchhtml.aspx/ 
    for line in current_buffer:
        if re.match(expression,line):
            #TODO Check if its self closing tag
            #if it is a self closing tag discard line
            #else store in some sort of data structure


def printBuf(current_buffer):
    for i in current_buffer:
        print(i)
