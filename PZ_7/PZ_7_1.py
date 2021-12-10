# Дан символ C и строки S, S0. Перед каждым вхождением символа
# С в строку S, вставить строку S0


C = str(input("Введите символ C: "))
S = str(input("Введите строку S: "))
S0 = str(input("Введите строку S0: "))

print("\n", S)
S1 = []

for i in range(len(S)):
    S1.append(S[i])
    if C in S1[i]:
        S1[i] += S0

print("\n", S1)
t = 0

while t < len(S)-1:
    S1[0] += S1[1]
    del S1[1]
    t += 1

print("\n", S1[0])
