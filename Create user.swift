import SwiftUI
import Foundation

struct Iphone1415ProMax2: View {
    @State private var firstName: String = ""
    @State private var lastName: String = ""
    @State private var username: String = ""
    @State private var email: String = ""
    @State private var password: String = ""
    @State private var repeatPassword: String = ""
    @State private var showAlert = false
    @State private var alertMessage = ""
    
    var passwordsMatch: Bool {
        return password == repeatPassword
    }
    
    var body: some View {
        NavigationView {
            VStack (spacing: 10){
                Spacer().frame(height: 69)
                Text("Create Account")
                    .font(.title)
                    .padding()
                
                TextField("First Name", text: $firstName)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .padding()
                    .background(Color.white)
                    .cornerRadius(10)
                    .font(.system(size: 26))
                    .padding(.horizontal)
                
                
                TextField("Last Name", text: $lastName)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .padding()
                    .font(.system(size: 26))
                    .background(Color.white)
                    .cornerRadius(10)
                    .padding(.horizontal)
                
                TextField("Username", text: $username)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .padding()
                    .background(Color.white)
                    .cornerRadius(10)
                    .padding(.horizontal)
                    .font(.system(size: 26))
                
                TextField("Email", text: $email)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .padding()
                    .background(Color.white)
                    .cornerRadius(10)
                    .padding(.horizontal)
                    .font(.system(size: 26))
                
                SecureField("Password", text: $password)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .padding()
                    .background(Color.white)
                    .cornerRadius(10)
                    .padding(.horizontal)
                    .font(.system(size: 26))
                
                SecureField("Repeat Password", text: $repeatPassword)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .padding()
                    .background(Color.white)
                    .cornerRadius(10)
                    .padding(.horizontal)
                    .font(.system(size: 26))
                
                if !passwordsMatch {
                    Text("Passwords do not match")
                        .foregroundColor(.red)
                }
                
                Spacer()
                
                Button(action: createUser) {
                    Text("Create Account")
                        .padding()
                        .frame(maxWidth: 170)
                        .background(Color.blue)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .padding(.horizontal)
                }
                
                NavigationLink(destination: Iphone1415ProMax3().navigationBarBackButtonHidden(true)) {
                    
                    Text("Login")
                        .padding()
                        .frame(maxWidth: 170)
                        .background(Color.blue)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .padding(.horizontal)
                }
                .padding(.top)
                .navigationBarBackButtonHidden(true)
                
                Spacer()}
            .alert(isPresented: $showAlert) {
                Alert(title: Text("Error"), message: Text(alertMessage), dismissButton: .default(Text("OK")))
            }
            .frame(width: 430, height: 110)
            .background(Color.white)
            .navigationBarTitle("")
            .navigationBarHidden(true)
            .onAppear {
                UITableView.appearance().backgroundColor = .clear
            
            }
            .padding(.top, -100)
        }
    }
    
    func createUser() {
        guard passwordsMatch else {
            showAlert(message: "Passwords do not match")
            return
        }
        
        guard !firstName.isEmpty, !lastName.isEmpty, !username.isEmpty, !email.isEmpty, !password.isEmpty, !repeatPassword.isEmpty else {
            showAlert(message: "All fields are required")
            return
        }
        
        guard password == repeatPassword else {
            showAlert(message: "Passwords do not match")
            return
        }
        let userData: [String: String] = [
            "förnamn": firstName,
            "efternamn": lastName,
            "användarnamn": username,
            "mail": email,
            "lösenord": password,
            "upprepa_lösenord": repeatPassword
        ]
        
        guard let jsonData = try? JSONSerialization.data(withJSONObject: userData) else {
            showAlert(message: "Failed to encode user data")
            return
        }
        let url = URL(string: "http://127.0.0.1:5000/create_user")!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = jsonData
        
        // Perform the HTTP request
        URLSession.shared.dataTask(with: request) { data, response, error in
            guard let httpResponse = response as? HTTPURLResponse, (200...299).contains(httpResponse.statusCode) else {
                showAlert(message: "Failed to create user")
                return
            }
            
            
            showAlert(message: "User created successfully")
        }.resume()
    }
    
    func showAlert(message: String) {
        alertMessage = message
        showAlert = true
    }
    
    struct UserRegistrationView_Previews: PreviewProvider {
        static var previews: some View {
            Iphone1415ProMax2()
        }
    }
}

struct Create_user: PreviewProvider {
    static var previews: some View {
        Iphone1415ProMax2()
            .modelContainer(for: Item.self, inMemory: true)
        }
    }
