class Personagem:
    def __init__(self, nome, descricao, link_imagem, programa, animador):
        self.nome = nome
        self.descricao = descricao
        self.link_imagem = link_imagem
        self.programa = programa
        self.animador = animador

personagens_cadastrados = []

def mostrar_menu():
    print("=== MENU ===")
    print("1 - Registrar personagem")
    print("2 - Visualizar personagens cadastrados")
    print("3 - Sair")

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite o nome do personagem: ")
        descricao = input("Digite a descrição do personagem: ")
        link_imagem = input("Digite o link para imagem do personagem: ")
        programa = input("Digite o programa do personagem: ")
        animador = input("Digite o nome do animador responsável pelo personagem: ")
        personagem = Personagem(nome, descricao, link_imagem, programa, animador)
        personagens_cadastrados.append(personagem)
        print("Personagem registrado com sucesso!")
    elif escolha == "2":
        print("Personagens cadastrados:")
        for personagem in personagens_cadastrados:
            print(f"Nome: {personagem.nome}, Descrição: {personagem.descricao}, Link para Imagem: {personagem.link_imagem}, Programa: {personagem.programa}, Animador: {personagem.animador}")
    elif escolha == "3":
        recomecar = input("Deseja recomeçar? (S/N): ")
        if recomecar.lower() == "s":
            personagens_cadastrados = []
            print("Reiniciando...")
        else:
            print("Saindo...")
            break
    else:
        print("Opção inválida. Tente novamente.")
        continue
