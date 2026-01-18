from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save_note", methods=["POST"])
def save_note():
    note = request.json["note"]

    with open("notes.txt", "a", encoding="utf-8") as f:
        f.write(note + "\n")

    return jsonify({"message": "Note saved successfully"})

@app.route("/get_notes")
def get_notes():
    try:
        with open("notes.txt", "r", encoding="utf-8") as f:
            notes = f.readlines()
    except FileNotFoundError:
        notes = []

    return jsonify(notes)

@app.route("/delete_note/<int:index>", methods=["DELETE"])
def delete_note(index):
    with open("notes.txt", "r", encoding="utf-8") as f:
        notes = f.readlines()

    if 0 <= index < len(notes):
        notes.pop(index)

    with open("notes.txt", "w", encoding="utf-8") as f:
        f.writelines(notes)

    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
