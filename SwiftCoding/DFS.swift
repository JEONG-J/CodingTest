//
//  main.swift
//  SwiftCoding
//
//  Created by 정의찬 on 2023/03/09.
//

import Foundation

var visited = Array(repeating: false, count: 9)

var graph:[[Int]] = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,5],[7],[2,6,8],[1,7]]

func dfs(_ start:Int){
    visited[start] = true
    print(start, terminator: " ")
    for i in graph[start]{
        if !visited[i]{
            dfs(i)
        }
    }
}

dfs(1)
print()
