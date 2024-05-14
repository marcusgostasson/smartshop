import SwiftUI

struct ChatMessage: Identifiable {
    var id = UUID()
    var text: String
    var isUser: Bool
}

struct Recipe: Codable, Identifiable {
    let id = UUID()
    let name: String
    let ingredients: [String]
}

struct RecipeDetailsView: View {
    let recipe: Recipe
    
    var body: some View {
        VStack {
            Text(recipe.name)
                .font(.title)
                .padding()
            
            ScrollView {
                Text(recipe.ingredients.map { "• \($0)" }.joined(separator: "\n"))
                    .padding()
            }
        }
        .navigationBarTitle(recipe.name)
    }
}

struct ChatbotView: View {
    @State private var messages: [ChatMessage] = []
    @State private var userInput: String = ""
    @State private var recipes: [Recipe] = []
    @State private var isFirstMessage = true
    @State private var selectedRecipe: Recipe?
    @State private var recipeSteps: [String: [String]] = [:]

    private func addMessage(_ message: String, isUser: Bool) {
        messages.append(ChatMessage(text: message, isUser: isUser))
    }

    private func sendMessage() {
        guard !userInput.isEmpty else { return }
        addMessage(userInput, isUser: true)
        
        if isFirstMessage {
            addMessage("Chefbot: What ingredients do you have at home today?", isUser: false)
            isFirstMessage = false
        } else {
            let lowercasedInput = userInput.lowercased()
            
            if let recipe = recipes.first(where: { $0.name.lowercased() == userInput.lowercased() }) {
                selectedRecipe = recipe
                addMessage("Chefbot: Here are the ingredients for \(recipe.name): \(recipe.ingredients.joined(separator: ", "))", isUser: false)
                if let steps = recipeSteps[recipe.name] {
                    addMessage("Chefbot: Now, here are the steps to make \(recipe.name):", isUser: false)
                    for (index, step) in steps.enumerated() {
                        addMessage("\(index + 1). \(step)", isUser: false)
                    }
                } else {
                    addMessage("Chefbot: Sorry, I couldn't find the steps to make \(recipe.name).", isUser: false)
                }
            } else {
                let ingredients = userInput.components(separatedBy: ",").map { $0.trimmingCharacters(in: .whitespaces) }
                let recipeMatches = checkIngredients(ingredients)
                if recipeMatches.isEmpty {
                    addMessage("Chefbot: I couldn't find any recipes with \(userInput). Could you specify other ingredients?", isUser: false)
                } else {
                    for match in recipeMatches {
                        let missingIngredients = match.additionalIngredients.filter { !ingredients.contains($0.lowercased()) }
                        addMessage("Chefbot: Your ingredients match with \(match.recipe). Additional ingredients needed: \(missingIngredients.joined(separator: ", "))", isUser: false)
                    }
                }
                addMessage("Chefbot: Which recipe would you like to cook today?", isUser: false)
            }
        }
        userInput = ""
    }

    private func checkIngredients(_ ingredients: [String]) -> [(recipe: String, additionalIngredients: [String])] {
        var matches: [(recipe: String, additionalIngredients: [String])] = []
        
        for recipe in recipes {
            let matchingIngredients = recipe.ingredients.filter { ingredients.contains($0.lowercased()) }
            if !matchingIngredients.isEmpty {
                let additionalIngredients = recipe.ingredients.filter { !ingredients.contains($0.lowercased()) }
                matches.append((recipe.name, additionalIngredients))
            }
        }
        
        return matches
    }

    var body: some View {
        NavigationView {
            VStack {
                ScrollView {
                    VStack(alignment: .leading, spacing: 10) {
                        ForEach(messages) { message in
                            Text(message.text)
                                .padding(10)
                                .background(message.isUser ? Color.blue : Color.green)
                                .foregroundColor(.white)
                                .cornerRadius(10)
                                .frame(maxWidth: .infinity, alignment: message.isUser ? .trailing : .leading)
                        }
                    }
                    .padding()
                }
                
                HStack {
                    TextField("Type your message", text: $userInput)
                        .padding()
                        .background(Color.gray.opacity(0.1))
                        .cornerRadius(10)
                    
                    Button(action: sendMessage) {
                        Text("Send")
                            .padding()
                            .background(Color.blue)
                            .foregroundColor(.white)
                            .cornerRadius(10)
                    }
                    .padding(.trailing)
                }
                .padding()
            }
            .navigationBarTitle("Chefbot")
            .onAppear {
                addMessage("Chefbot: Hello smartshopper!", isUser: false)
                loadRecipes()
                loadRecipeSteps()
            }
            .sheet(item: $selectedRecipe) { recipe in
                RecipeDetailsView(recipe: recipe)
            }
        }
    }
    
    private func loadRecipeSteps() {
        guard let url = Bundle.main.url(forResource: "recipesteps", withExtension: "json") else {
            print("Unable to locate recipesteps.json")
            return
        }
        
        do {
            let data = try Data(contentsOf: url)
            let decoder = JSONDecoder()
            decoder.keyDecodingStrategy = .convertFromSnakeCase
            self.recipeSteps = try decoder.decode([String: [String]].self, from: data)
            
            for (recipeName, steps) in recipeSteps {
                print("\(recipeName): \(steps)")
            }
        } catch {
            print("Error loading recipe steps from JSON: \(error)")
        }
    }
    

    private func loadRecipes() {
        guard let url = Bundle.main.url(forResource: "recipes", withExtension: "json") else {
            print("Unable to locate recipes.json")
            return
        }
        
        do {
            let data = try Data(contentsOf: url)
            let decoder = JSONDecoder()
            decoder.keyDecodingStrategy = .convertFromSnakeCase
            let recipeData = try decoder.decode([String: [Recipe]].self, from: data)
            if let recipes = recipeData["recipes"] {
                self.recipes = recipes
            } else {
                print("No recipes found in JSON")
            }
        } catch {
            print("Error loading recipes from JSON: \(error)")
        }
    }
}

struct ChatbotView_Previews: PreviewProvider {
    static var previews: some View {
        ChatbotView()
    }
}
