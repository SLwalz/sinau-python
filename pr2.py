#latihan komparasi dan logika

print("range\t---0+++5---8+++11---")
inputUser = int(input("masukkan angka:" ))
#       ---0+++5---8+++11---
kurang0false =not(inputUser < 0)
print(inputUser,"< 0",kurang0false)
kurang5true = (inputUser < 5)
print(inputUser,"< 5",kurang5true)
kurang8false = not(inputUser < 8)
print(inputUser,"< 8",kurang8false)
kurang11true = (inputUser < 11)
print(inputUser,"< 11",kurang11true)
lebih11fasle = not(inputUser > 11)
print(inputUser,"> 11 ",lebih11fasle)

print(15*"=")

print('range\t+++0---5+++8---11+++')
inputUser = int(input("masukkan angka:" ))

kurang0false =(inputUser < 0)
print(inputUser,"< 0",kurang0false)
kurang5true = not(inputUser < 5)
print(inputUser,"< 5",kurang5true)
kurang8false = (inputUser < 8)
print(inputUser,"< 8",kurang8false)
kurang11true = not(inputUser < 11)
print(inputUser,"< 11",kurang11true)
lebih11fasle = (inputUser > 11)
print(inputUser,"> 11 ",lebih11fasle)
