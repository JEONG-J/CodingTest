//
//  main.swift
//  SwiftCoding
//
//  Created by 정의찬 on 2023/03/08.
//

import Foundation



    let inputData = readLine()!.split(separator: " ").map { Int(String($0))!}
    let n = Int(inputData[0])
    let m = Int(inputData[1])
    
    let xydir = readLine()!.split(separator: " ").map { Int(String($0))!}
    var x = Int(xydir[0])
    var y = Int(xydir[1])
    var dir = Int(xydir[2])
    
    var d:[[Int]] = Array(repeating: Array(repeating: 0, count: m), count: n)
    d[x][y] = 1
    
    
    var map: [[Int]] = []
    
    for _ in stride(from: 0, to: n, by: 1){
        map.append(readLine()!.split(separator: " ").map {Int(String($0))!})
    }
    
    // dx dy 정의
    let dx:[Int] = [-1,0,1,0]
    let dy:[Int] = [0,-1,0,1]
    
    func turn(){
        dir -= 1
        if dir == -1{
            dir = 3
        }
    }
    
    var cnt:Int = 1
    var turn_cnt:Int = 0
    var nx:Int = 0
    var ny:Int = 0
    
    while true{
        turn()
        nx = x + dx[dir]
        ny = y + dy[dir]
        if (d[nx][ny] == 0 && map[nx][ny] == 0){
            d[nx][ny] = 1
            cnt += 1
            x = nx
            y = ny
            turn_cnt = 0
        } else{
            turn_cnt += 1
        }
        if (turn_cnt == 4){
            nx = x - dx[dir]
            ny = y - dy[dir]
            if (map[nx][ny] == 0){
                x = nx
                y = ny
            } else{
                break
            }
            turn_cnt = 0
        }
    }
