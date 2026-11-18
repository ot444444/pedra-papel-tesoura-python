# Pedra, Papel e Tesoura em Python

Projeto acadêmico desenvolvido durante a disciplina de Raciocínio Algorítmico no curso de Ciência da Computação da PUCPR.

O programa implementa um jogo de Pedra, Papel e Tesoura com três modos:

- Humano vs Humano
- Humano vs Computador
- Computador vs Computador

## Conceitos praticados

- Variáveis
- Entrada de dados
- Estruturas condicionais
- Loops com `while`
- Validação de opções numéricas
- Geração de números aleatórios com `random`
- Controle de placar

## Como executar

Certifique-se de ter Python 3 instalado. Baixe o repositório e, no terminal, acesse a pasta que contém o arquivo `main.py`. Execute:

```bash
python main.py
```

Escolha o modo de jogo e siga as opções numéricas apresentadas no terminal.

## Limitação conhecida

O programa verifica se as opções numéricas estão dentro do intervalo permitido. Porém, entradas com letras, campos vazios ou outros valores que não possam ser convertidos para um número inteiro encerram a execução com um erro. Tratar essas entradas é uma melhoria futura.

## O que mudou nesta versão

Na primeira versão, o trecho que pedia e validava uma jogada aparecia
em três pontos do código. Agora, os modos com jogadores humanos
reutilizam a função `pedir_escolha(jogador)`.

- `mostrar_escolha(jogador, escolha)` exibe a jogada de um humano ou do computador.
- `jogo(escolha1, escolha2)` resolve a rodada e atualiza o placar.

[Veja o antes e depois no commit da refatoração](https://github.com/ot444444/pedra-papel-tesoura-python/commit/d366eb2f4b73bd839668c723dbe9ae82785ee500).

## Autores

Projeto desenvolvido por Otavio Kavinski e Gabriel G. como atividade acadêmica da disciplina de Raciocínio Algorítmico da PUCPR.
