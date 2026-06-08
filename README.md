# SGTA — Sistema de Gerenciamento de Tarefas Acadêmicas

Projeto desenvolvido na disciplina **Laboratório de Programação Backend** na Universidade de Vassouras.

O SGTA é uma API REST que permite o gerenciamento de tarefas acadêmicas: alunos podem criar e acompanhar suas tarefas, e professores podem atribuir atividades com prioridade e prazo de entrega. O sistema também possui gerenciamento de usuários responsáveis pelas tarefas.

---

## Tecnologias Utilizadas

| Tecnologia | Versão |
|---|---|
| Python | 3.12 |
| Django | 6.0.3 |
| Django REST Framework | 3.16.1 |
| psycopg (psycopg3) | 3.3.3 |
| python-decouple | 3.8 |
| PostgreSQL | 16 |
| Docker / Docker Compose | v2 |

---

## Estrutura do Projeto

```
sgta/
│
├── backend/
│   ├── config/           # Configurações do Django (settings, urls, wsgi, asgi)
│   ├── tarefas/          # App de tarefas (models, views, urls, migrations)
│   ├── usuarios/         # App de usuários (models, views, urls, migrations)
│   ├── Dockerfile
│   ├── entrypoint.sh
│   └── requirements.txt
│
├── docker-compose.yml
├── .env.example
├── README.md
└── .gitignore
```

---

## Pré-requisitos

- [Docker](https://www.docker.com/) instalado
- [Docker Compose](https://docs.docker.com/compose/) v2+

---

## Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/matheusbaltar/sgta.git
cd sgta
```

### 2. Configurar as variáveis de ambiente

Copie o arquivo de exemplo e preencha as variáveis:

```bash
cp .env.example .env
```

Conteúdo do `.env`:

```env
SECRET_KEY=sua_secret_key_aqui
DEBUG=True

DB_NAME=sgta
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=db
DB_PORT=5432
```

### 3. Subir os containers

```bash
docker compose up --build
```

> O serviço `web` só sobe depois que o PostgreSQL passa no `healthcheck` (via `pg_isready`). As migrations são aplicadas automaticamente pelo `entrypoint.sh`.

### 4. Acessar a API

A API estará disponível em: `http://localhost:8000/`

---

## Imagem Docker

A imagem do serviço `web` está publicada no Docker Hub:

```bash
docker pull matheusbaltar/sgta-web
```

---

## Modelos de Dados

### Usuario

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | int | Identificador único |
| `nome` | CharField(255) | Nome do usuário |
| `email` | EmailField(255) | E-mail do usuário |
| `ativo` | CharField | Status: `ATIVO` ou `INATIVO` |
| `data_criacao` | DateField | Data de criação (auto) |

### Tarefa

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | int | Identificador único |
| `titulo` | CharField(255) | Título da tarefa |
| `descricao` | TextField | Descrição detalhada |
| `status` | CharField | `ABERTA`, `EM_ANDAMENTO`, `CONCLUIDA` ou `CANCELADA` |
| `prioridade` | CharField | `URGENTE` ou `NAO_URGENTE` |
| `usuario_responsavel` | FK → Usuario | Usuário responsável pela tarefa |
| `data_criacao` | DateTimeField | Data/hora de criação (auto) |
| `data_entrega` | DateField | Prazo de entrega |

---

## API Endpoints

### Tarefas — `/api/tarefas/`

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/api/tarefas/` | Lista todas as tarefas |
| GET | `/api/tarefas/id/<int:id>/` | Retorna uma tarefa pelo ID |
| GET | `/api/tarefas/prioridade/<str:prioridade>/` | Filtra tarefas por prioridade |
| GET | `/api/tarefas/busca/<str:titulo>/` | Busca tarefas por título (parcial) |
| GET | `/api/tarefas/importante` | Tarefas abertas e urgentes |
| GET | `/api/tarefas/atrasadas` | Tarefas com entrega hoje e não concluídas |

#### Exemplos

```
GET /api/tarefas/id/1/
GET /api/tarefas/prioridade/urgente/
GET /api/tarefas/prioridade/nao_urgente/
GET /api/tarefas/busca/back/        → encontra "tarefa de back"
GET /api/tarefas/busca/teste/       → encontra tarefas com "teste" no título
GET /api/tarefas/importante
GET /api/tarefas/atrasadas
```

---

### Usuários — `/api/usuarios/`

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/api/usuarios/` | Lista todos os usuários |
| GET | `/api/usuarios/id/<int:id>/` | Retorna um usuário pelo ID |

#### Exemplos

```
GET /api/usuarios/
GET /api/usuarios/id/1/
```

---

## Variáveis de Ambiente

| Variável | Descrição |
|---|---|
| `SECRET_KEY` | Chave secreta do Django |
| `DEBUG` | Modo debug (`True` em desenvolvimento) |
| `DB_NAME` | Nome do banco de dados PostgreSQL |
| `DB_USER` | Usuário do banco |
| `DB_PASSWORD` | Senha do banco |
| `DB_HOST` | Host do banco (usar `db` no Docker) |
| `DB_PORT` | Porta do banco (padrão: `5432`) |

---

## Contribuidores

- **Matheus Baltar** — [@matheusbaltar](https://github.com/matheusbaltar)
  **Ayla Almeida** — [@aylaalmeida](https://github.com/aylaalmeida)

---

## Licença

Projeto acadêmico — Universidade de Vassouras, disciplina Laboratório de Programação Backend.