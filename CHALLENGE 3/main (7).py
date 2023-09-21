def linearsearchproduct(productlist, targetproduct):
    indices = []

    for index, product in enumerate(productlist):
        if product == targetproduct:
            indices.append(index)

    return indices

# Example usage:
products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
result = linearsearchproduct(products, target)
print(result)