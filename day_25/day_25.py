from math import sqrt,ceil

card_pub = 11239946
door_pub = 10464955
modu = 20201227

# brute-force card private key
card_priv = -1
val = 1
for j in range(1,modu):
    #val = pow(7, j, modu)
    val *= 7
    val %= modu
    if val == card_pub:
        print("card",j)
        card_priv = j
        break

ans = pow(door_pub, card_priv, modu)
print(ans)
