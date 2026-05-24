import time

def cantar_verso(verso, duracao_segundos):
    total_letras = len(verso)
    atraso_letra = duracao_segundos / total_letras if total_letras > 0 else 0
    
    for letra in verso:
        print(letra, end="", flush=True)
        time.sleep(atraso_letra)
    print() 

musica = [
    ("I cannot vanish, you will not scare me", 3.5),
    ("Try to get through it, try to bounce to it", 3.5),
    ("You were not thinking that I will not do it", 4.0),
    ("They be lovin' someone and I'm another story", 4.0),
    ("Take the next ticket, get the next train", 3.5),
    ("Why would I do it? Have you ever think that?", 4.0)
]

print("\nLet It Happen...\n")
time.sleep(3) 

for verso, duracao in musica:
    cantar_verso(verso, duracao)
