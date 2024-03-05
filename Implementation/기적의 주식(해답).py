from sys import stdin
def BNP(money, chart):
    cnt = 0
    for i in range(len(chart)):
        can_buy = money // chart[i]
        if can_buy > 0:
            money -= can_buy * chart[i]
            cnt += can_buy
    return cnt * chart[-1] + money

def TIMING(money, chart):
    cnt = up = down = 0
    for i in range(1, len(chart)):
        if chart[i] < chart[i-1]:
            up = 0
            down += 1
            if down >= 3:
                can_buy = money // chart[i]
                money -= can_buy * chart[i]
                cnt += can_buy
        elif chart[i] > chart[i-1]:
            down = 0
            up += 1
            if up >= 3:
                money += cnt * chart[i]
                cnt = 0
        else:
            up = down = 0
    return cnt * chart[-1] + money

money = int(stdin.readline())
chart = list(map(int,stdin.readline().split()))
jun = BNP(money, chart)
sung = TIMING(money, chart)
if jun > sung:
    print("BNP")
elif jun == sung :
    print("SAMESAME")
else:
    print("TIMING")