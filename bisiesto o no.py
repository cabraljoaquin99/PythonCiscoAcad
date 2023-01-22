import calendar

# Pedimos al usuario que ingrese el año
year = input("Ingresa el año: ")

# Comprobamos si el año es bisiesto
if calendar.isleap(int(year)):
  print(f"{year} es un año bisiesto.")
else:
  print(f"{year} no es un año bisiesto.")