Guia de Instalação e Execução
Este projeto é um jogo Connect 4 implementado em Python, onde um jogador enfrenta uma IA utilizando o algoritmo Minimax com poda alfa-beta. A IA é capaz de jogar de forma competitiva contra o jogador humano. O jogo usa a biblioteca Pygame para a interface gráfica.

Aqui está um guia para rodar o jogo no seu computador, além de uma breve explicação sobre o código.

1. Pré-Requisitos
Python 3.11 ou superior: Certifique-se de ter o Python instalado. Caso não tenha, você pode baixá-lo de python.org.

Bibliotecas necessárias: O projeto utiliza as bibliotecas numpy e pygame.

2. Instalação
Passo 1: Clonar o Repositório
Caso ainda não tenha o código, você pode cloná-lo utilizando Git. Se você não tiver o Git instalado, pode baixá-lo aqui.

bash
Copiar código
git clone https://github.com/seu_usuario/connect4-main.git
cd connect4-main
Passo 2: Criar e Ativar um Ambiente Virtual (opcional, mas recomendado)
Se preferir, crie um ambiente virtual para instalar as dependências isoladas:

bash
Copiar código
python -m venv env
# No Windows
.\env\Scripts\activate
# No Linux/Mac
source env/bin/activate
Passo 3: Instalar as Dependências
Agora, instale as bibliotecas necessárias para o projeto:

bash
Copiar código
pip install numpy pygame
3. Execução do Jogo
Depois de instalar as dependências, você pode rodar o jogo com o seguinte comando:

bash
Copiar código
python main.py
Isso iniciará a interface gráfica do Connect 4.

4. Como Jogar
Jogador: Clique nas colunas para adicionar uma peça vermelha.
IA: A IA jogará automaticamente após o jogador realizar sua jogada. O tempo que a IA leva para decidir o movimento depende da profundidade do algoritmo Minimax escolhida.
5. Estrutura do Código
O código está dividido em várias funções responsáveis por diferentes partes do jogo, desde a criação do tabuleiro até a verificação de vitórias e a execução do algoritmo Minimax.

Principais Funções
criar_tabuleiro(): Cria o tabuleiro vazio com dimensões 7x8.
colocar_peca(): Coloca uma peça no tabuleiro nas coordenadas fornecidas.
movimento_vencedor(): Verifica se houve uma vitória após um movimento.
minimax(): O algoritmo Minimax, que permite que a IA jogue de maneira inteligente, usando poda alfa-beta para otimizar a busca por movimentos.
desenhar_tabuleiro(): Desenha o tabuleiro e as peças na tela usando a biblioteca Pygame.
principal(): Função principal que gerencia o loop do jogo.
Heurísticas do Algoritmo Minimax
O algoritmo Minimax avalia os movimentos possíveis com base nas heurísticas, tentando maximizar a vantagem da IA e minimizar a possibilidade de vitória do jogador. Algumas das heurísticas implementadas são:

Vantagem para a IA:
Se a IA tiver 4 peças consecutivas (vitória), ela ganha.
Se a IA estiver a uma jogada de ganhar, ela recebe uma pontuação alta.
Se a IA estiver próxima de ganhar, ela recebe uma pontuação menor, mas ainda significativa.
Desvantagens para o Jogador:
Se o jogador estiver a uma jogada de ganhar, a IA tenta bloquear esse movimento.
Posições Centrais: O centro do tabuleiro tem maior peso nas decisões, pois ocupar as colunas centrais oferece mais opções de movimentos.
6. Outros Detalhes
Jogador vs IA: O jogador sempre joga primeiro, mas a IA pode ser configurada para iniciar caso deseje.
Profundidade do Algoritmo: O jogador pode escolher a profundidade da busca Minimax, que afeta a "dificuldade" da IA. Quanto maior a profundidade, mais tempo a IA pode levar para calcular sua jogada, mas suas decisões se tornam mais precisas.
7. Possíveis Erros Comuns
Erro de Módulo Não Encontrado: Se você encontrar um erro como ModuleNotFoundError, significa que a biblioteca necessária não foi instalada. Para isso, use:

bash
Copiar código
pip install numpy pygame
Erro de Tela em Branco no Pygame: Se a interface gráfica não carregar corretamente, verifique se o Pygame está bem instalado e atualizado.

Conclusão
Esse é um projeto simples e divertido para aprender como implementar um jogo básico com IA, utilizando conceitos como Minimax e Poda Alfa-Beta. Com essas instruções, você deve conseguir configurar o ambiente e rodar o jogo sem problemas. Se precisar de mais ajuda, estou à disposição!
