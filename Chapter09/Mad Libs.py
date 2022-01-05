
import re

sen=input("Enter a sentence containing word ADJECTIVE, NOUN, ADVERB, or VERB : ").split(' ')

adj=input("Enter word for ADJECTIVE : ")
non=input("Enter word for NOUN : ")
adv=input("Enter word for ADVERB : ")
verb=input("Enter word for VERB : ")

# mo=re.compile()

for i in sen:
    if i =="ADVERB":
        print(adv,end=' ')
    elif i =="ADJECTIVE":
        print(adj,end=' ')
    elif i =="NOUN":
        print(non,end=' ')
    elif i =="VERB":
        print(verb,end=' ')
    else:
        print(i,end=' ')