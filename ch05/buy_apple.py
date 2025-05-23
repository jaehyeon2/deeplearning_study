from layer_naive import MulLayer

apple = 100
apple_num = 2
tax = 1.1

# forward
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

apple_price = mul_apple_layer.forward(apple, apple_num)
price = mul_tax_layer.forward(apple_price, tax)

print(price)

# backward
d_price = 1
d_apple_price, d_tax = mul_tax_layer.backward(d_price)
d_apple, d_apple_num = mul_apple_layer.backward(d_apple_price)

print(d_apple, d_apple_num, d_tax)