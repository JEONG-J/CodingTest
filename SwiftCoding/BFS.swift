//
//  File.swift
//  SwiftCoding
//
//  Created by 정의찬 on 2023/03/09.
//

import Foundation

var visited = Array(repeating: false, count: 9)

var graph:[[Int]] = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,5],[7],[2,6,8],[1,7]]

public struct Queue <T> {
    fileprivate var array = [T]()
    
    public var isEmpty: Bool{
        return array.isEmpty
    }
    
    public mutating func add(_ element: T) {
        array.append(element)
    }
    
    public mutating func dequeue() -> T?{
        if isEmpty{
            return nil
        } else {
            return array.removeFirst()
        }
    }
}

var queue = Queue<Int>()

func bfs(_ start:Int){
    queue.add(start)
    visited[start] = true
    
    while !queue.isEmpty{
        guard let v = queue.dequeue() else { return }
        print(v, terminator: " ")
        for i in graph[v]{
            if !visited[i]{
                queue.add(i)
                visited[i] = true
            }
        }
    }
}

bfs(1)
