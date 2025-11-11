
from flask import Flask
import platform
import psutil
import os
import json

app = Flask(__name__)

@app.route('/info')
def info():
    dados = {
        "nome": "Lorenzo, João Abreu, Kevyn Gabriel"
    }
    return json.dumps(dados, ensure_ascii=False)

@app.route('/metricas')
def metricas():
    metricas_dados = {
        "pid": os.getpid(),
        "sistema_operacional": platform.platform(),
        "uso_cpu": psutil.cpu_percent(),
        "uso_memoria_mb": psutil.virtual_memory().used // (1024 * 1024)
    }
    return json.dumps(metricas_dados, ensure_ascii=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)