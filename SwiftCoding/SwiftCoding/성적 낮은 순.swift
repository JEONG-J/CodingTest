//
//  main.swift
//  SwiftCoding
//
//  Created by 정의찬 on 2023/03/10.
//

import Foundation

let n = Int(readLine()!)!

 //var catArr : [(name: String, age: Int)] = []

var data:[(Name: String, Num: Int)] = []

for _ in 0..<n{
    var inputData = readLine()!.split(separator: " ")
    var name: String = String(inputData[inputData.startIndex])
    var num: Int = Int(inputData[inputData.index(after: inputData.startIndex)])!
    data.append((Name: name, Num: num))
}

data.sort(by: { $0.1 < $1.1})


for i in 0..<n{
    print(data[i].Name)
}
