import SwiftUI

struct StoreView: View {
    var body: some View {
        NavigationView {
            VStack (spacing:20){
                Image(uiImage: UIImage(named: "Smartshoplogo")!)
                    .resizable()
                    .scaledToFit()
                    .frame(width: 750, height: 220)
                    .padding(.top)

                Spacer()

                VStack (spacing: -70){
                    Spacer().frame(height: 10)

                    NavigationLink(destination: RecipeSelectionView(storeId: 1)) {
                        Image(uiImage: UIImage(named: "willys")!)
                            .resizable()
                            .aspectRatio(contentMode: .fit)
                            .frame(width: 155, height: 100)
                    }
                    .buttonStyle(ImageButtonStyle())
                    .padding(.top)

                    NavigationLink(destination: RecipeSelectionView(storeId: 2)) {
                        Image(uiImage: UIImage(named: "ica")!)
                            .resizable()
                            .aspectRatio(contentMode: .fit)
                            .frame(width: 75, height: 100)
                    }
                    .buttonStyle(ImageButtonStyle())
                    .padding()

                    NavigationLink(destination: RecipeSelectionView(storeId: 3)) {
                        Image(uiImage: UIImage(named: "coop")!)
                            .resizable()
                            .aspectRatio(contentMode: .fit)
                            .frame(width: 120, height: 100)
                    }
                    .buttonStyle(ImageButtonStyle())
                    .padding()
                }
            }
            .padding()
        }
    }
}
struct CartItem: Identifiable {
    let id = UUID()
    let productName: String
    let productPrice: Double
}
struct Ingredient: Identifiable, Hashable, Codable {
    let id = UUID()
    let productName: String
    let productPrice: Double
    let storeName: String

    enum CodingKeys: String, CodingKey {
        case productName
        case productPrice
        case storeName
    }

    func hash(into hasher: inout Hasher) {
        hasher.combine(id)
    }
}

struct CartView: View {
    let ingredients: [Ingredient] // Assuming Ingredient is your data model for each item in the cart

    var body: some View {
        NavigationView {
            ScrollView {
                VStack (spacing: 10){
                    ForEach(ingredients) { ingredient in
                        VStack {
                            Text("Store: \(ingredient.storeName)")
                            Text("Item: \(ingredient.productName)")
                            Text("Price: \(ingredient.productPrice, specifier: "%.2f"):-")
                        }
                        .padding()
                        .background(Color.white)
                        .cornerRadius(8)
                        .shadow(radius: 3)
                    }
                    Spacer()
                }
                .padding(.top,255)
                .padding()
                .frame(maxHeight: 400)
            }
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .principal) {
                Text("Recipe Ingredients")
                    .font(.title)
                    .foregroundColor(.black)
                }
            }
            .padding()
        }
    }
}

struct RecipeSelectionView: View {
    let storeId: Int
    let recipes = ["Hamburgare", "Tacos", "Kyckling roma", "Pasta med räkor och curry"] // Add more recipes

    var body: some View {
        List(recipes, id: \.self) { recipe in
            NavigationLink(destination: RecipeCalculationDetailView(recipe: recipe, storeId: storeId)) {
                Text(recipe)
            }
        }
        .navigationTitle("Select Recipe")
    }
}
struct TotalPriceResponse: Codable {
    let totalPrice: Double
    let ingredients: [Ingredient]
}

struct RecipeCalculationDetailView: View {
    let recipe: String
    let storeId: Int

    @State private var totalPrice: Double = 0
    @State private var productName: String = ""
    @State private var productPrice: Double = 0
    @State private var cartItems: [CartItem] = []
    @State private var ingredients: [Ingredient] = []
    @State private var showCartView = false

    var formattedTotalPrice: String {
        return String(format: "%.2f", totalPrice)
    }

    var body: some View {
        VStack {
            Image(uiImage: storeImage(for: storeId))
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: 200, height: 150)

            Text("Total Price: \(formattedTotalPrice)")
                .padding()

            Button("Calculate Total Price") {
                calculateTotalPrice()
            }
            .padding()

            Button("Recipe Details") {
                showCartView = true
            }
            .padding()

            NavigationLink(destination: CartView(ingredients: ingredients), isActive: $showCartView) {
                            EmptyView()
            }
            .hidden()
        }
        .onAppear {
            calculateTotalPrice()

            cartItems.append(CartItem(productName: productName, productPrice: productPrice))
            ingredients = cartItems.map { cartItem in Ingredient(productName: cartItem.productName, productPrice: productPrice, storeName: "" )}
        }
        .navigationTitle(recipe)
        .padding()
    }

    func calculateTotalPrice() {
        guard let url = URL(string: "http://127.0.0.1:5000/calculate/totalprice/\(storeId)/\(recipe)") else {
            print("Invalid URL")
            return
        }

        URLSession.shared.dataTask(with: url) { data, response, error in
            guard let data = data else {
                print("No data")
                return
            }
            print("Received data:", String(data: data, encoding: .utf8) ?? "Unable to decode data")

            do {
                let decoder = JSONDecoder()
                let totalPriceResponse = try decoder.decode(TotalPriceResponse.self, from: data)
                DispatchQueue.main.async {
                    self.totalPrice = totalPriceResponse.totalPrice
                    self.ingredients = totalPriceResponse.ingredients
                }
            } catch {
                print("Error decoding total price data: \(error)")
            }
        }.resume()
    }
}


func storeImage(for storeId: Int) -> UIImage {
    let imageName: String
    switch storeId {
    case 1:
        imageName = "willys"
    case 2:
        imageName = "ica"
    case 3:
        imageName = "coop"
    default:
        imageName = "default"
    }
    if let imagePath = Bundle.main.path(forResource: imageName, ofType: "png") {
        return UIImage(contentsOfFile: imagePath) ?? UIImage(named: "default")!
    } else {
        return UIImage(named: "default")!
    }
}
struct ProductDetailView: View {
    let ingredient: Ingredient

    var body: some View {
        VStack {
            Text(ingredient.productName)
            Text("$\(ingredient.productPrice, specifier: "%.2f")")
        }
        .padding()
        .navigationTitle("Product Detail")
        .padding()
    }
}

struct ImageButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .padding()
            .opacity(configuration.isPressed ? 0.5 : 1.0) // Dim button when pressed
    }
}

struct Calculate: PreviewProvider {
    static var previews: some View {
        StoreView()
    }
}
