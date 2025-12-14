# azure-content-safety

Azure content safety

## setup project

### Prerequisites

1. Install uv [guide](https://docs.astral.sh/uv/getting-started/installation/)
2. Instll go-task [guide](https://taskfile.dev/installation/)

### Setup

```sh
cd <this project folder>
uv sync
pre-commit install
cp .env.sample .env
```

you do not need to do `uv init` because we have already done it for you.

### Activate virtual environment

MacOS/Linux

```sh
source .venv/bin/activate
```

Windows

```sh
.venv\Scripts\activate
```

### install pre-commit hooks

```sh
pre-commit install
```

### vscode extensions

1. code . (open the project in vscode)
2. install the recommended extensions (cmd + shift + p ->
   `Extensions: Show Recommended Extensions`)
