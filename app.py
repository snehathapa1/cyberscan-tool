from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form.get('url')

    if not url:
        return render_template('index.html', result="Please enter a URL.")

    try:
        command = f"nikto -h {url} -ssl"
        result = subprocess.getoutput(command)
    except Exception as e:
        result = f"Error running scan: {str(e)}"

    return render_template('index.html', result=result, scanned_url=url)

if __name__ == '__main__':
    app.run(debug=True)