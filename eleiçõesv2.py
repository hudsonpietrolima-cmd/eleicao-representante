
e = 1
ana = 0
bruno = 0
carlos = 0
branco = 0

print("Bem vindo ao sistema de eleição de representante de turma! Vote em um dos candidatos abaixo: ")

while e == 1:
    print("================================ELEIÇÃO DO REPRESENTANTE=================================")
    print("1 - Votar em Ana ........................................................................")
    print("2 - Votar em Bruno ......................................................................")
    print("3 - Votar em Carlos .....................................................................")
    print("4 - Votar em branco .....................................................................")
    print("5 - Consultar resultado parcial .........................................................")
    print("6 - Encerrar ............................................................................")

    es =  int(input("\nEscolha uma das opções acima: "))

    if es == 1:
        ana += 1
        print("\n\033[32mVoto cadastrado!\033[0m")

    elif es == 2:
        bruno += 1
        print("\n\033[32mVoto cadastrado!\033[0m")

    elif es == 3:
        carlos += 1
        print("\n\033[32mVoto cadastrado!\033[0m")

    elif es == 4:
        branco += 1
        print("\n\033[32mVoto cadastrado!\033[0m")

    elif es == 5:
        print(f"\nAna === {ana} votos")
        print(f"Bruno === {bruno} votos")
        print(f"Carlos === {carlos} votos")
        print(f"Branco === {branco} votos")

    elif es == 6:
        print("\nVotação encerrada!")

        print("====================================RESULTADOS FINAIS====================================")
        print(f"\nAna === {ana} votos")
        print(f"Bruno === {bruno} votos")
        print(f"Carlos === {carlos} votos")
        print(f"Branco === {branco} votos")

        if ana > bruno and ana > carlos and ana > branco:
            print("\n\033[33mCandidato vencedor === ANA\033[0m")

        elif bruno > carlos and bruno > ana and bruno > branco:
            print("\n\033[33mCandidato vencedor === BRUNO\033[0m")

        elif carlos > bruno and carlos > ana and carlos > branco:
            print("\n\033[33mCandidato vencedor === CARLOS\033[0m")

        elif branco > ana and branco > carlos and branco > bruno:

            if ana > bruno and ana > carlos:
                print("\n\033[33mCandidato vencedor === ANA\033[0m")

            elif bruno > carlos and bruno > ana:
                print("\n\033[33mCandidato vencedor === BRUNO\033[0m")

            elif carlos > bruno and carlos > ana:
                print("\n\033[33mCandidato vencedor === CARLOS\033[0m")

        elif ana == bruno and ana == carlos and bruno == carlos:
            print("\n\033[33mEMPATE TRIPLO!\033[0m")

        else:
            print("\n\033[33mHOUVE EMPATE!\033[0m")

        break

    else:
        print("Valor errado!")