
# EBD PLANNER

API desenvolvida em FastApi para um aplicação de frequências, relatórios e organização de aulas da escola biblíca dominical.


## Instalação

Inicie clonando o repositório

```bash
  git clone https://github.com/Erick-Viniciusx/EBD-PLANNER-API.git
```

Instale o **pipx** e o **poetry**

```bash
  pip install pipx
  pipx install poetry
```
Na raiz do projeto onde está localizado o arquivo **project.toml** rode:

```bash
  poetry install
```
Ative o ambiente virtual com:

```bash
  poetry env activate
```
ou:

```bash
  poetry self add poetry-plugin-shell
  poetry shell
```
No caminho 'ebd_planner/src/' configure o **prisma**:
```bash
  prisma generate
  prisma migrate dev --name "initial"
```
No caminho "ebd_planner/src/ebd_planner" inicie o **FastApi**:
```bash
  fastapi dev app.py
```

