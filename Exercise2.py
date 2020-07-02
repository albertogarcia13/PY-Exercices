def isPoker (c1, c2, c3, c4):
    if c1[:2]==c2[:2]==c3[:2]==c4[:2] :
        return "Es poker"
    else:
        return "No es poker"

print(isPoker("A de corazones", "A de picas", "A de diamantes", "A de treboles"))
print(isPoker("10 de corazones", "10 de picas", "10 de diamantes", "10 de treboles"))
print(isPoker("2 de corazones", "2 de picas", "3 de diamantes", "2 de treboles"))
print(isPoker("1 de corazones", "10 de picas", "10 de diamantes", "10 de treboles"))
