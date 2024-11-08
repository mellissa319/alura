# conversor.py

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def mostrar_menu():
    print("\nEscolha a conversão desejada:")
    print("1. Celsius para Fahrenheit e Kelvin")
    print("2. Fahrenheit para Celsius e Kelvin")
    print("3. Kelvin para Celsius e Fahrenheit")
    print("4. Sair")

def main():
    while True:
        mostrar_menu()
        escolha = input("Digite o número da opção: ")

        if escolha == '1':
            celsius = float(input("Digite a temperatura em Celsius: "))
            print(f"{celsius}°C = {celsius_para_fahrenheit(celsius)}°F")
            print(f"{celsius}°C = {celsius_para_kelvin(celsius)} K")
        elif escolha == '2':
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            print(f"{fahrenheit}°F = {fahrenheit_para_celsius(fahrenheit)}°C")
            print(f"{fahrenheit}°F = {fahrenheit_para_kelvin(fahrenheit)} K")
        elif escolha == '3':
            kelvin = float(input("Digite a temperatura em Kelvin: "))
            print(f"{kelvin} K = {kelvin_para_celsius(kelvin)}°C")
            print(f"{kelvin} K = {kelvin_para_fahrenheit(kelvin)}°F")
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
