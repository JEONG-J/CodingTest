//
//  main.swift
//  Swift
//
//  Created by 정의찬 on 2023/03/02.
//  큰 수의 법칙

import Foundation

var nmk = readLine()!.split(separator: " ").map{Int(String($0))!}
var n: Int = nmk[0]
var m: Int = nmk[1]
var k: Int = nmk[2]

var data = readLine()!.split(separator: " ").map{Int(String($0))!}

data.sort(by: >)

let first: Int = data[0]
let second: Int = data[1]

var res: Int = 0

var cnt: Int
cnt = (m/(k+1)) * k
cnt += m % (k+1)

res += cnt * first
res += (m - cnt) * second

print(res)
