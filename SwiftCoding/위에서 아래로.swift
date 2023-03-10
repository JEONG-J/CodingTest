//
//  main.swift
//  SwiftCoding
//
//  Created by 정의찬 on 2023/03/10.
//

import Foundation

let n = Int(readLine()!)!

var array:[Int] = []
for _ in 0..<n{
    array.append(Int(readLine()!)!)
}

array.sort(by: >)

print(array)
