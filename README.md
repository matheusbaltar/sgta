# SGTA - Sistema de Gerenciamento de Tarefas Acadêmicas

Projeto desenvolvido na disciplina **Laboratório de Programação Backend**.

O objetivo do sistema é permitir o gerenciamento de tarefas acadêmicas, onde alunos podem criar e acompanhar suas tarefas e professores podem atribuir atividades.

---

# Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker
- Git

---

# Estrutura do Projeto
sgta/
│
├── backend/
│ ├── config/
│ ├── tarefas/
│ ├── manage.py
│ └── requirements.txt
│
├── docker/
│ └── postgres/
│
├── docker-compose.yml
├── README.md
└── .gitignore

---

# API Endpoints

## Funcionalidades Existentes

### Listar Todas as Tarefas
- **URL:** `/api/tarefas/`
- **Método:** GET
- **Descrição:** Retorna a lista completa de todas as tarefas cadastradas no sistema.

### Buscar Tarefa por ID
- **URL:** `/api/tarefas/id/<int:id>/`
- **Método:** GET
- **Descrição:** Retorna os detalhes de uma tarefa específica pelo seu ID.
- **Exemplo:** `/api/tarefas/id/1/`

---

## Novas Funcionalidades

### Filtrar Tarefas por Prioridade
- **URL:** `/api/tarefas/prioridade/<str:prioridade>/`
- **Método:** GET
- **Descrição:** Retorna tarefas filtradas pela prioridade informada (URGENTE ou NAO_URGENTE).
- **Valores aceitos:** `urgente` ou `nao_urgente` (case insensitive)
- **Exemplos:**
  - `/api/tarefas/prioridade/urgente/`
  - `/api/tarefas/prioridade/nao_urgente/`

### Buscar Tarefas por Título (Busca Parcial)
- **URL:** `/api/tarefas/busca/<str:titulo>/`
- **Método:** GET
- **Descrição:** Busca tarefas que contenham a palavra informada no título (busca parcial, case insensitive).
- **Exemplos:**
  - `/api/tarefas/busca/back/` - Encontra "tarefa de back"
  - `/api/tarefas/busca/teste/` - Encontra tarefas com "teste" no título

### Listar Tarefas Importantes
- **URL:** `/api/tarefas/importante`
- **Método:** GET
- **Descrição:** Retorna tarefas com status ABERTA e prioridade URGENTE.

### Listar Tarefas Atrasadas
- **URL:** `/api/tarefas/atrasadas`
- **Método:** GET
- **Descrição:** Retorna tarefas cuja data de entrega é hoje e que não estão concluídas.
