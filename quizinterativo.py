print('Seja bem vindo ao quiz "Master do Python"!')
print("Para cada pergunta, responda A, B ou C")

def fazer_pergunta(pergunta, alternativa_correta, nivel):
    print(f"\nNível: {nivel}")
    resposta = input(pergunta + " ")
    if resposta.strip().lower() == alternativa_correta.lower():
        print("A resposta está correta! ✔️")
        return 1
    else:
        print(f"""Resposta errada ✖️  ! A alternativa correta era: {alternativa_correta}""")
        return 0
    
def exibir_resultado(pontuacao, total_perguntas):
    print("\n 📊 Resultado final: ")
    print(f"Você acertou {pontuacao} de {total_perguntas} perguntas!")

    percentual = (pontuacao / total_perguntas) * 100

    if percentual == 100:
        print("Parabéns! Você é um verdadeiro Master do Python! 🥇")
    elif percentual >= 60:
        print("Muito bem! Você está no caminho certo! 🥈")
    else:
        print("Continue estudando, em breve você vai arrasar! 🥉")

pontuacao_total = 0
total_perguntas = 0

perguntas = [
    {"pergunta": "Qual comando usamos para criar uma função em Python?", "resposta": "def", "nivel": "fácil"},
    {"pergunta": "O que significa DRY na programação?", "resposta": "Don't Repeat Yourself", "nivel": "difícil"},
    {"pergunta": "Qual é a palavra-chave para retornar um valor em Python?", "resposta": "return", "nivel": "fácil"},
    {"pergunta": "Como chamamos uma função com nome e valor nos argumentos?", "resposta": "Argumento nomeado", "nivel": "médio"},
    {"pergunta": "Como evitar repetir código desnecessariamente em várias partes?", "resposta": "Usando funções", "nivel": "médio"},
    {"pergunta": "Qual o operador lógico que representa 'ou' em Python?", "resposta": "or", "nivel": "fácil"}
]

for item in perguntas:
    ponto = fazer_pergunta(
        pergunta = item["pergunta"],
        alternativa_correta = item["resposta"],
        nivel = item["nivel"]
    )
    pontuacao_total += ponto
    total_perguntas += 1

exibir_resultado(pontuacao = pontuacao_total, total_perguntas = total_perguntas)