import SwiftUI

struct FlowersView: View {
    var body: some View {
        NavigationView {
            VStack (spacing:20){
                Image(uiImage: UIImage(named: "Smartshoplogo")!)
                    .resizable()
                    .scaledToFit()
                    .frame(width: 750, height: 220)
                    .padding(.top)

                Image(uiImage: UIImage(named: "flowers")!)
                    .resizable()
                    .scaledToFit()
                    .frame(width: 550, height: 200)
                    .padding()

                VStack (spacing: -70){
                    Spacer().frame(height: 10)

                    NavigationLink(destination: FlowersSelectionView(storeId: 1)) {
                        Image(uiImage: UIImage(named: "willys")!)
                            .resizable()
                            .aspectRatio(contentMode: .fit)
                            .frame(width: 155, height: 100)
                    }
                    .buttonStyle(ImageButtonStyle())
                    .padding(.top)

                    NavigationLink(destination: FlowersSelectionView(storeId: 2)) {
                        Image(uiImage: UIImage(named: "ica")!)
                            .resizable()
                            .aspectRatio(contentMode: .fit)
                            .frame(width: 75, height: 100)
                    }
                    .buttonStyle(ImageButtonStyle())
                    .padding()

                    NavigationLink(destination: FlowersSelectionView(storeId: 3)) {
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

struct FlowersSelectionView: View {
    let storeId: Int
    let flowers = ["Roser 9p 40cm", "Roser 7p 35cm", "Other flowers"]

    var body: some View {
        ScrollView {
            VStack {
                ForEach(flowers, id: \.self) { flower in
                    NavigationLink(destination: FlowerDetailView(flower: flower)) {
                        Text(flower)
                    }
                }
            }
        }
        .navigationTitle("Select Flower")
    }
}

struct FlowerDetailView: View {
    let flower: String // Assuming this is the name of the flower

    var body: some View {
        VStack {
            Text(flower)
                .font(.title)
                .padding()

            // Add more details about the flower here if needed
        }
        .navigationTitle(flower)
        .padding()
    }
}

func storeImageFlowers(for storeId: Int) -> UIImage {
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


struct FlowersView_Previews: PreviewProvider {
    static var previews: some View {
        FlowersView()
    }
}
