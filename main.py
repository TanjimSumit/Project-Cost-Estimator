def main():
    material = float(input("Material Cost: "))
    labor = float(input("Labor Cost: "))
    overhead = float(input("Overhead Cost: "))
    total = material + labor + overhead
    print("Total Project Cost:", total)

    choice = input("Calculate Profit? (y/n): ")
    if choice.lower() == 'y':
        selling = float(input("Selling Price: "))
        print("Profit:", selling - total)

if __name__ == "__main__":
    main()
