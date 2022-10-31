import pandas as pd
import clean_up as cl   #thi si the file name clean_up.py




#string = clean("HI THS IS ME...TESTIN500202, @CHECKing the scrip897t")
#print(string)


with open("big_data.txt", 'r')as text:
    all_words = []
    count = 0
    for line in text:
        words = line.split()
        count += 1
        
        for word in words:
            word = cl.clean(word)
            all_words.append(word)
    print('total count: ',count)
    print("num of words: ", len(all_words), '\n')
        
    
    

df_words = pd.DataFrame(data =all_words, columns=('words',) )
count_words = df_words['words'].value_counts()
print(count_words)



with open("big_data.txt", 'r')as text:
    all_letters = []
    count = 0
    for line in text:
        words = line.split()
        count += 1
        
        for word in words:
            word = cl.clean(word)
            #all_words.append(word)
            letters = list(words)
            for l in letter:
                all_letters.append(l)
    print('total count: ',count)
    print("num of words: ", len(all_words), '\n')
        
    
    

df_words = pd.DataFrame(data =all_words, columns=('words',) )
count_words = df_words['words'].value_counts()
print(count_words)