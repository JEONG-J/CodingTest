//
//  main.swift
//  SwiftCoding
//
//  Created by 정의찬 on 2023/03/08.
//

import Foundation

let n = Int(readLine()!)
var MergeString:String
var cnt:Int = 0

for h in 0...n!{
    for m in 0..<60{
        for s in 0..<60{
            MergeString = String(h) + String(m) + String(s)
            if MergeString.contains("3"){
                cnt += 1
            }
        }
    }
}

print(cnt)
