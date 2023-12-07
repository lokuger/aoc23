def main():
    with open('input6.txt') as f:
        input = f.readlines()
    
    # part 1 and part 2 share most code so pass part number to single solver function
    partx(input,1)
    partx(input,2)

def determine_hand_type(hand, part):
    if part == 1:
        s = set(hand)
        if len(s) == 1:
            return 7
        if len(s) == 2:
            counts = [hand.count(c) for c in s]
            if max(counts) == 4:
                return 6
            else:
                return 5
        if len(s) == 3:
            counts = [hand.count(c) for c in s]
            if max(counts) == 3:
                return 4
            else:
                return 3
        if len(s) == 4:
            return 2
        if len(s) == 5:
            return 1
    if part == 2:
        nJ = hand.count('J')
        g = hand.replace('J','')
        counts = [g.count(c) for c in set(g)]
        if nJ == 5 or max(counts)+nJ == 5:
            return 7
        if max(counts)+nJ == 4:
            return 6
        if max(counts)+nJ == 3:
            if nJ == 2: # three of a kind
                return 4
            if nJ in [0,1]:
                return 5 if len(set(g)) == 2 else 4 # full house or three of kind
        if max(counts)+nJ == 2:
            if nJ == 0:
                return 3 if len(set(g)) == 3 else 2     # two pair or one pair
            if nJ == 1:
                return 2
        if max(counts)+nJ == 1: # high card
                return 1


card_values_part1 = {'A':14,'K':13,'Q':12,'J':11,'T':10}
card_values_part2 = {'A':14,'K':13,'Q':12,'J':1,'T':10}
def compare_hands(hand1,hand2,part):
    h1 = determine_hand_type(hand1,part)
    h2 = determine_hand_type(hand2,part)
    if h1 == h2:
        i,differ = 0,False
        while i < len(hand1):
            if hand1[i] != hand2[i]:
                v1 = int(hand1[i]) if hand1[i].isdigit() else (card_values_part1[hand1[i]] if part == 1 else card_values_part2[hand1[i]])
                v2 = int(hand2[i]) if hand2[i].isdigit() else (card_values_part1[hand2[i]] if part == 1 else card_values_part2[hand2[i]])
                return 1 if v1 > v2 else -1
            i+=1
        print('Hands were equal, use arbitrary order')
        return 1
    elif h1 < h2:
        return -1
    else: # if h1 > h2:
        return 1

def partx(input,part):
    print('#### Part {} ####'.format(part))
    S = [(line.split()[0],int(line.split()[1])) for line in input]
    # insertion sort S comparing the hands in S[..][0]
    for i in range(1,len(S)):
        j = i
        while j > 0 and compare_hands(S[j][0],S[j-1][0],part) == -1:
            S[j], S[j-1] = S[j-1], S[j]
            j -= 1
    r = 0
    for i,s in enumerate(S):
        r += (i+1)*s[1]
    print(r) 

if __name__ == '__main__':
    main()