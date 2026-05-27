from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/game/<game_name>")
def game_page(game_name):
    return render_template("game.html", game=game_name)

@app.route("/download/<game_name>/<platform>")
def download(game_name, platform):
    if platform == "windows":
        folder = "windows"
        filename = f"{game_name}.exe"
    elif platform == "linux":
        folder = "linux"
        filename = f"{game_name}.zip"
    else:
        return "Invalid platform"
    return send_from_directory(
        f"static/downloads/{folder}",
        filename,
        as_attachment=True
    )

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/games")
def games():
    games_list = ["textsnake"]
    return render_template("games.html", games=games_list)

@app.route("/code")
def code():
    files = [
        ("textsnake", "Text snake")
    ]
    return render_template("code.html", files=files)
    
@app.route("/code/<game_name>")
def view_code(game_name):

    file_path = f"project_code/{game_name}.txt"

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
    else:
        code = "File not found."

    return render_template("view_code.html", game=game_name, code=code)

if __name__ == "__main__":
    app.run(debug=True)