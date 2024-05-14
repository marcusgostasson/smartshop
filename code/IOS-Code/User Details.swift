import SwiftUI
import Foundation

struct UserDetailView: View {
    var förnamn: String
    var efternamn: String
    var användarnamne: String
    var mail: String

    var body: some View {
        ZStack {
            Color.clear

            VStack(spacing: 22) {
                Rectangle()
                    .foregroundColor(.white)
                    .frame(width: 300, height: 0)
                    .background(.green)
                    .cornerRadius(20)
                    .offset(x: 1, y: -10)
                    .overlay(
                        VStack(spacing: 16) {
                            Text("Användarnamn")
                                .font(.title)
                            Text(förnamn)
                                .font(.title)
                            Text("______________________________")
                            Text("Förnamn")
                                .font(.title)
                            Text(förnamn)
                                .font(.title)
                            Text("______________________________")
                            Text("Efternamn")
                                .font(.title)
                            Text(efternamn)
                                .font(.title)
                            Text("______________________________")
                            Text("Mail")
                                .font(.title)
                            Text(mail)
                                .font(.title)
                            Text("______________________________")
                        }
                        .foregroundColor(.black)
                        .padding()
                        )



                Rectangle()
                    .foregroundColor(.white)
                          .frame(width: 130, height: 40)
                          .background(.white)
                          .cornerRadius(20)
                          .offset(x: 0, y: 330.4)
                          .overlay(
                              Text("Logga ut")
                                  .foregroundColor(.black)
                                  .offset(x: 1,  y: 330.4) // Adjust the offset as needed
                          )
                  }
                  .padding()

              }
              .frame(width: 430, height: 932)
              .background(Color(red: 0.97, green: 0.67, blue: 0.08))
          }
      }
#Preview {
    UserDetailView(förnamn: "", efternamn: "", användarnamne: "", mail: "")
        .modelContainer(for: Item.self, inMemory: true)
}
