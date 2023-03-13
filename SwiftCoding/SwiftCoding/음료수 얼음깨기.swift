//
//  main.swift
//  SwiftCoding
//
//  Created by 정의찬 on 2023/03/09.
//

import Foundation

let inputData = readLine()!.split(separator: " ").map{ Int(String($0))!}
let n = inputData[0]
let m = inputData[1]

var array:[[Int]] = []
for _ in stride(from: 0, through: n, by: 1){
    array.append(readLine()!.map{Int(String($0))!})
}

func dfs(x:Int, y:Int) -> Bool{
    if x < 0 || x >= n || y < 0 || y >= m {
        return false
    }
    if array[x][y] == 0{
        array[x][y] = 1
        dfs(x: x+1, y: y)
        dfs(x: x-1, y: y)
        dfs(x: x, y: y+1)
        dfs(x: x, y: y-1)
        return true
    }
    return false
}

var res:Int = 0

for i in 0..<n{
    for z in 0..<m{
        if dfs(x: i, y: z) == true{
            res += 1
        }
    }
}
