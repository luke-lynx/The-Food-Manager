

# The Food Manager

**Versão 0.1.3** | Lançamento Inicial (CLI)

# Nota de Atualização: Adicionada função de listagem de itens com CLI aprimorada.

Gerenciador de estoques de alimentos desenvolvido para simplificar o controle de inventário. Esta versão inicial estabelece a lógica central do sistema via terminal, priorizando a organização do código e o funcionamento das regras de negócio antes da implementação de interfaces gráficas.

## Sobre o Projeto

O objetivo do The Food Manager é fornecer uma ferramenta leve e direta para o controle de suprimentos. O programa opera inteiramente via linha de comando nesta fase, servindo como a fundação para uma futura plataforma multiplataforma.

### Funcionalidades v0.1.3
* **Cadastro de Itens:** Adicionar novos alimentos ao sistema com quantidade inicial.
[#CONCLUÍDO]

* **Remoção:** Excluir itens do registro de estoque.
[#CONCLUÍDO]

* **Ajuste de Saldo:** Funções específicas para aumentar ou diminuir a quantidade de itens.

* **Listagem:** Visualização completa de todos os alimentos e seus respectivos status.
[#CONCLUIDO]
## Desenvolvimento e Estabilidade

Nesta fase de lançamento, o foco total está na estabilidade das funções básicas (CRUD) e na qualidade da lógica de programação. 

* **Interface:** Command Line Interface (CLI).
* **Manutenção:** Versões incrementais (como a 0.1.1) serão lançadas para correções de bugs ou melhorias pontuais de desempenho.

## Planejamento Futuro (Roadmap)

O projeto será transformado em uma plataforma open source com o objetivo de alcançar as seguintes metas:

- [ ] **Expansão de Plataforma:** Versões para Web, Desktop (Windows/Linux) e Mobile (Android).
- [ ] **Exportação de Dados:** Geração de relatórios de estoque em formato PDF.
- [ ] **Identificação Visual:** Suporte para imagens dos itens para facilitar a gestão.
- [ ] **Abertura para Comunidade:** Código aberto para contribuições de outros desenvolvedores.

## Estrutura Inicial (Planejada)
```text
food_manager/
│── main.py
│── data/
│   └── estoque.json (ou .csv)
│── modules/
│   ├── add_item
│   ├── remove_item
│   ├── update_item
│   └── list_items
│── README.md

---
#OpenSource #SoftwareDevelopment #FoodManager #BuildInPublic




