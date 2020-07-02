def isPoker(cards):
    isPokerHand = "No es poker"
    cardTypes = {}

    for card in cards:
        if(card[0] in cardTypes):
            cardTypes[card[0]] = cardTypes[card[0]] + 1

            if cardTypes[card[0]] >= 4:
                isPokerHand = "Es poker"
        else:
            cardTypes[card[0]] = 1

    return isPokerHand

print(isPoker([("10","corazones"), ("10", "picas"), ("10", "diamantes"), ("10", "treboles"),("8","diamantes")]))
print(isPoker([("10","corazones"), ("10", "picas"), ("10", "diamantes"), ("8", "treboles"),("8","diamantes")]))
print(isPoker([("10","corazones"), ("10", "picas"), ("8", "diamantes"), ("10", "treboles"),("8","diamantes")]))
print(isPoker([("10","corazones"), ("8", "picas"), ("10", "diamantes"), ("10", "treboles"),("8","diamantes")]))
print(isPoker([("8","corazones"), ("10", "picas"), ("10", "diamantes"), ("10", "treboles"),("8","diamantes")]))
print(isPoker([("10","corazones"), ("10", "picas"), ("8", "diamantes"), ("10", "treboles"),("10","diamantes")]))
print(isPoker([("8","corazones"), ("10", "picas"), ("8", "diamantes"), ("10", "treboles"),("10","diamantes")]))
print(isPoker([("10","corazones"), ("8", "picas"), ("8", "diamantes"), ("10", "treboles"),("10","diamantes")]))
print(isPoker([("10","corazones"), ("10", "picas"), ("8", "diamantes"), ("8", "treboles"),("10","diamantes")]))
print(isPoker([("10","corazones"), ("10", "picas"), ("10", "diamantes"), ("8", "treboles"),("10","diamantes")]))
print(isPoker([("10","corazones"), ("8", "picas"), ("10", "diamantes"), ("8", "treboles"),("10","diamantes")]))
print(isPoker([("8","corazones"), ("10", "picas"), ("10", "diamantes"), ("8", "treboles"),("10","diamantes")]))
print(isPoker([("10","corazones"), ("8", "picas"), ("10", "diamantes"), ("10", "treboles"),("10","diamantes")]))
print(isPoker([("8","corazones"), ("8", "picas"), ("10", "diamantes"), ("10", "treboles"),("10","diamantes")]))
print(isPoker([("8","corazones"), ("10", "picas"), ("10", "diamantes"), ("10", "treboles"),("10","diamantes")]))
