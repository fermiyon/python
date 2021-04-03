class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def isPrime(num):
    liste = range(1,num + 1)
    filtered = list(filter(lambda x: num % x == 0,liste))
    print(f"{bcolors.OKCYAN}{num} is divisible by {filtered}{bcolors.ENDC}")
    if len(filtered) == 2:
        return True
    else:
        return False
def main():
    again = True
    while again:
        num_input = int(input("Check this number: "))
        if isPrime(num_input):
            print(f"{bcolors.OKGREEN}{num_input} is a prime number{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}{num_input} is not a prime number{bcolors.ENDC}")
        
        restart = input("Type 'yes' to control another number. Otherwise type 'no' \n").lower()
        if restart != "yes":
            again = False
            print("Goodbye!")

main()