# Sistema Bancário Simples 

### Ferramentas 

- Python 3.11
- VS Code
- Github

### Desafio Proposto 

Criar um sistema bancário com as operações: Depósito, Saque e Visualização de Extrato. A versão do projeto trabalha apenas com um usuário e por isso não foi necessário implementar verificação de conta ou agência.

### Regras de Negócio Solicitadas

- Para a operação de depósito devem ser permitidos apenas valores positivos.
- O saque deve obedecer um limite diário de 3 operações diárias, com limite máximo de R$ 500, 00 por saque.
- Caso o usuário não tenha saldo em conta, o sistema deve cancelar a operação de saque e exibir uma mensagem de aviso.
- As operações de depósito e saque devem ser armazenadas em uma variável e apresentadas na operação extrato.
- Ao final do extrato deve ser exibido o saldo final após as operações registradas.
- Os valores devem ser exibidos no formato R$ xxxx.xx

#### Implementações Pessoais

- Mensagens de saída amigaveis e descritivas das operações.
- Emissão de comprovante com valor das operações realizadas, a cada operação, e não apenas na operação extrato.