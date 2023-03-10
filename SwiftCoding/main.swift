//
//  main.swift
//  SwiftCoding
//
//  Created by 정의찬 on 2023/03/10.
//

import Foundation

let inputData = readLine()!.split(separator: " ").map {Int(String($0))!}
let n:Int = inputData[0]
let k:Int = inputData[1]

var a = readLine()!.split(separator: " ").map {Int(String($0))!}
var b = readLine()!.split(separator: " ").map {Int(String($0))!}

a.sort()
b.sort(by: >)

var temp:Int

for i in 0..<k{
    if b[i] > a[i]{
        temp = a[i]
        a[i] = b[i]
        b[i] = temp
    }
}

print(a.reduce(0, +))
