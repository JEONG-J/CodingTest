//
//  main.swift
//  SwiftCoding
//
//  Created by 정의찬 on 2023/03/06.
//

import Foundation

let inputData = readLine()!.split(separator: " ").map { Int(String($0))!}
var N:Int = inputData[0] // 17
var K:Int = inputData[1] // 4
var res:Int = 0

while true{
    let target:Int = (N / K) * K // 16
    res += N - target // 17 - 16
    N = target
    if N < K{
        break
    }
    res += 1
    N /= K
}
    
    res += (N-1)
    print(res)
