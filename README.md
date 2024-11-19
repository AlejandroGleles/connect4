# Connect 4 - Jogo com Inteligência Artificial (Minimax)
Este é um projeto de Connect 4 (ou Quatro em Linha) implementado em Python. O jogo permite que um jogador humano enfrente uma IA que utiliza o algoritmo Minimax com poda alfa-beta para calcular as melhores jogadas possíveis.

## Tabela de Conteúdos
1. [Instalação](#instalação)
2. [Como Jogar](#como-jogar)
3. [Estrutura do Código](#estrutura-do-código)
4. [Heurísticas da IA](#heurísticas-da-ia)
5. [Como Rodar o Jogo](#como-rodar-o-jogo)
6. [Contribuindo](#contribuindo)
7. [Licença](#licença)

## Instalação
### Clonando o Repositório
Clone o repositório para o seu computador utilizando Git:

```bash
git clone https://github.com/AlejandroGleles/connect4.git
cd connect4
Instalando Dependências
Este projeto requer o Python 3 e as bibliotecas numpy e pygame. Se você não tem o Python instalado, faça o download aqui.

Crie e ative um ambiente virtual (opcional, mas recomendado):

bash
# Criando o ambiente virtual
python -m venv venv

# No Windows:
.\venv\Scripts\activate

# No Linux/Mac:
source venv/bin/activate
Em seguida, instale as dependências:

bash
pip install -r requirements.txt
Ou instale manualmente numpy e pygame:

bash
pip install numpy pygame
Como Jogar
Iniciar o Jogo
Execute o arquivo main.py:

bash
python main.py
Objetivo
O objetivo do jogo é ser o primeiro a alinhar 4 peças consecutivas, seja horizontal, vertical ou diagonalmente.

Jogador
O jogador humano pode fazer movimentos clicando nas colunas, colocando uma peça vermelha.

IA
A IA (inteligência artificial) jogará automaticamente após o jogador fazer seu movimento. O algoritmo Minimax decide a melhor jogada com base em uma série de heurísticas.

Estrutura do Código
O código é dividido em várias funções que gerenciam diferentes aspectos do jogo. A seguir estão as principais funções:

Funções Principais
criar_tabuleiro(): Cria e retorna um tabuleiro vazio (matriz 7x8) usando numpy.

colocar_peca(): Coloca uma peça (do jogador ou da IA) no tabuleiro.

movimento_vencedor(): Verifica se o movimento atual resulta em uma vitória para o jogador ou IA.

minimax(): Implementa o algoritmo Minimax com poda alfa-beta para otimizar a decisão da IA. Esse algoritmo avalia possíveis jogadas e escolhe a melhor, com base nas heurísticas definidas.

desenhar_tabuleiro(): Responsável por desenhar o tabuleiro e as peças na tela usando a biblioteca Pygame.

principal(): Função principal que gerencia o fluxo do jogo, incluindo a interação com o usuário e as jogadas da IA.

Heurísticas da IA
A IA utiliza heurísticas para avaliar as melhores jogadas possíveis durante o jogo. Essas heurísticas são baseadas em características do tabuleiro e visam maximizar a chance da IA vencer e minimizar as chances do jogador vencer. Abaixo estão as principais heurísticas utilizadas:

Vantagens para a IA (maximizar a chance de vitória)

4 peças consecutivas: Se a IA conseguir alinhar 4 peças consecutivas em qualquer direção (linha, coluna ou diagonal), a jogada é considerada uma vitória. Isso recebe uma pontuação alta.

3 peças consecutivas + 1 espaço vazio: Se a IA já tiver 3 peças consecutivas e um espaço vazio em uma janela de 4 posições, ela recebe uma pontuação alta. Isso indica que a IA pode ganhar na próxima jogada.

2 peças consecutivas + 2 espaços vazios: Se a IA tiver 2 peças consecutivas e 2 espaços vazios, ela recebe uma pontuação moderada. A IA está próxima de completar a sequência.

Desvantagens para o Jogador (minimizar a chance de vitória)

3 peças do jogador + 1 espaço vazio: Se o jogador tiver 3 peças consecutivas e um espaço vazio, a IA penaliza essa situação com uma pontuação negativa, porque o jogador pode ganhar na próxima jogada.

2 peças do jogador + 2 espaços vazios: Se o jogador tiver 2 peças consecutivas e dois espaços vazios, isso também é uma situação perigosa. A IA penaliza essa configuração para evitar que o jogador complete a sequência.

Posições Centrais (prioridade para a IA)

A centralidade das peças: A IA valoriza mais as peças colocadas nas colunas centrais, pois elas oferecem mais possibilidades de movimentos nas próximas jogadas. Assim, a IA recebe uma pontuação adicional para cada peça colocada nas colunas centrais.

Bloqueio de Jogadas Vencedoras

Prevenção de vitória do jogador: Além de procurar suas próprias vitórias, a IA também precisa bloquear as vitórias do jogador. Se o jogador estiver a uma jogada de ganhar, a IA é incentivada a bloquear essa posição.

Poda Alfa-Beta

O algoritmo Minimax utiliza a poda alfa-beta para otimizar a busca. Ele pode "podar" (ou cortar) partes da árvore de decisões que não precisam ser exploradas, pois já encontramos uma solução melhor em outro ramo. Isso acelera significativamente o processo de decisão da IA, permitindo que ela jogue de forma eficiente.

Como Rodar o Jogo
Para rodar o jogo, basta executar o arquivo principal:

bash
python main.py
O jogo pedirá para você escolher a profundidade da busca (quanto maior, mais difícil a IA) e o algoritmo que a IA deve usar (Minimax ou Alpha-Beta).

Opções de Entrada
Profundidade: Escolha a profundidade da busca (maior profundidade torna a IA mais forte, mas também mais lenta).

Algoritmo: Escolha entre minimax ou alpha_beta (para usar a poda alfa-beta).
