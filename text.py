def revword (word):
    newword=word[::-1].lower()
    return newword

def countword ():
    myfile=open('text.txt', 'r')
    word1=((myfile.readline()).lower()).strip()
    lines=myfile.readlines()
    count=1
    for line in lines:  
        line=line.strip()
        line=line.split(" ")
        for wordline in line:
            wordline=revword(wordline)
            if wordline==word1:
                count+=1
    return count
