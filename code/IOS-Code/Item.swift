//
//  Item.swift
//  SmartShop IOS
//
//  Created by Oliver Brantin on 2024-04-21.
//

import Foundation
import SwiftData

@Model
final class Item {
    var timestamp: Date

    init(timestamp: Date) {
        self.timestamp = timestamp
    }
}
