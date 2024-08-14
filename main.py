from currency_converter import CurrencyConverter
from config import API_KEY

def main():
    converter = CurrencyConverter(API_KEY)
    
    while True:
        print("\033[92m==============================\033[0m")
        print("\033[92m=== Calculadora de Divisas ===\033[0m")
        print("\033[92m==============================\033[0m")
        print("\033[92m===                        ===\033[0m")
        print("\033[92m=== OPCIONES:              ===\033[0m")
        print("\033[92m===                        ===\033[0m")
        print("\033[92m=== 1. Convertir divisas   ===\033[0m")
        print("\033[92m=== 2. Salir               ===\033[0m")
        print("\033[92m===                        ===\033[0m")
        print("\033[92m==============================\033[0m")
        
        print("\n")
        
        choice = input("\033[92m ==> Elige una opción: \033[0m")
        
        if choice == '1':
            from_currency = input("\033[92m ==>Divisa de origen (por ejemplo, USD): \033[0m").upper()
            to_currency = input("\033[92m ==>Divisa de destino (por ejemplo, EUR): \033[0m").upper()
            try:
                amount = float(input(f"\033[92m ==>Cantidad en {from_currency}: \033[0m"))
                rate = converter.get_exchange_rate(from_currency, to_currency)
                if rate:
                    converted_amount = amount * rate
                    print(f"\033[92m{amount} {from_currency} = {converted_amount:.2f} {to_currency}\033[0m")
                else:
                    print("\033[91mError: No se pudo obtener la tasa de cambio.\033[0m")
            except ValueError:
                print("\033[91mError: La cantidad ingresada no es válida. Por favor, ingresa un número.\033[0m")
            
        elif choice == '2':
            print("\033[93mSaliendo de la calculadora...\033[0m")
            break
        else:
            print("\033[91mOpción no válida. Intenta de nuevo.\033[0m")
            print("\n")
            
if __name__ == "__main__":
    main()
