import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    sars_cov_2_strain_name = request.form.get('strain')
    cmd = f'python collapse.py -i {sars_cov_2_strain_name}'
    collapsed_strain_name = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
    return collapsed_strain_name


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
