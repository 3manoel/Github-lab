# Lab Dapr no OpenShift

Este repositório contém um laboratório demonstrando o uso do Dapr para comunicação entre duas aplicações (uma em Python e outra em Node.js) executando em OpenShift ou localmente com o Dapr sidecar.

Estrutura:
- [labdapr/nodeapp](labdapr/nodeapp) — Aplicação Node.js que recebe pedidos (orders).
- [labdapr/pythonapp](labdapr/pythonapp) — Aplicação Python que envia pedidos para a Node app via sidecar Dapr.
- [Readme.md](Readme.md) — Este arquivo.

Resumo do fluxo
- A aplicação Python cria um pedido (order) e usa o sidecar Dapr local para realizar um HTTP invoke para a aplicação Node.
- O Dapr sidecar do Python faz a chamada para o sidecar do Node usando a API de invoke do Dapr: POST /v1.0/invoke/{app-id}/method/{method}.
- Assim, a aplicação Python não precisa conhecer o endereço direto da Node app, apenas o app-id (ex.: `nodeapp`).

Componentes
- Python app (pythonapp)
  - Gera e envia orders.
  - Realiza a chamada HTTP para o endpoint do Dapr: `http://localhost:3500/v1.0/invoke/nodeapp/method/sendOrder` (quando em execução local com Dapr).
- Node app (nodeapp)
  - Expõe um endpoint que processa o pedido recebido (por exemplo `POST /sendOrder`) e retorna status/resultado.

Execução local (com Dapr CLI)
1. Instalar Dapr CLI e inicializar: `dapr init`
2. Em um terminal, iniciar a Node app com sidecar:
   - Exemplo: `dapr run --app-id nodeapp --app-port 3000 -- node .`
3. Em outro terminal, iniciar a Python app com sidecar:
   - Exemplo: `dapr run --app-id pythonapp --app-port 5000 -- python app.py`
4. Fluxo de teste (curl via Dapr invoke pelo sidecar do python):
   - Se a própria python app faz o POST via Dapr API local, não é necessário curl externo.
   - Exemplo direto via Dapr HTTP API:  
     `curl -X POST http://localhost:3500/v1.0/invoke/nodeapp/method/sendOrder -d '{"orderId":"123","item":"x"}' -H "Content-Type: application/json"`

Notas para OpenShift
- Instalar o Dapr operator no cluster OpenShift (seguir documentação oficial do Dapr para OpenShift).
- Criar o Namespace/Project e aplicar os deployments das aplicações (`Deployment` + `Service`) com as annotations/labels que habilitam/invocam o sidecar Dapr (ou usar injeção automática, conforme configuração do cluster).
- As aplicações usarão o mesmo padrão de invoke: Dapr cuida do discovery entre app-ids, então não é necessário expor endpoints internos diretamente entre pods.
- Para expor a Node app para fora do cluster (se necessário para testes), criar um Route/Service externo.

Observações finais
- A integração via Dapr simplifica comunicação entre serviços sem que as aplicações conheçam os endereços IP/ports uma da outra.
- Para ver o código das aplicações: [labdapr/nodeapp](labdapr/nodeapp) e [labdapr/pythonapp](labdapr/pythonapp).