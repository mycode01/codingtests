def getLastDigit(inp1, inp2, l=5):
    inp = inp1 ** inp2
    if inp > 9999 :
        return int(str(inp)[-5:])
    else :
        return inp

print(getLastDigit(2,26))
print(getLastDigit(123456789,12345))