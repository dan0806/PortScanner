# PortScanner

Um scanner de portas TCP desenvolvido em Python para fins educacionais e estudo de redes de computadores e segurança da informação.

O programa realiza conexões TCP em um intervalo de portas definido pelo usuário, identificando quais portas estão abertas em um host específico. O escaneamento é realizado de forma concorrente utilizando threads para aumentar o desempenho.

---

## Funcionalidades

- Escaneamento de portas TCP
- Definição de intervalo de portas via linha de comando
- Validação básica de host
- Execução concorrente com ThreadPoolExecutor
- Exibição de progresso durante o escaneamento
- Identificação de portas abertas

---

## Tecnologias Utilizadas

- Python 3
- Socket
- Concurrent Futures
- TCP/IP

---

## Estrutura do Projeto

```text
PortScanner/
│
├── scanner.py
└── README.md
```

---

## Como Executar

### Clone o repositório

```bash
git clone https://github.com/dan0806/PortScanner.git
```

### Acesse o diretório

```bash
cd PortScanner
```

### Execute o programa

```bash
python scanner.py <host> <porta_inicial> <porta_final>
```

### Exemplo

```bash
python scanner.py 192.168.0.83 1 500
```

ou

```bash
python scanner.py scanme.nmap.org 1 1000
```

---

## Exemplo de Saída

```text
Scanning target 192.168.0.83

[OPEN] Port 135
[OPEN] Port 139
[OPEN] Port 445

Progress: 501/501

Scan completed
```

---

## Conceitos Aplicados

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de redes e programação em Python:

- Sockets TCP
- Modelo Cliente-Servidor
- Conexões TCP/IP
- Multithreading
- Concorrência com ThreadPoolExecutor
- Argumentos de linha de comando
- Tratamento de exceções
- Validação de entrada

---

## Limitações

Atualmente o projeto:

- Realiza apenas escaneamento TCP
- Não identifica serviços executando nas portas abertas
- Não realiza banner grabbing
- Não exporta resultados para arquivos

---

## Melhorias Futuras

- Implementação de banner grabbing
- Detecção automática de serviços
- Exportação dos resultados para CSV ou JSON
- Utilização de argparse para gerenciamento de argumentos
- Interface de terminal mais amigável
- Suporte a escaneamento UDP
- Configuração personalizada do número de threads

---

## Objetivo Educacional

Este projeto foi desenvolvido para aprofundar conhecimentos em:

- Redes de computadores
- Segurança da informação
- Programação concorrente
- Desenvolvimento de ferramentas de linha de comando

---

## Autor

Danilo Gomez

- GitHub: https://github.com/dan0806
- LinkedIn: https://www.linkedin.com/in/danilo-gomez-20678b3b1