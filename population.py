#population={"India":143,"China":140,"Pakistan":25}
#print(population)
population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}
def print_all():
    for country,p in population.items():
        print(f"{country}==>{p}")

def add():
    country=input("Enter country name to add: ")
    country=country.lower()
    if country in population:
        print("Country already exists in our database.Terminating")
        return
    p=input(f"Enter population for {country}: ")
    p=float(p)
    population[country]=p
    print_all()

def remove():
    country=input("Enter the country to remove: ")
    if country not in population:
        print("Country is not in the database.Terminating.")
        return
    del population[country]
    print_all()

def querry():
    country=input("Enter the name of the country: ")
    if country not in population:
        print("Country not in our database.Terminating.")
        return
    print(f"Population of {country} is: {population[country]} crore")

def main():
    op = input("Enter operations(add,remove,querry or print): ")
    if op.lower()=='add':
        add()
    elif op.lower()=='remove':
        remove()
    elif op.lower()=='querry':
        querry()
    else:
        print_all()

if __name__ == '__main__':
    main()