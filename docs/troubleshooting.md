# Troubleshooting

## Porta ocupada

Se `python run.py mock-api` falhar por porta ocupada, encerre o processo antigo ou use outra porta:

```bash
python run.py mock-api --port 8010
```

## Import quebrado

Execute a partir de `Semana3/src`:

```bash
python run.py doctor
```

## Teste de API falhando

Confirme que a mock API está rodando:

```bash
python run.py mock-api
```

Em outro terminal:

```bash
python run.py test ex01
```

