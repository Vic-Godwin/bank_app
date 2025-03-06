products =['phone', 'tablet', 'laptop', 'journal']

print(f'Current Products in carts: {products}\n')

remove_item = input('Enter item to remove: ').lower()
products.remove(remove_item)
print(f'{remove_item} has been removed from cart\nNew Cart is {products}\n')

add_item = input('Enter item to add: ').lower()
add_index = input('Where; before which product do you want the item: ').lower()
products.insert(products.index(add_index), add_item)
print(f'{add_item} has been added to cart before {add_index}.\n\nUpdated Cart: {products}')