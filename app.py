from flask import Flask, request, render_template
import google.generativeai as genai
import markdown

# Ganti dengan API Key Gemini kamu
genai.configure(api_key="AIzaSyBAlVu0TMQvFk2MBjbSvAF2y23kUU44ry0")

app = Flask(__name__)
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    reply = ""
    if request.method == "POST":
        daerah = request.form["daerah"]
        program = request.form["program"]
        biaya = request.form["biaya"]

        # Format biaya dalam kalimat
        if biaya == "1000000":
            biaya_text = "di bawah 1 juta"
        elif biaya == "5000000":
            biaya_text = "di bawah 5 juta"
        else:
            biaya_text = "di atas 5 juta"

        prompt = (
            f"Saya sedang mencari rekomendasi pesantren di daerah {daerah} "
            f"dengan program {program} dan biaya pendaftaran {biaya_text}. "
            f"Tolong berikan 4 - 5 rekomendasi yang cocok "
            f"nama, keunggulan, lokasi, akun media sosial link pendaftaran, kalo ada tolong di sampaikan"
            f"Selalu mulai dengan kalimat 'Assalamu’alaikum Sahabat GoPesantren'."
            f"hilangkan kata tentu dalam memberi jawaban"
        )

        response = model.generate_content(prompt)
        reply_raw = response.text
        reply = markdown.markdown(reply_raw)

    return render_template("go_pesantren.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
