from datetime import datetime

def minha_tarefa(*args, **kwargs):
    print(f"Executando minha_tarefa em {datetime.now()} com args={args} e kwargs={kwargs}")

def outra_tarefa(*args, **kwargs):
    print(f"Executando outra_tarefa em {datetime.now()} com args={args} e kwargs={kwargs}")
