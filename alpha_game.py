# 단어게임

from string import ascii_uppercase
from random import randint

alphabetList = list(ascii_uppercase)
print('''
WELCOME
''')

difficulty = int(input('''1단계는 1입력
2단계는 2입력
3단계는 3입력
단계를 입력하세요 : '''))
if difficulty == 1:
    setNumber = 15
elif difficulty == 2:
    setNumber = 13
else:
    setNumber = 11

randomList = []
print("-"*setNumber*2)
for i in range(setNumber):
    randomAlphaSet = ""
    randomAlphaList = ""
    for j in range(setNumber):
        randomNumber = randint(1,26)
        randomAlpha = alphabetList[randomNumber-1]
        randomAlphaSet += randomAlpha + " "
        randomAlphaList += randomAlpha
    print(randomAlphaSet)
    randomList.append(list(randomAlphaList))
print("-"*setNumber*2)


def finding_word(number, List, inputString):
    # randomList에서 index추출(word하나)
    stringNumber = [[i,j] for i in range(number) for j in range(number) if inputString == List[i][j]]
    if stringNumber == []:
        stringNumber = "wrong"
    return stringNumber

def find_words(word):
    List = []
    for i in range(len(word)):
        list = finding_word(setNumber, randomList, word[i])
        List.append(list)
    return List

def word_line(list):
    line = []
    if len(list)>=3:
        for i in range(len(list[0])):
            for j in range(len(list[1])):
                num1 = (list[0][i][0] - list[1][j][0])
                num2 = (list[0][i][1] - list[1][j][1])
                if (num1<=1 and num1>=-1) and (num2<=1 and num2>=-1):
                    line.append([list[0][i],list[1][j],[num1, num2]])
    answer = [(list[l][m]) for k in range(len(line)) for l in range(2,len(list)) for m in range(len(list[l])) if [(line[k][1][0]-(line[k][2][0])*(l-1)),(line[k][1][1]-(line[k][2][1])*(l-1))] == list[l][m]]
    if len(answer) >= 1:
        return answer
    else:
        return 1



        
player1Answer = 1
player2Answer = 1    
gameContinue = 0

while gameContinue == 0:
        print("-------------------")    
        player1 = input("1P answer? ").upper()
        wordNumberList = find_words(player1)
        p1 = word_line(wordNumberList)
        if ("wrong" in wordNumberList) or (len(wordNumberList)<3) or (p1 == 1):
            player1Answer = 0
            print("1P wrong!")
        
            
        player2 = input("2P answer? ").upper()
        wordNumberList = find_words(player2)
        p2 = word_line(wordNumberList)
        if ("wrong" in wordNumberList) or (len(wordNumberList)<3) or (p2 == 1):
            player2Answer = 0
            print("2P wrong!")


        if (player1Answer + player2Answer)%2 == 0:
            player1Answer = 1
            player2Answer = 1
        else:     
            gameContinue = 1
            print('''--------
GAMOVER
--------''')
