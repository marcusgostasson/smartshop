import SwiftUI

struct RecipeSelectionViewComp1: View {
    @State private var isLoading = false
    @State private var recipes: [RecipeWrapper] = []
    
    var body: some View {
        NavigationView {
            if isLoading {
                ProgressView("Loading...")
            } else {
                List {
                    ForEach(recipes, id: \.self) { recipeWrapper in
                        NavigationLink(destination: RecipeCalculationDetailViewComp(recipe: recipeWrapper.recipeName, storeId: 1)) {
                            Text(recipeWrapper.recipeName)
                        }
                    }
                }
                .navigationTitle("Select Recipe")
            }
        }
        .onAppear {
            fetchRecipesComp()
        }
    }
    
    struct RecipeItemView: View {
        let recipe: String
        
        var body: some View {
            Text(recipe)
                .font(.title)
                .fontWeight(.bold)
                .padding()
                .border(Color.gray, width: 1)
                .cornerRadius(8)
        }
    }
    struct RecipeWrapper: Hashable {
        let recipeName: String
    }
    
    
    struct RecipeOptionViewComp: View {
        let recipe: RecipeWrapper
        let onIngredientsTapped: () -> Void
        let onStepsTapped: () -> Void
        
        var body: some View {
            VStack {
                VStack {
                    Text("\(recipe.recipeName)")
                        .padding()
                    Spacer()
                }
                Button(action: {
                    onIngredientsTapped()
                }) {
                    Text("Ingredients")
                }
                .padding()
                Button(action: {
                    onStepsTapped()
                }) {
                    Text("Steps")
                }
                .padding()
            }
        }
    }
    
    
    
    func fetchRecipesComp() {
        isLoading = true
        
        guard let url = URL(string: "http://127.0.0.1:5000/recipe") else {
            print("Invalid URL")
            isLoading = false
            return
        }
        
        URLSession.shared.dataTask(with: url) { data, response, error in
            guard let data = data else {
                print("No data")
                isLoading = false
                return
            }
            
            do {
                let recipeNames = try JSONDecoder().decode([String].self, from: data)
                recipes = recipeNames.map { RecipeWrapper(recipeName: $0) }
                
                isLoading = false
            } catch {
                print("Error decoding data: \(error)")
                isLoading = false
            }
        }.resume()
    }
}

struct RecipeWrapperComp: Codable, Identifiable {
    var id = UUID()
    var recipeName: String
}

struct ContentViewComp: View {
    var body: some View {
        RecipeSelectionViewComp1()
    }
}

struct StoreViewComp: View {
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
struct CartItemComp: Identifiable {
    let id = UUID()
    let productName: String
    let productPrice: Double
}
struct IngredientComp: Identifiable, Hashable, Codable {
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

struct CartViewComp: View {
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

struct RecipeSelectionViewComp: View {
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
struct TotalPriceResponseComp: Codable {
    let totalPrice: Double
    let ingredients: [Ingredient]
}

struct RecipeCalculationDetailViewComp: View {
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
            NavigationLink(destination: RecipeCalculationDetailView(recipe: recipe, storeId: 1)) {
                Image(uiImage: UIImage(named: "willys")!)
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .frame(width: 185, height: 100)
            }
            .buttonStyle(ImageButtonStyle())
            .padding(.top)
            
            Text("Total Price: \(formattedTotalPrice)")
                .padding()
            
            NavigationLink(destination: RecipeCalculationDetailView(recipe: recipe, storeId: 2)) {
                Image(uiImage: UIImage(named: "ica")!)
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .frame(width: 135, height: 100)
            }
            .buttonStyle(ImageButtonStyle())
            .padding(.top)
            
            Text("Total Price: \(formattedTotalPrice)")
                .padding()
            
            NavigationLink(destination: RecipeCalculationDetailView(recipe: recipe, storeId: 3)) {
                Image(uiImage: UIImage(named: "coop")!)
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .frame(width: 195, height: 100)
            }
            .buttonStyle(ImageButtonStyle())
            .padding(.top)
            
            Text("Total Price: \(formattedTotalPrice)")
                .padding()
            
            
            
            
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
            calculateTotalPriceComp(for: 3)
            
            
            
            cartItems.append(CartItem(productName: productName, productPrice: productPrice))
            ingredients = cartItems.map { cartItem in Ingredient(productName: cartItem.productName, productPrice: productPrice, storeName: "" )}
        }
        .navigationTitle(recipe)
        .padding()
    }
    
    func calculateTotalPriceComp(for storeid: Int) {
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



func storeImageComp(for storeId: Int) -> UIImage {
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
struct ProductDetailViewComp: View {
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

struct ImageButtonStyleComp: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .padding()
            .opacity(configuration.isPressed ? 0.5 : 1.0) // Dim button when pressed
    }
}

struct Comparison: PreviewProvider {
    static var previews: some View {
        RecipeSelectionViewComp1()
    }
}
