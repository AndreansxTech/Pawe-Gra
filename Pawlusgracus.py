print("Historia o Wyrębickim")
int(input("Wstęp Napisz 1 i enter odpowiedzi pisz z małych liter"))
Początek=input("Czy chcesz zacząć tą jakże interesującą historie? [t/n]")
if Początek =="t":
    print("Bardzo się cieszę")
if Początek =="n":
    print("hamie jeden")
    exit()
print("rozdział 1")
rozdziałI=input("Paweł proponuje ci wyjście na basen Idziesz? [T/N]")
if rozdziałI =="t":
    print("Paweł się cieszy i cię ściska tak że się prawie zeżygałeś")
if rozdziałI =="n":
    print("Paweł się zdenerwował i cię zmażdża")
if rozdziałI=="t":
    print("PRZYGOTOWANIE NA BASEN")
elif rozdziałI=="n":
    print("Bad ending")
    exit()
Przygotowanienabasen=input("Co bierzesz? Kebab/kąpielówki")
if Przygotowanienabasen=="kebab":
    print("Paweł się ucieszył więc jednak idziecie po 2 metrowego kebaba jak Paweł wpierdolił go całego był zadowolony")
if Przygotowanienabasen=="kebab":
    print("GOOD ENDING PAWEŁ ZADOWOLONY")
    exit()
if Przygotowanienabasen=="kąpielówki":
    print("Idziecie spokojnie na basen")
if Przygotowanienabasen=="kąpielówki":
    print("BASEN")
Basen = input("Czy kupujesz bilet? [T/N]")
if Basen == "t":
    print("Normalnie wchodzisz na basen")
elif Basen == "n":
    print("Ochroniaż to zauważył i zadzwonił po policję (jebany konfident)")
    print("Police ending")
    exit() 
Mainstory = input("Fajnie się bawicie dopóki Pawłowi się zachciało srać. Co robisz? [mówię żeby poszedł się wysrać/nic z tym nie robię]")
if Mainstory == "mówię żeby poszedł się wysrać":
    pass
else:
    pass
    print("Paweł nie zdążył i się zesrał w basenie")
if Mainstory=="Nic z tym nie robię":
    print("Paweł nie zdążył i się zesrał w basenie")
if Mainstory=="mówię żeby poszedł się wysrać":
    print("Paweł nie zdążył i zesrał się w basenie i Ochrona nas wywala z basenu CAGO ENDING")
if Mainstory=="Nic z tym nie robię":
    print("Paweł się zesrał w basenie i Ochrona was wywala CAGO ENDING")
