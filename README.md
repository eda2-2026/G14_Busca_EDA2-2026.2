<h1 align="center">Busca_Medicamentos</h1>

<p align="center">
  Ferramenta de linha de comando que consulta o cadastro de medicamentos da Anvisa<br>
  e mostra, lado a lado, quantas comparações e quanto tempo cada algoritmo de busca gastou.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Tema-Algoritmos%20de%20Busca-1f4e79?style=flat-square" alt="Tema: algoritmos de busca">
  <img src="https://img.shields.io/badge/Registros-43.444-4a90a4?style=flat-square" alt="Base com 43.444 registros">
  <img src="https://img.shields.io/badge/Fonte-Dados%20abertos%20Anvisa-6aa84f?style=flat-square" alt="Fonte: Dados abertos da Anvisa">
</p>



```console
$ busca-medicamentos --nome "CLORIDRATO DE FLUOXETINA"

┌───────────┬──────────────────────────────────────────────┐
│ Campo     │ Valor                                        │
├───────────┼──────────────────────────────────────────────┤
│ Produto   │ CLORIDRATO DE FLUOXETINA                     │
├───────────┼──────────────────────────────────────────────┤
│ Registro  │ 100470290                                    │
├───────────┼──────────────────────────────────────────────┤
│ Situação  │ Ativo                                        │
├───────────┼──────────────────────────────────────────────┤
│ Categoria │ Genérico                                     │
├───────────┼──────────────────────────────────────────────┤
│ Classe    │ ANTIDEPRESSIVOS                              │
├───────────┼──────────────────────────────────────────────┤
│ Empresa   │ SANDOZ DO BRASIL INDÚSTRIA FARMACÊUTICA LTDA │
└───────────┴──────────────────────────────────────────────┘

┌────────────┬─────────────┬─────────┐
│ Algoritmo  │ Comparações │   Tempo │
├────────────┼─────────────┼─────────┤
│ sequencial │      21 843 │ 4,10 ms │
├────────────┼─────────────┼─────────┤
│ binária    │          16 │ 0,01 ms │
├────────────┼─────────────┼─────────┤
│ hashing    │           1 │ 0,00 ms │
└────────────┴─────────────┴─────────┘

  → hashing foi 410x mais rápido que a busca sequencial
```

> Saída ilustrativa da interface pretendida; os números reais serão medidos sobre a base completa.

## Integrantes

<div align="center">

| [<img src="https://res.cloudinary.com/dll5ypaj7/image/fetch/f_auto,w_300,h_300,c_fill,r_30,bo_2px_solid_rgb:2d333b/https://github.com/arthurrochamoreira.png" width="200">](https://github.com/arthurrochamoreira)<br><nobr><sub style="font-size: 160%;">Arthur Moreira</sub></nobr> | [<img src="https://res.cloudinary.com/dll5ypaj7/image/fetch/f_auto,w_300,h_300,c_fill,r_30,bo_2px_solid_rgb:2d333b/https://github.com/dev-LucasDpaula.png" width="200">](https://github.com/dev-LucasDpaula)<br><nobr><sub style="font-size: 160%;">Lucas D. Paula</sub></nobr> |
| :---: | :---: |
| 21/1030658 | 24/1011386 |

</div>

## Descrição do projeto

Aplicação de consulta ao cadastro de medicamentos registrados na Anvisa, construída para
comparar, sobre uma base real, o desempenho de diferentes algoritmos de busca.

### A base de dados

Arquivo `DADOS_ABERTOS_MEDICAMENTOS.csv`, publicado pela [Anvisa](https://dados.anvisa.gov.br/dados/):

<div align="center">

| | |
| ---: | :--- |
| **Registros** | 43.444 |
| **Snapshot** | baixado em 30/08/2026 |
| **Formato** | CSV, separador `;`, codificação ISO-8859-1 |
| **Campos** | nome, categoria regulatória, nº de registro, nº do processo, classe terapêutica, empresa detentora, situação, princípio ativo |

</div>

> A Anvisa substitui o arquivo sem versionamento nem changelog. Todos os números
> deste repositório referem-se ao snapshot acima; um download posterior pode divergir.

### Os algoritmos

A mesma consulta é resolvida por estratégias distintas, e a aplicação reporta o **tempo de
execução** e o **número de comparações** de cada uma:

| Algoritmo | Complexidade | Chave usada | Por quê |
| :--- | :---: | :--- | :--- |
| Busca sequencial | `O(n)` | qualquer campo | linha de base, sem pré-processamento |
| Busca binária | `O(log n)` | `NUMERO_REGISTRO_PRODUTO` | chave numérica, exige base ordenada |
| Hashing | `O(1)` médio | `NOME_PRODUTO` / `PRINCIPIO_ATIVO` | acesso quase direto; mede colisões em campos repetidos |

## Guia de instalação

### 1. Clone este repositório

```bash
git clone https://github.com/eda2-2026/G14_Busca_EDA2-2026.2.git
cd G14_Busca_EDA2-2026.2
```

### 2. Pré-requisitos

#### Linux (Ubuntu/Debian)

- Certifique-se de ter o `make`, `python3`, `pip` e `venv` instalados:

```bash
sudo apt update
sudo apt install -y make python3 python3-pip python3-venv
```

#### Windows

- Instale o [Git for Windows](https://git-scm.com/download/win)
- Instale o [Chocolatey](https://chocolatey.org/install) (executando o terminal **como administrador**)
- Em seguida, instale o Python e o Make com:

```cmd
choco install python make
```

### 3. Construir o ambiente com Make

Após instalar os pré-requisitos, execute:

```bash
make setup
```

O script irá:

- Verificar o interpretador Python
- Criar o ambiente virtual em `.venv`
- Instalar as dependências do [`requirements.txt`](requirements.txt)

### 4. Executar a aplicação

```bash
make run
```

Outros alvos disponíveis:

| Comando | O que faz |
| :--- | :--- |
| `make help` | lista todos os comandos |
| `make test` | roda os testes (pytest) |
| `make lint` | verifica o estilo do código (ruff) |
| `make clean` | remove o ambiente virtual e os arquivos temporários |

> A base de dados fica em `data/`.

## Capturas de tela

_A definir._

## Conclusões

_A definir._

## Referências

- **Anvisa.** Dados abertos - Medicamentos. <https://dados.anvisa.gov.br/dados/>
- **ROSA, J. L. G.** *SCC-201 - Métodos de Busca.* ICMC/USP, 2009.
- **CORMEN, T. H.** et al. *Introduction to Algorithms.* 3rd ed. MIT Press, 2009.

---

<p align="center">
  <sub>Trabalho 1 da disciplina Estruturas de Dados 2 (2026.2)</sub><br>
  <sub>Universidade de Brasília - FCTE - Prof. Maurício Serrano</sub>
</p>
