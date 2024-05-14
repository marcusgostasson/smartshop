import SwiftUI

// Rename the struct to avoid redeclaration error
struct NewIngredient {
    var name: String
    var quantity: Int
}
extension String: Identifiable {
    public var id: String { self }
}

struct CreateRecipeView: View {
    @State private var recipeName = ""
    @State private var ingredients: [String] = []
    @State private var selectedIngredient: String? = nil
    @State private var steps: [String] = []
    @State private var newStep = ""
    @State private var searchText = ""
    @State private var showIngredientList = false

    var filteredIngredients: [String] {
        if searchText.isEmpty {
            return ingredients
        } else {
            return ingredients.filter { $0.localizedCaseInsensitiveContains(searchText) }
        }
    }

    var body: some View {
        VStack {
            TextField("Recipe Name", text: $recipeName)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()

            Divider()

            Text("Ingredients")
                .font(.headline)
                .padding(.vertical, -2)
                .padding(.horizontal, -12)

            ScrollView {
                LazyVStack {
                    ForEach(filteredIngredients, id: \.self) { ingredient in
                        Button(action: {
                            selectedIngredient = ingredient
                        }) {
                            Text(ingredient)
                                .padding()
                        }
                    }
                }
            }
            .frame(height: 160)

            HStack {
                TextField("Search", text: $searchText)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .padding()

                Button("Search") {
                    showIngredientList = true

                }
                Spacer()
            }

            Divider()

            Text("Steps")
                .font(.headline)
                .padding(.vertical,-2)
                .padding(.horizontal)

            List {
                ForEach(steps, id: \.self) { step in
                    Text(step)
                }
                .onDelete(perform: removeStep)
            }

            HStack {
                TextField("New Step", text: $newStep)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                Button(action: addStep) {
                    Image(systemName: "plus.circle.fill")
                        .foregroundColor(.blue)
                }
            }
            .padding()

            Spacer()

            Button(action: saveRecipe) {
                Text("Save Recipe")
                    .padding()
                    .frame(maxWidth: .infinity)
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }
            .padding()
        }
        .padding()
        .navigationBarTitle("Create Recipe", displayMode: .inline)
        .onAppear {
            fetchIngredients()
        }
        .sheet(item: $selectedIngredient) { ingredient in
            Text("You selected \(ingredient)")
        }
    }
    struct IngredientListView: View {
        @Binding var searchText: String
        var ingredients: [String]

        var filteredIngredients: [String] {
            if searchText.isEmpty {
                return ingredients
            } else {
                return ingredients.filter { $0.localizedCaseInsensitiveContains(searchText) }
            }
        }

        var body: some View {
            VStack {
                TextField("Search", text: $searchText)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .padding()

                ScrollView {
                    LazyVStack {
                        ForEach(filteredIngredients, id: \.self) { ingredient in
                            Button(action: {
                                // Handle ingredient selection
                            }) {
                                Text(ingredient)
                                    .padding()
                            }
                        }
                    }
                }
            }
            .padding()
            .navigationBarTitle("Ingredients")
        }
    }


    func fetchIngredients() {
        guard let url = URL(string: "http://127.0.0.1:5000/ingredients") else {
            print("Invalid URL")
            return
        }

        URLSession.shared.dataTask(with: url) { data, response, error in
            guard let data = data else {
                print("No data")
                return
            }

            do {
                let ingredientNames = try JSONDecoder().decode([String].self, from: data)
                DispatchQueue.main.async {
                    ingredients = ingredientNames
                }
            } catch {
                print("Error decoding data: \(error)")
            }
        }.resume()
    }

    func addStep() {
        if !newStep.isEmpty {
            steps.append(newStep)
            newStep = "" // Clear the text field after adding the step
        }
    }

    func removeStep(at offsets: IndexSet) {
        steps.remove(atOffsets: offsets)
    }

    func saveRecipe() {
        // Implement saving the recipe
    }
}

struct CreateRecipeView_Previews: PreviewProvider {
    static var previews: some View {
        CreateRecipeView()
    }
}
