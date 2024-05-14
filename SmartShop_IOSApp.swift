//
//  SmartShop_IOSApp.swift
//  SmartShop IOS
//
//  Created by Oliver Brantin on 2024-04-21.
//

import SwiftUI
import SwiftData

@main
struct SmartShop_IOSApp: App {
    var body: some Scene {
        WindowGroup {
            NavigationView {
                Iphone1415ProMax1() // Initial view
            }
            .navigationViewStyle(StackNavigationViewStyle()) // Optional: Use stack navigation style
        }
    }
}
