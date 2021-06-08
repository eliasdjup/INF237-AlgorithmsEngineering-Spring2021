# Greedy

i = [int(x) for x in input().split()]
N = i[0]
T = i[1]
K = i[2]

n_cards={}
cardvalues=[]

for c in input().split():
    x = int(c)
    if x in n_cards:
        n_cards[x] += 1
    else:
        n_cards[x] = 1

for i in range(0,T):
    line = [int(x) for x in input().split()]
    n = n_cards.get(i+1,0)
    buy = (2-n)*line[0]
    sell = n*line[1]
    cardvalues.append([buy+sell,buy,sell])

cardvalues.sort(key = lambda x: x[0])

total=0
for i in range(0,K):
    total-= cardvalues[i][1]
for i in range(K,T):
    total+= cardvalues[i][2]

print(total)

'''
PSEUDO

let cardValues be list

for i in 1..t
	buyWorth = (2-cardsInDeck)*buyPrice
	sellWorth = cardsInDeck*sellPrice
	profit = buyWorth+sellWorth
	insert (profit,buyWorth,sellWorth) into cardValues

sort cardValues by profit

total = 0
for i in 0..k
	total -= buyWorth in cardValues[i]
for i in k..t
	total += sellWorth in cardValues[i]

return total
'''