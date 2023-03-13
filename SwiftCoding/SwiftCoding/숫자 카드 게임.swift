//
//  main.swift
//  SwiftCoding
//
//  Created by 정의찬 on 2023/03/02.
// 숫자 카드 게임

import Foundation

let inputData = readLine()!.split(separator: " ").map{Int(String($0))!}

let n = inputData[0],  m = inputData[1]

var res: Int = 0
for _ in 1...n{
    let data = readLine()!.split(separator: " ").map{Int(String($0))!}
    let resData = data.min()!
    res = max(res, resData)
}

print(res)
