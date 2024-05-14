import SwiftUI


struct IngredientsResponse: Decodable {
    struct Ingredient: Identifiable, Decodable {
        var id = UUID()
        var storeName: String
        var productName: String
        var productPrice: Double
        
        enum CodingKeys: String, CodingKey {
            case storeName, productName, productPrice
        }
    }
    
    var ingredients: [Ingredient]?
        
}

extension IngredientsResponse.Ingredient: Hashable {
    func hash(into hasher: inout Hasher) {
        hasher.combine(storeName)
        hasher.combine(productName)
        hasher.combine(productPrice)    }
}

struct Iphone1415ProMax3: View {
    @State private var recipes: [RecipeWrapper] = []
    @State private var isLoading = false
    @State private var selectedRecipe: RecipeWrapper? = nil
    @State private var ingredients: [[String : String]] = []
    @State private var showIngredientsView = false
    
    var body: some View {
        ZStack {
            Color.white.edgesIgnoringSafeArea(.all)
            
            NavigationView {
                VStack {
                    Text("Your Recipies")
                        .font(.largeTitle)
                        .fontWeight(.bold)
                        .padding(.top,1)
                    if isLoading {
                        ProgressView("Loading...")
                            .padding()
                    } else {
                        List {
                            ForEach(recipes) { recipe in
                                NavigationLink(
                                    destination: RecipeOptionView(
                                        recipe: recipe,
                                        onIngredientsTapped: {
                                            self.fetchRecipeDetails(recipe: recipe)
                                        },
                                        onStepsTapped: {
                                            self.fetchRecipeSteps(recipe: recipe)
                                        }
                                    )
                                ) {
                                    Text(recipe.recipeName)
                                }
                            }
                            .listRowBackground(Color.white)
                        }
                        .padding(.bottom,-85)
                    }
                    Spacer()
                    VStack {
                        Spacer()
                        // Store Button
                        NavigationLink(destination: StoreView()) {
                            Text("Stores")
                                .font(.custom("Canela",size: 28))
                                .fontWeight(.semibold)
                                .tracking(2)
                                .padding(.vertical, 15)
                                .frame(maxWidth: .infinity)
                              
                                .background(Color.white)
                                .foregroundColor(.black)
                                .cornerRadius(10)
                                .padding(.horizontal, 30)
                                .shadow(color: .black.opacity(0.1), radius: 5, x: 0, y: 2)
                                .padding(.bottom, -30)
                        }
                        .padding()
                        .padding(.top, 85)
                        
                        Spacer()
                        HStack(spacing:-60) {
                            Spacer()
                            
                            NavigationLink(destination: ChatbotView()) {
                                Text("Chefbot")
                                    .font(.headline)
                                    .padding()
                                    .frame(width: 150, height: 50)
                                    .background(Color.white)
                                    .foregroundColor(.black)
                                    .cornerRadius(10)
                                    .padding(.vertical, 15)
                                    .padding(.horizontal, 30)
                                    .shadow(color: .black.opacity(0.1), radius: 5, x: 0, y: 2)
                            }
                            .padding()
                            .padding(.bottom,-75)
                            
                            NavigationLink(destination: FlowersView()) {
                                Text("Flowers")
                                    .font(.headline)
                                    .padding()
                                    .frame(width: 150, height: 50)
                                    .background(Color.white)
                                    .foregroundColor(.black)
                                    .cornerRadius(10)
                                    .padding(.vertical, 15)
                                    .padding(.horizontal, 30)
                                    .shadow(color: .black.opacity(0.1), radius: 5, x: 0, y: 2)
                            }
                            .padding()
                            .padding(.bottom,-75)
                            
                            Spacer()
                        }
                        .padding()
                        .padding(.bottom)
                        
                        
                        HStack (spacing: -60){
                            Spacer()
                            
                            NavigationLink(destination: RecipeSelectionViewComp1()) {
                                Text("Comparison")
                                    .font(.headline)
                                    .padding()
                                    .frame(width: 150, height: 50)
                                    .background(Color.white)
                                    .foregroundColor(.black)
                                    .cornerRadius(10)
                                    .padding(.vertical, 15)
                                    .padding(.horizontal, 30)
                                    .shadow(color: .black.opacity(0.1), radius: 5, x: 0, y: 2)
                            }
                            .padding()
                            .padding(.bottom)
                            
                            
                            NavigationLink(destination: CreateRecipeView()) {
                                Text("Create Recipe")
                                    .font(.headline)
                                    .padding()
                                    .frame(width: 150, height: 50)
                                    .background(Color.white)
                                    .foregroundColor(.black)
                                    .cornerRadius(10)
                                    .padding(.vertical, 15)
                                    .padding(.horizontal, 30)
                                    .shadow(color: .black.opacity(0.1), radius: 5, x: 0, y: 2)
                            }
                            .padding()
                            .padding(.bottom)
                            Spacer()
                            
                        }
                        .padding()
                        .padding(.bottom,-30)
                        Spacer()
                    }
                }
            }
                    .padding()
                    .onAppear(perform: fetchRecipes)
                    .navigationBarTitle("", displayMode: .inline)
                    .background(Color.white)
                    .background(
                        Group {
                            if showIngredientsView {
                                IngredientsView(ingredients: ingredients.map { $0["productName"] ?? "" }, onRemove: removeIngredient)  {
                                    self.showIngredientsView = false
                                }
                            }
                        }
                    )
                }
            }
        
    
        
        
        func fetchRecipesBeta() {

            
            recipes.append(RecipeWrapper(recipeName: "Spaghetti Bolognese"))
            recipes.append(RecipeWrapper(recipeName: "Chicken Stir-Fry"))
            recipes.append(RecipeWrapper(recipeName: "Vegetable Curry"))
            recipes.append(RecipeWrapper(recipeName: "Olivers Bolognese"))
            recipes.append(RecipeWrapper(recipeName: "Emils Stir-Fry"))
            recipes.append(RecipeWrapper(recipeName: "Marcus Vegetable Curry"))
            recipes.append(RecipeWrapper(recipeName: "Rasmus wook69"))
            recipes.append(RecipeWrapper(recipeName: "Simons beef tartar"))
            recipes.append(RecipeWrapper(recipeName: "Red Curry"))
            recipes.append(RecipeWrapper(recipeName: "Spaghetti Bolognese"))
            recipes.append(RecipeWrapper(recipeName: "Healthy Burger"))
            recipes.append(RecipeWrapper(recipeName: "Healthy Curry"))
            recipes.append(RecipeWrapper(recipeName: "Healthy Bolognese"))
        }
    
        func fetchRecipes() {
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

        
        func fetchRecipeDetails(recipe: RecipeWrapper) {
            guard let recipeName = recipe.recipeName.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) else {
                return
            }
            
            guard let url = URL(string: "http://127.0.0.1:5000/recipe/ingredients/\(recipeName)") else {
                print("Invalid URL")
                return
            }
            
            URLSession.shared.dataTask(with: url) { data, response, error in
                guard let data = data else {
                    print("No data")
                    return
                }
                
                do {
                    let ingredientsResponse = try JSONDecoder().decode(IngredientsResponse.self, from: data)
                    if let ingredients = ingredientsResponse.ingredients {
                        DispatchQueue.main.async {
                            let alertController = UIAlertController(title: "Ingredients", message: nil, preferredStyle: .alert)
                            for ingredient in ingredients {
                                let ingredientString = "\(ingredient.productName) - \(ingredient.productPrice)"
                                let button = UIAlertAction(title: ingredientString, style: .default) { _ in
                                    // Handle button action if needed
                                }
                                button.setValue(UIImage(systemName: "minus.circle"), forKey: "image")
                                alertController.addAction(button)
                            }
                            alertController.addAction(UIAlertAction(title: "Cancel", style: .cancel, handler: nil))
                            UIApplication.shared.windows.first?.rootViewController?.present(alertController, animated: true, completion: nil)
                        }
                    } else {
                        print("Ingredients data is nil")
                    }
                } catch {
                    print("Error decoding ingredients data: \(error)")
                }
            }.resume()
        }
        
        func fetchRecipeSteps(recipe: RecipeWrapper) {
            guard let recipeName = recipe.recipeName.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) else {
                return
            }
            
            guard let url = URL(string: "http://127.0.0.1:5000/recipe/steps/\(recipeName)") else {
                print("Invalid URL")
                return
            }
            
            URLSession.shared.dataTask(with: url) { data, response, error in
                guard let data = data else {
                    print("No data")
                    return
                }
                
                do {
                    let stepsResponse = try JSONDecoder().decode(StepsResponse.self, from: data)
                    if let steps = stepsResponse.steps {
                        DispatchQueue.main.async {
                            let stepView = RecipeStepView(step: steps, onClose: {
                                // Dismiss the alert when the "Close" button is tapped
                                UIApplication.shared.windows.first?.rootViewController?.dismiss(animated: true, completion: nil)
                            })
                            let alert = UIAlertController(title: "Recipe Step", message: nil, preferredStyle: .alert)
                            alert.setValue(UIHostingController(rootView: stepView), forKey: "contentViewController")
                            UIApplication.shared.windows.first?.rootViewController?.present(alert, animated: true, completion: nil)
                        }
                        
                    } else {
                        print("Steps data is nil")
                    }
                } catch {
                    print("Error decoding steps data: \(error)")
                }
            }.resume()
        }
        
        func removeIngredient(ingredientToRemove: String) {
            if let index = ingredients.firstIndex(where: { $0["productName"] == ingredientToRemove }) {
                ingredients.remove(at: index)
                
                showIngredientsView = true
            }
        }
    }
    
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            Iphone1415ProMax3()
        }
    }
    
    struct IngredientsView: View {
        var ingredients: [String]
        var onRemove: (String) -> Void
        var onClose: () -> Void // Closure to handle closing the view
        
        var body: some View {
            VStack(alignment: .leading) {
                Text("Ingredients:")
                    .font(.headline)
                    .padding()
                ScrollView {
                    VStack(alignment: .leading, spacing: 8) {
                        ForEach(ingredients, id: \.self) { ingredient in
                            HStack {
                                Text(ingredient)
                                    .onTapGesture {}
                                Spacer()
                                Button(action: {
                                    onRemove(ingredient)
                                    
                                }) {
                                    Image(systemName: "minus.circle")
                                }
                                .foregroundColor(.red)
                            }
                        }
                    }
                    .padding()
                }
                Button("Close") {
                    onClose()
                }
                .padding()
            }
            .background(Color.white)
            .cornerRadius(10)
            .shadow(radius: 5)
            .padding()
        }
    }
    
    struct RecipeOptionView: View {
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
    
    struct RecipeStepView: View {
        let step: String
        let onClose: () -> Void // Add onClose argument
        
        var body: some View {
            VStack {
                Text(step)
                    .padding()
                Button(action: {
                    onClose() // Call onClose when the button is tapped
                }) {
                    Text("Close")
                }
                .padding()
            }
        }
    }
    
    struct RecipeWrapper: Codable, Identifiable {
        var id = UUID()
        var recipeName: String
    }
    
    struct StepsResponse: Codable {
        var steps: String?
    }
    struct Main_Screen: PreviewProvider {
        static var previews: some View {
            Iphone1415ProMax3()
                .modelContainer(for: Item.self, inMemory: true)
        }
    }
