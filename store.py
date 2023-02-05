first_item_price = float(input('first_item_price: '))
second_item_price = float(input('second_item_price: '))
is_customer_a_club_member = input('is_customer_a_club_member: ')
tax = 1.25
initial_price = first_item_price + second_item_price
num_of_purchases = (input('num_of_purchases: '))
base_price = 0

while(is_customer_a_club_member == True):
    base_price_1 = base_price - 10 / 100 * base_price
    if (num_of_purchases == 2):
        base_price_2 = first_item_price + 1 / 2 * second_item_price
    else:
        base_price = base_price
base_price_3 = base_price_2 + base_price_1
total_price = base_price_3 - tax * base_price_3

print(initial_price, base_price, total_price, sep = '\t')
