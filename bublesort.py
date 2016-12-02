vetor = [9, 8, 5, 2, 1, 3, 5, 51, 23, 312, 32, 6]

for i in range(len(vetor)):
    for j in range((len(vetor) - 1)):
        if vetor[j] > vetor[j+1]:
            aux = vetor[j]
            vetor[j] = vetor[j+1]
            vetor[j+1] = aux

print(vetor)
