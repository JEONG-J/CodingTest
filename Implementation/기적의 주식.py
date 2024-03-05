def joon_bnf(money, stocks):
    have_stcok = 0
    for idx in range(len(stocks)):
        can_buy = money // stocks[idx]
        if can_buy > 0:
            money -= can_buy * stocks[idx]
            have_stcok += can_buy
    return money + stocks[-1] * have_stcok

def seong_timing(money, stocks):
    up_cnt = 0
    down_cnt = 0
    have_stock = 0
    for idx in range(1, len(stocks)):
        if stocks[idx] > stocks[idx-1]:
            up_cnt += 1
            down_cnt = 0
            if up_cnt >= 3:
                money += have_stock * stocks[idx]
                have_stock = 0
        elif stocks[idx] < stocks[idx-1]:
            down_cnt += 1
            up_cnt = 0
            if down_cnt >= 3:
                can_buy = money // stocks[idx]
                money -= can_buy * stocks[idx]
                have_stock += can_buy
        else:
            up_cnt = 0
            down_cnt = 0

    return money + stocks[-1] * have_stock

money = int(input())
stocks = list(map(int, input().split()))

joon = joon_bnf(money, stocks)
seong = seong_timing(money, stocks)

if joon > seong:
    print("BNP")
elif joon == seong :
    print("SAMESAME")
else:
    print("TIMING")