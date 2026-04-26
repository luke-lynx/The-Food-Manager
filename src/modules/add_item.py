from pathlib import Path
import json


def add_item():
    first_step_interface()
    name_iten =register_new_inventory_iten()
    second_step_interface(name_iten)


def register_new_inventory_iten():
    while True:
        name_iten = input("> Nome do Alimento: ")
        
        while True:
            try:
                quantity_iten = int(input("> Quantidade inicial: "))
                if quantity_iten >= 0:
                    break
                else:
                    print("Invalid Value : Please Type Again")
            except:
                print("Invalid Value : Please Type Again")

        confirm_data = input(f"Adicionar: {name_iten} com {quantity_iten} unidades?? Digite S/N: ").lower()
        if confirm_data in ["s","sim","y","yes"]:
            break
        else:
            pass
    with open(user_data_for_add_iten(), 'r', encoding='utf8') as f:
        dados = json.load(f)

    new_datas = {
        "id": len(dados) +1,
        "nome": name_iten,
        "quantidade": quantity_iten
    }

    dados.append(new_datas)

    with open(user_data_for_add_iten(), 'w', encoding='utf8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    return name_iten


def first_step_interface():
    print("")
    print("="*50)
    print("CADASTRO DE NOVO ALIMENTO".center(50))
    print("="*50)
    print("Digite os dados abaixo (ou 'S' para cancelar):\n")


def second_step_interface(nome):
    print("-"*50)
    print(f"[OK] '{nome}' adicionado com sucesso!")
    print("="*50)


def user_data_for_add_iten():
    caminho_atual = Path(__file__).resolve()

    pasta_modules = caminho_atual.parent
    
    pasta_src = pasta_modules.parent

    pasta_raiz = pasta_src.parent

    pasta_data = pasta_raiz / "data"

    arquivo_json = pasta_data / "user_data.json"
    return arquivo_json


if __name__ == "__main__":
    add_item()