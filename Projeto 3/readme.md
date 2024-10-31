# Projeto de Topologia em Mininet: Tree com Profundidade e Ramificação

## 📖 Descrição
Este projeto cria uma topologia em árvore no Mininet com profundidade 4 e ramificação 2. A topologia utiliza largura de banda de 25 Mbps entre os nós e um servidor TCP configurado no host 1 para testes de desempenho. O objetivo é explorar a criação de topologias, inspecionar informações de interfaces, endereços IP e MAC, e testar a conectividade e largura de banda.

---

## ⚙️ Pré-requisitos

- **Mininet**: Certifique-se de que o Mininet está instalado. 
---

## 🚀 Instruções para Execução

### 1. Iniciar a Topologia no Mininet

No terminal, execute o seguinte comando para criar uma topologia em árvore com profundidade 4 e ramificação 2, usando largura de banda de 25 Mbps entre os nós:

```bash
sudo mn --topo tree,depth=4,fanout=2 --link tc,bw=25
```

Neste comando:
- `--topo tree,depth=4,fanout=2`: Define a topologia como uma árvore com profundidade 4 e ramificação 2.
- `--link tc,bw=25`: Define a largura de banda das conexões como 25 Mbps.

Após o comando, o Mininet será iniciado e você entrará no CLI interativo.

---

### 2. Inspecionar Interfaces, Endereços MAC e IP
O comando dump exibe informações detalhadas sobre todos os nós (hosts e switches) da topologia, incluindo endereços IP, MAC, portas e links. Ele é útil para inspecionar rapidamente as configurações de cada componente na rede.
Para verificar as informações de interfaces, endereços IP e MAC de cada nó na topologia, utilize os seguintes comandos no CLI do Mininet:

- **Listar Hosts, Switches**:
  ```dump
  ```
  Isso exibirá informações de todos os dispositivos da topologia, incluindo:
  Hosts: Mostra o nome, endereço IP, endereço MAC e interfaces dos hosts.
  Switches: Exibe as portas conectadas, permitindo visualizar a topologia de rede.

- **Informações de Interfaces de um Host (por exemplo, `h1`)**:
  ```bash
  h1 ifconfig
  ```
  Isso mostra o endereço IP e MAC do host `h1`. Repita para outros hosts (`h2`, `h3`, etc.) conforme necessário.

- **Informações de Interfaces de um Switch (por exemplo, `s1`)**:
  ```bash
  s1 ifconfig
  ```
  Exibe informações sobre as interfaces de `s1`. Substitua `s1` por outros switches (`s2`, `s3`, etc.) para verificar as portas e conexões.

---

### 3. Testes de Conectividade (Ping entre Hosts e de todos os nós)

Para verificar a conectividade entre diferentes hosts, utilize o comando `ping` no CLI do Mininet. Por exemplo, para testar entre `h1` e `h2`:

```bash
h1 ping -c 4 h2
```

Este comando envia 4 pacotes `ping` de `h1` para `h2`, confirmando a conectividade entre os nós. Repita entre outros hosts, conforme necessário, para verificar o estado da rede.

---

```bash
pingall
```

Este comando mostra os pings de todos os nós.

---
### 4. Configurando Teste TCP com `iperf`

Nesta etapa, configuramos um teste TCP usando o `iperf` para medir a largura de banda entre `h1` (servidor) e `h2` (cliente) com uma largura de banda de 25 Mbps.

#### No `h1` (Servidor):
No CLI do Mininet, execute o seguinte comando para iniciar o servidor TCP no host `h1` na porta `5555`:

```bash
h1 iperf -s -p 5555
```

Este comando inicia o servidor `iperf` no `h1` na porta `5555`, esperando conexões de clientes.

#### No `h2` (Cliente):
Em seguida, execute o `iperf` em `h2` para conectá-lo ao servidor `h1`, registrando a largura de banda a cada segundo durante um período de 10 segundos:

```bash
h2 iperf -c h1 -p 5555 -t 10 -i 1
```

Neste comando:
- `-c h1`: Define `h2` como cliente que se conecta ao servidor `h1`.
- `-p 5555`: Define a porta `5555` para conexão.
- `-t 10`: Executa o teste por 10 segundos.
- `-i 1`: Gera um relatório a cada segundo.

> Após a execução, o cliente exibirá relatórios de largura de banda, mostrando a taxa de transferência a cada segundo.

---

## 🔄 Finalizando o Mininet

Para sair do Mininet, basta digitar o comando:

```bash
exit
```

