<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:00ff41,50:008f11,100:00ff41&height=240&section=header&text=Master%20do%20Python&fontSize=62&fontColor=000&fontAlignY=42&animation=twinkling&desc=Teste%20seus%20conhecimentos%20em%20Python%20no%20terminal&descAlignY=65&descSize=16"/>

<br/>

![Python](https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=00ff41)
![Terminal](https://img.shields.io/badge/Terminal-000000?style=for-the-badge&logo=gnometerminal&logoColor=00ff41)
![Status](https://img.shields.io/badge/RODANDO-000000?style=for-the-badge&logoColor=00ff41)
![Perguntas](https://img.shields.io/badge/6_PERGUNTAS-000000?style=for-the-badge&logoColor=00ff41)

</div>

<br/>

```
███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗     ██████╗  ██████╗ 
████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗    ██╔══██╗██╔═══██╗
██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝    ██║  ██║██║   ██║
██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗    ██║  ██║██║   ██║
██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║    ██████╔╝╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝

██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗                     
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║                     
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║                     
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║                     
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║                     
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝                     
```

<br/>

---

## SOBRE O PROJETO

Quiz interativo de Python executado diretamente no **terminal**, desenvolvido para testar e consolidar conhecimentos sobre funções, operadores, boas práticas e conceitos fundamentais da linguagem.

O programa apresenta 6 perguntas divididas em três níveis de dificuldade — fácil, médio e difícil — e ao final calcula a pontuação do usuário com feedback personalizado baseado no desempenho.

<br/>

---

## TECNOLOGIAS

<div align="center">

| | Tecnologia | Versão | Função |
|:---:|:---:|:---:|:---|
| ◈ | Python | 3.x | Linguagem principal |
| ◈ | Biblioteca padrão | — | `input()`, `print()`, funções nativas |

</div>

<br/>

---

## FUNCIONALIDADES

<details>
<summary><b>◈ Sistema de Perguntas</b></summary>
<br/>

- 6 perguntas sobre conceitos fundamentais de Python
- Cada pergunta exibe o nível de dificuldade antes da resposta: **fácil**, **médio** ou **difícil**
- Validação case-insensitive — `DEF`, `def` e `Def` são todos aceitos

</details>

<details>
<summary><b>◈ Placar e Resultado</b></summary>
<br/>

- Pontuação acumulada ao longo de todas as perguntas
- Cálculo de percentual de acertos ao final
- Feedback personalizado em 3 faixas de desempenho:
  - 100% — Master do Python
  - 60% ou mais — No caminho certo
  - Abaixo de 60% — Continue estudando

</details>

<details>
<summary><b>◈ Temas Abordados no Quiz</b></summary>
<br/>

- Declaração de funções com `def`
- Retorno de valores com `return`
- Argumentos nomeados
- Princípio DRY (*Don't Repeat Yourself*)
- Operadores lógicos (`or`)
- Boas práticas de reutilização de código com funções

</details>

<br/>

---

## APRENDIZADOS

<details>
<summary><b>◈ Funções como Unidade de Organização</b></summary>
<br/>

O projeto inteiro gira em torno do uso de funções para separar responsabilidades: `fazer_pergunta()` cuida da interação com o usuário, enquanto `exibir_resultado()` processa e apresenta o desempenho final — cada função com uma única responsabilidade clara.

</details>

<details>
<summary><b>◈ Argumentos Nomeados na Prática</b></summary>
<br/>

O projeto usa *keyword arguments* de forma consistente nas chamadas das funções, tornando o código mais legível e menos suscetível a erros de ordem de parâmetros.

```python
ponto = fazer_pergunta(
    pergunta=item["pergunta"],
    alternativa_correta=item["resposta"],
    nivel=item["nivel"]
)
```

</details>

<details>
<summary><b>◈ Iteração sobre Lista de Dicionários</b></summary>
<br/>

As perguntas são armazenadas como uma lista de dicionários — estrutura expressiva e fácil de expandir. Adicionar uma nova pergunta é apenas adicionar um novo item à lista, sem alterar nenhuma lógica existente.

```python
perguntas = [
    {"pergunta": "...", "resposta": "...", "nivel": "fácil"},
    # novas perguntas aqui
]
```

</details>

<details>
<summary><b>◈ Princípio DRY Aplicado</b></summary>
<br/>

Em vez de repetir a lógica de verificação para cada pergunta, toda a validação vive dentro de `fazer_pergunta()`. O loop `for` chama a função para cada item da lista — o código cresce em dados, não em repetição.

</details>

<details>
<summary><b>◈ f-strings e Formatação de Saída</b></summary>
<br/>

Uso de f-strings para interpolação dinâmica de variáveis nas mensagens do terminal — sintaxe mais limpa e eficiente do que concatenação de strings.

```python
print(f"Você acertou {pontuacao} de {total_perguntas} perguntas!")
```

</details>

<br/>

---

## COMO EXECUTAR

```
PASSO 1   Certifique-se de ter Python 3.x instalado
PASSO 2   Clone o repositório
PASSO 3   Execute o arquivo principal no terminal
PASSO 4   Responda cada pergunta e pressione Enter
PASSO 5   Veja sua pontuação final
```

**Rodando localmente:**

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/master-do-python.git

# Entre na pasta
cd master-do-python

# Execute o quiz
python quiz.py
```

<br/>

---

## LICENÇA

**Permissão de Uso:** O código pode ser usado somente para fins educacionais.

**Modificação e Distribuição:** Qualquer pessoa pode modificar e redistribuir o código — na forma original ou modificada — desde que cite os autores originais.

**Inclusão da Licença:** Ao redistribuir, a licença original e o aviso de direitos autorais devem ser incluídos no código-fonte ou na documentação.

**Isenção de Garantia:** O software é fornecido "como está", sem garantias de qualquer tipo, explícitas ou implícitas. Os autores não se responsabilizam por danos decorrentes do uso.

<br/>

---

## AUTOR

<div align="center">

<br/>

Desenvolvido por **[Caetano Bordin](https://github.com/Caetano-2012)**

<br/>

![Visitor Badge](https://visitor-badge.laobi.icu/badge?page_id=seu-usuario.master-do-python&left_color=black&right_color=00cc33&left_text=visitas)

<br/>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:00ff41,50:008f11,100:00ff41&height=120&section=footer&animation=twinkling"/>

</div>
