"""Gerenciador simples de tarefas (linha de comando).

Este script demonstra um gerenciador de tarefas minimalista que roda no
terminal. As tarefas são mantidas em memória como uma lista de dicionários
com as chaves `title` (texto da tarefa) e `done` (boolean indicando se a
tarefa foi concluída).

Funcionalidades:
- listar tarefas com um indicador tipo checkbox ([ ] ou [X])
- adicionar uma tarefa
- remover uma tarefa por número ou por título
- marcar uma ou várias tarefas como concluídas (sem removê-las)

Uso:
Execute o script e responda às perguntas no terminal. As operações são
simples e demonstrativas — o estado não é persistido entre execuções.

Arquivo: `main.py`
"""

tarefas = [
    {"title": "Comprar leite", "done": False},
    {"title": "Lavar o carro", "done": False},
    {"title": "Estudar para a prova", "done": False},
]


def mostrar_tarefas():
    """Imprime as tarefas numeradas com checkbox [ ] ou [X].

    Cada linha mostra: índice (1-based), checkbox e título da tarefa.
    O checkbox exibe `X` quando `done` é True e espaço em branco caso
    contrário. Usamos índice 1-based para a interação com o usuário
    (mais natural para humanos que programadores).
    """
    if not tarefas:
        print("Nenhuma tarefa na lista.")
        return
    for i, t in enumerate(tarefas, 1):
        status = 'X' if t['done'] else ' '
        print(f"{i}. [{status}] {t['title']}")


def adicionar_tarefa(titulo: str):
    """Adiciona uma nova tarefa à lista.

    O parâmetro `titulo` é stripado pelo chamador; a tarefa passa a ter
    `done=False` por padrão.
    """
    tarefas.append({"title": titulo, "done": False})


def remover_tarefa_por_titulo(titulo: str) -> bool:
    """Remove a tarefa que coincida exatamente com `titulo`.

    Retorna True se encontrou e removeu a tarefa, False caso contrário.
    A comparação é sensível a maiúsculas/minúsculas; para buscas mais
    flexíveis, normalize `titulo` antes de chamar a função.
    """
    for t in tarefas:
        if t['title'] == titulo:
            tarefas.remove(t)
            return True
    return False


def marcar_concluida_por_indices(indices):
    """Marca como concluídas as tarefas cujos índices (1-based) estão em `indices`.

    Ignora índices fora do intervalo. `indices` pode ser uma lista vazia.
    """
    for idx in indices:
        if 1 <= idx <= len(tarefas):
            tarefas[idx - 1]['done'] = True


# --- Fluxo interativo (passo a passo) ---
# Abaixo o script pergunta ao usuário em sequência: adicionar, remover e marcar.
# Para cada etapa, fazemos validações simples e mostramos a lista quando
# necessário para facilitar a operação.

print("Deseja adicionar alguma tarefa? (s/n)")
resposta = input().lower()  # normaliza a resposta para minúsculas

if resposta == 's':
    # lermos a tarefa, retiramos espaços nas laterais e adicionamos
    print("Digite a tarefa:")
    tarefa = input().strip()
    adicionar_tarefa(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")
else:
    print("Nenhuma tarefa adicionada.")


print("\nDeseja remover alguma tarefa? (s/n)")
resposta = input().lower()

if resposta == 's':
    # Mostramos a lista com índices para o usuário escolher a remoção
    print("Tarefas atuais:")
    mostrar_tarefas()
    print("Digite o número da tarefa que deseja remover (ou o título):")
    entrada = input().strip()

    # Se o usuário digitou um número, removemos por índice; caso contrário,
    # tentamos remover por título exato.
    removed = False
    if entrada.isdigit():
        idx = int(entrada)
        if 1 <= idx <= len(tarefas):
            removed_title = tarefas[idx - 1]['title']
            tarefas.pop(idx - 1)
            print(f"Tarefa '{removed_title}' removida com sucesso!")
            removed = True
    else:
        if remover_tarefa_por_titulo(entrada):
            print(f"Tarefa '{entrada}' removida com sucesso!")
            removed = True

    if not removed:
        print("Tarefa não encontrada.")
else:
    print("Nenhuma tarefa removida.")


print("\nConcluiu alguma tarefa? (s/n)")
resposta = input().lower()  # normaliza a resposta para minúsculas
if resposta == 's':
    # Permitimos marcar múltiplas tarefas ao mesmo tempo fornecendo uma
    # lista de índices separados por vírgula (ex: 1,3,4).
    print("Tarefas (marque as concluídas):")
    mostrar_tarefas()
    print("Digite o número da(s) tarefa(s) concluída(s) separadas por vírgula (ex: 1,3):")
    entrada = input().strip()
    try:
        indices = [int(x) for x in entrada.split(',') if x.strip().isdigit()]
        marcar_concluida_por_indices(indices)
        print("Tarefas atualizadas.")
    except Exception:
        # Em caso de erro de parsing, apenas avisamos e mantemos o estado.
        print("Entrada inválida. Nenhuma alteração feita.")


# Exibe todas as tarefas (com status) ao final.
print("\nEssas são as tarefas atuais:")
mostrar_tarefas()