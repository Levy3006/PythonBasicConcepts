

def sales_price(item_and_price):
    item = ""
    price = ""
    item_and_price = item_and_price.split()

    for x in item_and_price:
        
        
        if x.isnumeric():
            item+= x + " "
        else:
            price+= x
    return "Item: {} Price: ${}".format(item, price)

print(sales_price("Carro 41"))           

