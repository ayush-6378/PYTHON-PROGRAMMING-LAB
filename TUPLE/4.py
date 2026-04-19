food=[("burger",150),("pizza",450),("fries",80)]
food.sort(key=lambda x: x[1], reverse=True)
print("sorted by price (descending):", food)
