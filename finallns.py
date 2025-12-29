from colorama import *

python_votes = 0
java_votes = 0
cpp_votes = 0

n = int(input(Fore.BLUE+"Chand nafar ray midan ?"+Fore.RESET))
print(Fore.YELLOW+"\nRay khod ra vared konid: ")
print("1: Python")
print("2: Java")
print("3: C++"+Fore.RESET)

for i in range(n):
    vote = int(input(Fore.MAGENTA+"Entekhab shoma: "))

    if vote == 1:
        python_votes += 1
    elif vote == 2:
        java_votes += 1
    elif vote == 3:
        cpp_votes += 1
    else:
        print("Ray namotabar !")

total_votes = python_votes + java_votes + cpp_votes
python_percent = int((python_votes / total_votes) * 100)
java_percent = int((java_votes / total_votes) * 100)
cpp_percent = int((cpp_votes / total_votes) * 100)

print("\n---------------")
print(Fore.LIGHTCYAN_EX+"Natije nazarsanji: ")
print(f"({'python': <8}) | {python_percent: <3}%")
print(f"{'java':<8} | {java_percent:<3}%")
print(f"{'c++': <8} | {cpp_percent:<3}%")
print("---------------")
print(Fore.CYAN + "Nemodar matni:")
print(f"{'Python:':<8} | {'*' * python_votes}")
print(f"{'Java:':<8} | {'*' * java_votes}")
print(f"{'C++:':<8} | {'*' * cpp_votes}" + Fore.RESET)
print("---------------")