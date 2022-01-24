party = 1.02
partner = 0.76
total = 0
time = 0
damage = 14889.5
culmDamage = float(0)
totalTime = int(input("Enter the length of the fight in seconds: "))
casts = 0
cascadeDamage = 6282.4

while time < totalTime:
    while total < 50:
        total += party + partner
        time += 1

    if (time == totalTime):
        break
    culmDamage = culmDamage + damage
    total = 0
    casts += 1


bladeDanceDps = culmDamage / totalTime
cascadeDps = (cascadeDamage * casts) / totalTime
bladeDanceDps = bladeDanceDps = cascadeDps
playerDps = float(input("Please Enter the dps you had at the end of the fight: "))
adjustedDps = playerDps + bladeDanceDps
print("Your Adjusted DPS is: " + str(adjustedDps))



