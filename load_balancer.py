from flask import Flask, request, Response
import requests

app = Flask(__name__)

INSTANCE = ['http://localhost:5001', 'http://localhost:5002']
indice_atual = 0

def next_instance():
    global indice_atual
    instancia = INSTANCE[indice_atual]
    indice_atual = (indice_atual + 1) % len(INSTANCE)
    return instancia

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def balancer(path):
    destino = next_instance()
    url = f"{destino}/{path}"

    print(f"[LOAD BALANCER] Redirecionando para: {url}")

    resposta = requests.request(
        method=request.method,
        url=url,
        data=request.get_data(),
        headers={key: val for key, val in request.headers if key != 'Host'}
    )

    return Response(resposta.content, status=resposta.status_code,
                    content_type=resposta.headers.get('Content-Type'))

app.run(port=5000, host='localhost', debug=True)
