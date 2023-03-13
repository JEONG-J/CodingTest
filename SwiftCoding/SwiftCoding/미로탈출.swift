//
//  main.swift
//  SwiftCoding
//
//  Created by 정의찬 on 2023/03/10.
//

import Foundation


let inputData = readLine()!.split(separator: " ").map {Int(String($0))!}
var n = inputData[0]
var m = inputData[1]

var map: [[Int]] = []
for _ in 0..<n{
    map.append(readLine()!.map {Int(String($0))!})
}



let dx: [Int] = [-1,1,0,0] // 북 남 서 동
let dy: [Int] = [0,0,-1,1]
var nx: Int = 0
var ny: Int = 0


func bfs(x: Int, y: Int) -> Int{
    var queue = [(Int,Int)]()
    queue.append((x,y))
    while !queue.isEmpty{
        let dir = queue.removeFirst()
        for i in 0..<4{
            nx = dir.0 + dx[i]
            ny = dir.1 + dy[i]
            if nx < 0 || nx >= n || ny < 0 || ny >= m{
                continue
            }
            if map[nx][ny] == 0{
                continue
            }
            if map[nx][ny] == 1{
                map[nx][ny] = map[dir.0][dir.1] + 1
                queue.append((nx,ny))
            }
        }
    }
    return map[n-1][m-1]
}

print(bfs(x: 0, y: 0))
