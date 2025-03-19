from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if code:
        url = "https://api.schwabapi.com/v1/oauth/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": "https://kyle-schwap.onrender.com/callback",
            "client_id": "0E6mCEgtjcQJlFzOQnj99qRA9cZHejjL",
            "client_secret": "gaOXZZ2OqIUtesPd"
        }
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            data = response.json()
            token = data["access_token"]
            refresh_token = data["refresh_token"]
            with open("token.txt", "w") as f:
                f.write(token + "\n" + refresh_token)
            return f"Token: {token}<br>Refresh Token: {refresh_token}"
        return f"Token exchange failed: {response.text}"
    return "No code received."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
