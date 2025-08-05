def adicionar_contato(nome, telefone, email):
    agenda_add = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    agenda.append(agenda_add)
    print(f"{nome} salvo na agenda com sucesso!")
    return

def visualizar_agenda():
    print(f"\nCONTATOS NA AGENDA:")
    for indice, contato in enumerate (agenda, start=1):
        favorito = "✓" if contato["favorito"] else " "
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. Nome: {nome} | Telefone: {telefone} | Email: {email} |Favorito:[{favorito}]")
        print("-"*40)
    return


def atualizar_contato(agenda, indice_agenda, novo_nome, novo_telefone, novo_email):
    indice_agenda_ajustado = indice_agenda - 1
    if indice_agenda_ajustado >= 0 and indice_agenda_ajustado < len(agenda):
        agenda[indice_agenda_ajustado]["nome"] = novo_nome
        agenda[indice_agenda_ajustado]["telefone"] = novo_telefone
        agenda[indice_agenda_ajustado]["email"] = novo_email
        print(f"Contato {novo_nome} atualizado.")
        print("-"*40)
    else:
        print("Índice de tarefa inválido.")
    return


def marcar_favorito(agenda, indice_contato):
    indice_agenda_ajustado = int(indice_contato) - 1
    agenda[indice_agenda_ajustado]["favorito"] = True
    print(f"\nContato {agenda[indice_agenda_ajustado]['nome']} marcado como favorito.")
    print("-"*40)
    return


def ver_favoritos():
    print(f"\nCONTATOS FAVORITOS:")
    encontrou_favorito = False
    for indice, contato in enumerate(agenda, start=1):
        if contato["favorito"]:
            favorito = "✓"
            nome = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            print(f"{indice}. {nome} | {telefone} | {email} |Favorito:[{favorito}]")
            print("-"*40)
            encontrou_favorito = True
    if not encontrou_favorito:
        print("Nenhum contato favorito encontrado.")
    return


def remover_contato(indice_contato):
    indice_agenda_ajustado = int(indice_contato) - 1 
    try:
        contato_removido = agenda.pop(indice_agenda_ajustado)
        print(f"Contato {contato_removido['nome']} removido com sucesso.")
        print("-"*40)
    except IndexError:
        print("Índice de contato inválido.")
        print("-"*40)
    return

agenda = []

while True:
    print("\n             MENU DE AGENDA")
    print("="*40)
    print("1. Adicionar Contato")
    print("2. Ver Contato")
    print("3. Atualizar Contato")
    print("4. Marcar contato como favorito")
    print("5. Mostrar favoritos")
    print("6. Remover contato")
    print("7. Sair")

    escolha = input("Digite sua escolha: ")
    if escolha == "1":
        nome = input("Nome: ").capitalize()
        telefone = input("Telefone: ")
        email = input("Email: ") 
        adicionar_contato(nome, telefone, email)
    
    if escolha == "2":
        visualizar_agenda()

    if escolha == "3":
        visualizar_agenda()
        indice_contato = int(input("Digite o indice do contato que deseja atualizar: "))
        novo_nome = input("Nome: ").capitalize()
        novo_tel = input("Telefone: ")
        novo_email = input("Email: ")
        atualizar_contato(agenda ,indice_contato, novo_nome, novo_tel, novo_email)
        
    if escolha == "4":
        visualizar_agenda()
        indice_contato = int(input("Indice do contato: "))
        marcar_favorito(agenda, indice_contato)

    if escolha == "5":
        ver_favoritos()

    if escolha == "6":
        visualizar_agenda()
        indice_contato = int(input("Digite o indice do contato que deseja remover: "))
        remover_contato(indice_contato)