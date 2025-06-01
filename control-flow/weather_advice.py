weather_type = input("What's the weather like today? (sunny/rainy/cold:)").lower()

if weather_type == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_type == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_type == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")