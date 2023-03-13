//
//  main.swift
//  Swift
//
//  Created by 정의찬 on 2023/03/02.
//  거스름돈

import Foundation

var n: Int = 1260
var cnt: Int = 0

let coins: [Int] = [500, 100, 50, 10]

for coin in coins{
    cnt += n/coin
    n %= coin
}

print(cnt)


