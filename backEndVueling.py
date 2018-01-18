from flask import Flask, request, jsonify

app = Flask (__name__)

@app.route("/")
def hello():
    return "Hola desde Vueling DialogFlow API Webhook Integration."

@app.route("/version")
def version():
    return "Vueling DialogFlow API Webhook Integration. Version 1.0"

@app.route("/webhook", methods=['POST'])
def webhook():
    content = request.json

    print(content)

    return jsonify(
        {"speech":"Gracias por usar nuestro sistema de mensajeria.",
         "displayText":"Mensaje mandado correctamente.",
         "source":"Vueling Mensajeria"}
    )

if __name__ == "__main__":
    app.run()