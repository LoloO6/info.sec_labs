from flask import Flask, request, render_template, redirect, url_for
from pathlib import Path
import json, datetime, html

app = Flask(__name__)
DATA_FILE = Path("flask.txt")

def mask_card(number: str) -> str:
    digits = "".join(ch for ch in number if ch.isdigit())
    if len(digits) <= 4:
        return "*" * len(digits)
    return "*" * (len(digits) - 4) + digits[-4:]

def save_entry(data: dict):
    DATA_FILE.touch(exist_ok=True)
    ts = datetime.datetime.utcnow().isoformat()
    safe = {k: html.escape(str(v)) for k,v in data.items()}
    entry = {"ts": ts, "data": safe}
    with DATA_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

@app.route("/", methods=["GET"])
def index():
    return render_template("fake_login.html")

@app.route("/submit", methods=["POST"])
def submit():
    card_name = request.form.get("card_name", "")
    card_number = request.form.get("card_number", "")
    exp_month = request.form.get("exp_month", "")
    exp_year = request.form.get("exp_year", "")
    cvc = request.form.get("cvc", "")

    entry = {
        "card_name": card_name,
        "card_number_masked": mask_card(card_number),
        "exp_month": exp_month,
        "exp_year": exp_year,
        "cvc_masked": "***"
    }
    save_entry(entry)
    return redirect(url_for("thank_you"))

@app.route("/thank_you")
def thank_you():
    return "<h3>Платёж принят.</h3>"

if __name__ == "__main__":
    DATA_FILE.touch(exist_ok=True)
    app.run(host="127.0.0.1", port=8000, debug=True)
