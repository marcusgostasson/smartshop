import SwiftUI

struct Iphone1415ProMax1: View {
    @State private var username: String = ""
    @State private var password: String = ""
    @State private var showAlert = false
    @State private var alertMessage = ""
    @State private var loggedIn: Bool? = false

    var body: some View {
        NavigationView {
            ZStack {
                Color.white
                    .edgesIgnoringSafeArea(.all)

                VStack {
                    Image(uiImage: UIImage(named: "Smartshoplogo")!)
                        .resizable()
                        .scaledToFit()
                        .frame(width: 750, height: 220)
                        .padding(.top)

                    VStack {
                        Spacer().frame(height: 70)
                        TextField("Användarnamn", text: $username)
                            .padding()
                            .background(Color.white)
                            .cornerRadius(10)
                            .font(.system(size: 23))
                            .padding(.horizontal, 10)
                            .textFieldStyle(PlainTextFieldStyle())
                            .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray,lineWidth: 1 ))
                            .padding(25)

                        SecureField("Lösenord", text: $password)
                            .padding()
                            .background(Color.white)
                            .cornerRadius(10)
                            .font(.system(size: 23))
                            .padding(.horizontal, 10)
                            .textFieldStyle(PlainTextFieldStyle())
                            .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray,lineWidth: 1 ))
                            .padding(25)

                        Spacer().frame(height: 50)

                        Button(action: {
                            authenticateUser()
                        }) {
                            Text("Logga in")
                                .padding()
                                .frame(maxWidth: 170)
                                .background(Color.blue)
                                .foregroundColor(.white)
                                .cornerRadius(10)
                                .padding(.horizontal)
                        }
                        .padding(.bottom, 1)
                        .navigationBarBackButtonHidden(true)

                        NavigationLink(
                            destination: Iphone1415ProMax3(),
                            tag: true,
                            selection: $loggedIn)  {
                            EmptyView()
                        }

                        NavigationLink(destination: Iphone1415ProMax2())  {
                            Text("Skapa konto")
                                .padding()
                                .frame(maxWidth: 170)
                                .background(Color.blue)
                                .foregroundColor(.white)
                                .cornerRadius(10)
                                .padding(.horizontal)
                                .padding(.bottom, 85)
                        }
                        .padding(.top)
                        .navigationBarBackButtonHidden(true)
                    }
                    .padding(.horizontal)
                    .navigationBarTitle("")
                    .navigationBarHidden(true)
                }
                .frame(width: 430, height: 132)
            }
            .ignoresSafeArea(.keyboard)
        }
        .background(Color.white)
        .edgesIgnoringSafeArea(.all)
        .alert(isPresented: $showAlert) {
            Alert(title: Text("Error"), message: Text(alertMessage), dismissButton: .default(Text("OK")))
        }
    }

    func authenticateUser() {
        guard let url = URL(string: "http://127.0.0.1:5000/login") else {
            print("Invalid URL")
            return
        }

        let body: [String: String] = [
            "användarnamn": username,
            "lösenord": password
        ]

        guard let jsonData = try? JSONSerialization.data(withJSONObject: body) else {
            print("Failed to encode request body")
            return
        }

        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = jsonData

        URLSession.shared.dataTask(with: request) { data, response, error in
            guard let data = data else {
                print("No data")
                return
            }

            do {
                let response = try JSONDecoder().decode(LoginResponse.self, from: data)
                if response.message == "Login successful" {
                    DispatchQueue.main.async {
                        loggedIn = true

                    }
                } else {
                    DispatchQueue.main.async {
                        showAlert = true
                        alertMessage = "Invalid username or password"
                    }
                }
            } catch {
                print("Error decoding response: \(error)")
            }
        }.resume()
    }
}

struct LoginResponse: Decodable {
    let message: String
}

struct Login_Previews: PreviewProvider {
    static var previews: some View {
        Iphone1415ProMax1()
    }
}
