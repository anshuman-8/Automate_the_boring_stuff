import re


def isValidChessBoard(dict):
    keysList=list(dict.keys())
    mo=re.compile(r'\d')
    for k in keysList:
        # print(mo.search(k).group())
        numb=int(mo.search(k).group())
        if numb>8:
            return False
    valuelist=list(dict.values())
    mki=re.compile(r'king$')
    mq=re.compile(r'queen$')
    k=0
    for v in valuelist:
        if mki.search(v).group()==king:
            k=k+1
        if k>2:
            return False
    q=0
    for v in valuelist:
        if mq.search(v).group()==queen:
            q=q+1
        if k>2:
            return False

    # print(valuelist)
    return True


dict={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
a=isValidChessBoard(dict)

print(a)