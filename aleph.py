counter = 0
with open("aleph.txt") as f:
    #print(f.readlines())
    for line in f:
        counter += line.count("Beatriz")
        
print(f"Beatriz se encuentra {counter} veces en el texto.")