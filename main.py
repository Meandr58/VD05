from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    context = {
        "caption": "Домашняя страница",
        "link": "О проекте"
    }
    return render_template("home.html", **context)

@app.route("/about/")
def about():
    context = {
        "caption": "О проекте",
        "link": "На домашнюю страницу"
    }
    return render_template("about.html", **context)

@app.route("/base/")
def base():
    return render_template("base.html", caption="Шаблон")

@app.route("/content/")
def content():
    return render_template("content.html", caption="Резерв")

if __name__ == "__main__":
    app.run()

