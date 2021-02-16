#try:
#    f = open('aleph.txt',)
#finally:
#    f.close()

with open("numeros.txt","w") as f:
    for i in range(10):
        f.write(str(i))