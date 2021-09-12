from flask import Flask, render_template, request, send_file, redirect
from gtts import gTTS

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/homepage')
def hello_world():
    return render_template("homepage.html")


@app.route("/download", methods=["POST", "GET"])
def download_output():
    if request.method == "POST":
        text = request.form["phrase"]
        tts = gTTS(text=text, lang="it")
        tts.save("tts_output.mp3")
        p = "tts_output.mp3"
        return send_file(p, as_attachment=True)
    else:
        return redirect("/home")


if __name__ == '__main__':
    app.run()
