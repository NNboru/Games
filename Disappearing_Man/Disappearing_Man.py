from random import *
man=['\n\t\t\t\t^   ^\n\t\t\t       (ʘ   ʘ)', '\n\t\t\t      Ƈ   #   Ɔ', '\n\t\t\t        ՙ===՚', '\n\t\t\t\t | |\n\t\t\t     ----------', '\n\t\t\t    /|   NN   |\\\n\t\t\t   / |        | \\', '\n\t\t\t  /  |        |  \\\n\t\t\t  \\  ----------  /', '\n\t\t\t     |   /\\   |\n\t\t\t     |  /  \\  |', '\n\t\t\t     | /    \\ |\n\t\t']
words=['Jaane Bhi Do Yaaro','Kaagaz Ke Phool','Do Bigha Zamin','Amar Akbar Anthony','Shatranj Ke Khilari','Sahib Bibi Aur Ghulam']

def display(parts=8, guesses=0, wrong=[], word=list('rohan NN') ):
    for i in range(parts):
        print(man[i],end='')
    print('\n')
    print('No of Guesses: ', guesses)
    print('Wrong Guesses: ', *wrong,'\n')
    print(*word,sep=' ')
    print()
    

def Input():
    print('Enter 1 character: ',end='')
    c=input()
    while len(c)!=1 or not c.isalpha():
        print('Enter 1 character: ',end='')
        c=input()
    print('\n*','-'*40,'*')
    return c


n=4
wrong=[]
guess=0
word=choice(words)
lenword=len(word)
st=['_']*lenword
sel=sample(range(lenword),4)
for i in sel:
    st[i]=word[i]
for i in range(lenword):
    if word[i]==' ' and st[i]!=' ':
        st[i]=' '
        n+=1

while n!=lenword:
    display(8-len(wrong),guess,wrong,st)
    guess+=1
    c=Input()
    a=0
    for i in range(lenword):
        if st[i]=='_':
            if word[i].lower()==c.lower():
                #correct guess
                st[i]=word[i]
                n+=1
                a=1
                #break #for single change
    if a==0:
        #wrong guess
        wrong.append(c)

    if n==lenword or 8-len(wrong)==0:
        if n==lenword:
            display(8-len(wrong),guess,wrong,st)
            print(" \nYou Won !!!!!! \n")
        else:
            print(f' \nMovie was {word}\n You Lose !!! Awwwwwww!!! \n')
        
        print(" Do you want to replay: ",end='')
        re=input()
        re.lower()
        if re=='n' or re=='no':
            break
        else:
            n=3
            wrong=[]
            guess=0
            w=choice(words)
            while w==word:
                w=choice(words)
            word=w
            lenword=len(word)
            st=['_']*lenword
            sel=sample(range(lenword),3)
            for i in sel:
                st[i]=word[i]
            for i in range(lenword):
                if word[i]==' ' and st[i]!=' ':
                    st[i]=' '
                    n+=1
                
                
man=r'''
		^   ^
	       (Ó   Ó)
		  #
	        \___/
		 | |
	    -------------
	   /|    N N    |\
	  / |           | \
	 /  |           |  \
	 \  -------------  /
	    |    /\     |
	    |   /  \    |
	    |  /    \   |
	    |_/      \__|
'''  
