from flask import Flask, render_template, request, jsonify, session
import json
import random

app = Flask(__name__)
app.secret_key = "salainen_avain"

# Lataa data.json
with open("data.json", "r", encoding="utf-8") as f:
    game_data = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start_game", methods=["POST"])
def start_game():
    try:
        num_players = int(request.form["num_players"])
        if num_players < 3 or num_players > 7:
            return jsonify({"error": "Pelaajien määrän tulee olla 3-7"}), 400
        
        chosen_location = random.choice(game_data["paikat"])
        roles = chosen_location["roles"].copy()
        random.shuffle(roles)
        
        players = []
        # Assign regular roles to all but one player
        for i in range(num_players - 1):
            players.append({
                "role": roles[i % len(roles)],  # Use modulo to avoid index errors
                "place": chosen_location["place"]
            })
        
        # Add the impostor
        players.append({"role": "???", "place": "???"})
        random.shuffle(players)
        
        session["players"] = players
        session["num_players"] = num_players
        return jsonify({"message": "Peli aloitettu!"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/get_card", methods=["GET"])
def get_card():
    try:
        player_index = int(request.args.get("player_index", 0))
        if "players" not in session:
            return jsonify({"error": "Peliä ei ole aloitettu"}), 400
        
        if player_index >= len(session["players"]):
            return jsonify({"error": "Virheellinen pelaajan indeksi"}), 400
        
        return jsonify(session["players"][player_index])
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")