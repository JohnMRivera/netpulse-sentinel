import requests

def send_alert(message):
    token = "7352747175:AAELE8TuJcb8EZcUtyIac1ssEGz9abxG5dY"
    chat_id = "2027638266"


    url = f"https://api.telegram.org/bot{token}/sendMessage"

    data = {
        'chat_id': chat_id,
        'text': message
    }

    print(f"URL: {url}\nMensaje: {message}")
    response = requests.post(url, data=data, timeout=0.5)

    print(f"Respuesta: {response}")

send_alert("¡Bot funcionando!")