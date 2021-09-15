words = open("GCP/resultado_part-00000.txt", "r")
resultado = open("GCP/resultado.txt", "w")
i = 0
while i < 10:
    resultado.writelines(words.readline())
    i += 1