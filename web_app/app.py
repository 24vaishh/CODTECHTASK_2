from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Ensure the reports directory exists
REPORTS_DIR = "reports"
os.makedirs(REPORTS_DIR, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scan", methods=["GET", "POST"])
def scan():
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            # Perform the scan (dummy data for now)
            results = {"URL": url, "Status": "Scanned Successfully", "Vulnerabilities": ["SQL Injection", "XSS"]}
            return render_template("result.html", results=results)
        return redirect(url_for("home"))
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)