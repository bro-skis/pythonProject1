def main():
    print('please enter temperature in farenheit:')
    farh = float(input())
    cel = farh_to_celcius(farh)
    print(farh, 'Farenheit is', cel, 'Celcius')


def farh_to_celcius(F):
    C = (F - 32) * 5/9
    return C

main()