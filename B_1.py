out = open("1_wyniki.txt", 'w') #otwarcie pliku, w którym będą zapisywane wyniki kolejnych procesów

text = "Siala baba mak  \nNie wiedziala jak  \nA dziad wiedzial nie powiedzial  \nA to bylo tak"
print("Tekst : \n", text,"\n", file = out)

test1 = "Tekst testowy"
test2 = "Przykladowe zdanie o roznej dlugosci slowach"
test3 = "a bb ccc"

words = text.lower().split()
Test1 = test1.lower().split()
Test2 = test2.lower().split()
Test3 = test3.lower().split()
""""---------------------FUNCIONS-------------------------------------------------"""
def NumberOfWords(words):       #count words in string
    number_of_words = len(words)
    print("Liczba słów w napisie : ", number_of_words,"\n", file = out)
    return(number_of_words)

def Prefix(words,k):        #string builds from prefixs
    prefix = []
    for i in words:
        prefix = list(word[0:k] for word in words) 
    print("Napis skonstruowany z prefixów: ","".join(prefix),"\n", file = out)
    return "".join(prefix)  
    
def Sufix(words,k):         #string builds with sufixs
    for i in words:
        sufix = list(word[-k:] for word in words) 
    print("Napis skonstruowany z sufixów: ","".join(sufix),"\n", file = out)
    return("".join(sufix))
    
def LongestWord(words):     #longest word
   longest_size = 0
   longest_word = ''
   for word in words:
       if len(word) > longest_size:    
           longest_word = word
           longest_size = len(word)
   print("Najdłuższe słowo w napisie: ",longest_word,"\n", file = out) 
   return(longest_word)
   
   
def ShortestWord(words):
    shortest_size = 100
    for word in words:
        if len(word) < shortest_size:    # shortest word
            shortest_word = word
            shortest_size = len(word)
    print("Najkrótsze słowo w napisie: ",shortest_word,"\n", file = out )
    return(shortest_word)

def SortedAlpha(words):     #alphabetical sorting
    alpha = sorted(words)
    
    print("Sortowanie alfabetyczne : \n", alpha,"\n", file = out)
    return(alpha)
    
def SortedByLenght(words):  #sorting (lenght of words)
    lenght = sorted(words,key = len)
    
    print("Sortowanie pod względem długoci słów : \n", lenght,"\n", file = out)
    return(lenght)   
    
"""----------------DOING--FUNCTIONS---------------------------------------------"""

NumberOfWords(words) 
Prefix(words,1)
Sufix(words,1)
LongestWord(words)
ShortestWord(words)
SortedAlpha(words)
SortedByLenght(words)

out.close()     #zamykam plik wyjciowy tutaj by wyniki wykonywania assertów nie zamiecały pliku wynikowego

"""------------------------ASSERTS-------------------------------------------------"""

print('\nAsserty :\n')
assert NumberOfWords(Test1) == 2, "Żle policzone wyrazy"
assert Prefix(Test1, 1)=='tt', "Błędne prefixy"
assert Sufix(Test1,1) == 'ty', "Błędne sufixy"
assert LongestWord(Test2) == 'przykladowe', 'Źle dobrane najdłuższe słowo!!!'
assert ShortestWord(Test2) == 'o', "Źle dobrane najkrótsze słowo!!!"
assert SortedAlpha(Test3) ==['a','bb','ccc'], 'Złe sortowanie alfabetyczne!!!'
assert SortedByLenght(Test3) ==['a','bb','ccc'], 'Złe sortowanie względem długoci słów!!!'

     


 


