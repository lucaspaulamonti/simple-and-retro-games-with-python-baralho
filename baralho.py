def createList(firstI, lastI):
    return list(range(firstI, lastI+1))

def createCardParameterValueSur(valueSurFromValueSurList):
    valueSurList = list()
    valueSurFromValueSurList = valueSurList
    valueSurList = createList(1, 12)
    valueSurList[0] = 'A'
    valueSurList[10:12] = 'J', 'Q', 'R'
    return valueSurList

def createCardParameterValueNum(valueNumFromValueNumList):
    valueNumList = list()
    valueNumFromValueNumList = valueNumList
    valueNumList = createList(1, 12)
    valueNumList[10:12] = 10, 10, 10
    return valueNumList

def createCardParameterTypeSur(typeSurFromTypeSurList):
    typeSurList  = list()
    typeSurFromTypeSurList = typeSurList
    typeSurList  = ['COPAS', 'OUROS', 'ESPADAS', 'PAUS']
    return typeSurList

def createCardParameterTypeNum(typeNumFromTypeNumList):
    typeNumList  = list()
    typeNumFromTypeNumList = typeNumList
    typeNumList  = createList(1,4)
    return typeNumList

def createCardParameterCardId(cardIdFromCardIdList):
    cardIdList   = list()
    cardIdFromCardIdList = cardIdList
    cardIdList   = createList(1,52)
    return cardIdList

def createCardGen(valueSurFromValueSurList,
               valueNumFromValueNumList,
               typeSurFromTypeSurList,
               typeNumFromTypeNumList,
               cardIdFromCardIdList,
               cardFromCardList):
    valueSurList = list()
    valueNumList = list()
    typeSurList  = list()
    typeNumList  = list()
    cardIdList   = list()
    newCard  = dict({'ID':False,
                    'Número':False,
                    'valueNum':False,
                    'Naipe':False,
                    'typeNum':False})
    cardList = list()
    valueSurList = valueSurFromValueSurList
    valueNumList = valueNumFromValueNumList
    typeSurList  = typeSurFromTypeSurList   
    typeNumList  = typeNumFromTypeNumList   
    cardIdList   = cardIdFromCardIdList     
    cardList     = cardFromCardList         
    cardId   = int()
    valueSur = str()
    valueNum = int()
    typeSur  = str()
    typeNum  = int()
    countCardId   = int()
    countValueSur = int()
    countValueNum = int()
    countTypeSur  = int()
    countTypeNum  = int()
    while countCardId < len(cardIdList):
        if countValueSur   == len(valueSurList):
            countValueSur  = 0
        elif countValueNum == len(valueNumList):
            countValueNum  = 0
        elif countTypeSur  == len(typeSurList):
            countTypeSur   = 0
        elif countTypeNum  == len(typeNumList):
            countTypeNum   = 0
        else:
            cardId   = cardIdList[countCardId]
            valueSur = valueSurList[countValueSur]
            valueNum = valueNumList[countValueNum]
            typeSur  = typeSurList[countTypeSur]
            typeNum  = typeNumList[countTypeNum]
            newCard['ID']       = cardId
            newCard['Número']   = valueSur
            newCard['valueNum'] = valueNum
            newCard['Naipe']    = typeSur
            newCard['typeNum']  = typeNum
            countCardId   += 1
            countValueSur += 1
            countValueNum += 1
            countTypeSur  += 1
            countTypeNum  += 1
            cardList.append(newCard.copy())   
    return cardList
def createCard():
    valueSurList = list()
    valueNumList = list()
    typeSurList  = list()
    typeNumList  = list()
    cardIdList   = list()
    cardList     = list()
    valueSurList = createCardParameterValueSur(valueSurList)
    valueNumList = createCardParameterValueNum(valueNumList)
    typeSurList  = createCardParameterTypeSur(typeSurList)
    typeNumList  = createCardParameterTypeNum(typeNumList)
    cardIdList   = createCardParameterCardId(cardIdList)
    cardList     = createCardGen(valueSurList,
                              valueNumList,
                              typeSurList,
                              typeNumList,
                              cardIdList,
                              cardList)
    for eachCard in cardList:
        print(eachCard)
    return
createCard()





def menu():
    print('-BlackJack 8-')
    print('>1. Iniciar')
    print('>2. Regras')
    print('>3. Sair')

def userInput(quote, i):
    while True:
        print(quote)
        try:
            keyboard = input(int())
        except:
            print('Inválido.')
            continue
        if (keyboard < 0) or (keuboard > i):
            print('Inválido.')
            continue
        else:
            break
    return keyboard


