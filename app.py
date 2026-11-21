import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# Секретный ключ берётся из переменной окружения на Render,
# а если её нет (локально) — используется запасной вариант.
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "локальный-запасной-ключ-замените-на-свой")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("Пожалуйста, заполните все поля.", "danger")
        else:
            print(f"Новое сообщение: {name} <{email}> — {message}")
            flash(f"Спасибо, {name}! Ваше сообщение получено.", "success")
            return redirect(url_for("contact"))

    return render_template("contact.html")


# Этот блок выполняется только при локальном запуске (python app.py).
# На Render сайт запускается через gunicorn, и этот код не используется.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)