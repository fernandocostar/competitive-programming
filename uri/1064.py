VALORES_POSITIVOS = 0
SOMA_POSITIVOS = 0
for i in range(6):
    user = float(input())
    if user > 0:
        VALORES_POSITIVOS += 1
        SOMA_POSITIVOS += user
print(VALORES_POSITIVOS, "valores positivos")
print(SOMA_POSITIVOS/VALORES_POSITIVOS) if VALORES_POSITIVOS else print("-nan")