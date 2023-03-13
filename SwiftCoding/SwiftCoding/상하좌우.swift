//
//  main.swift
//  SwiftCoding
//
//  Created by 정의찬 on 2023/03/06.
//

import Foundation

let n = Int(readLine()!)

var x:Int = 1
var y:Int = 1

let plans = readLine()!.split(separator: " ")

let dx:[Int] = [0,0,-1,1]
let dy:[Int] = [-1,1,0,0]
let dir:[String] = ["L","R","U","D"]

var nx:Int = 0
var ny:Int = 0

for plan in plans{
    for i in 0..<dir.count{
        if plan == dir[i]{
            nx = x + dx[i]
            ny = y + dy[i]
        }
        if nx < 1 || nx > n! || ny < 1 || ny > n!{
            continue
        }
    x = nx
    y = ny
    }
    
}
print(x,y)

