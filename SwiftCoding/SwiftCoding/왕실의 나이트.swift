//
//  main.swift
//  SwiftCoding
//
//  Created by 정의찬 on 2023/03/08.
//

import Foundation

let inputData = readLine()!

let row = Int(String(inputData[inputData.index(after: inputData.startIndex)]))!
let savecol:String = String(inputData[inputData.startIndex])
let col:Int =  Int(UnicodeScalar(savecol)!.value) - Int(UnicodeScalar("a").value) + 1


let steps = [(2,1), (1,2), (-2,1), (1,-2), (2,-1), (-1,2), (-1,-2), (-2,-1)]

var nextRow:Int
var nextCol:Int


var res: Int = 0
for step in steps{
    nextRow = row + step.0
    nextCol = col + step.1
    if nextRow >= 1 && nextRow <= 8 && nextCol >= 1 && nextCol <= 8{
        res += 1
    }
}

print(res)
