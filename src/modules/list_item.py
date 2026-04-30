from pathlib import Path
import time
import os 
import json
import sys



def remove_itens():
    caminho_atual = Path(__file__).resolve()

    pasta_modules = caminho_atual.parent
    
    pasta_src = pasta_modules.parent

    pasta_principal = pasta_src.parent

    pasta_data = pasta_principal / "data"

    arquivo_json = pasta_data / "initial_data.json"

    if os.path.exists(arquivo_json):
        with open(arquivo_json, 'r', encoding='utf8') as f:
            data_base_json = json.load(f)
            for data in data_base_json:
                print(f"\nID: {data['id']}")
                print(f"NAME: {data['nome']}")
                print(f"QUANTITY : {data['quantidade']}") 
    else:
        return 1




if __name__ == "__main__":
    remove_itens()
