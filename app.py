from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/plan", methods=["POST"])
def create_plan():
    data = request.json
    ders = data.get("ders", "TYT")
    saat = data.get("saat", 3)

    plan = f"{ders} için {saat} saatlik plan:\n- Konu\n- Test\n- Tekrar"

    return jsonify(plan)

if __name__ == "__main__":
    app.run(port=5001)
