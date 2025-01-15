# карточная игра больше или меньше
import random

# Константы карт
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLES = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
               'Jack', 'Queen', 'King')

NCARDS = 8


# Функция. Проходим по колоде и выбираем случайную карту
def getCard(deckListIn):
    thisCard = deckListIn.pop()

    return thisCard


# Перемешиваем колоду
def shuffle(decklistIn):
    decklistOut = decklistIn.copy()
    random.shuffle(decklistOut)
    return decklistOut


print('Welcom')
print()
startingDeckList = []

for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLES):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:
    print()
    gameDickList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDickList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is ', currentCardRank + ' of ' + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS):
        answer = input('Следующая карта будет больше или меньше ' + currentCardRank + ' ' +
                       currentCardSuit + ' ? (enter h or l): ')
        answer = answer.casefold()
        nextCardDict = getCard(gameDickList)
        nextCardRank = nextCardDict['rank']
        nextCardValue = nextCardDict['value']
        nextCardSuit = nextCardDict['suit']
        print('След карта: ', nextCardRank + ' of ' + nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('Отлично!!!, карта больше!! Вы выграли!')
                score = score + 20
            else:
                print('Увы, Вы проиграли')
                score = score - 15

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score = score + 20
                print('Отлично!!! Карта меньше, Вы выиграли!')

            else:
                score = score - 15
                print('Увы Вы проиграли')

        print('Ваш счет: ', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue

    goAgain = input('Поиграем еще ???? ввдите ENTER or q to quit: ')
    if goAgain == 'q':
        break

print('Пока!!!')