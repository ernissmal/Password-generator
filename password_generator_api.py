# password_generator_api.py

from flask import Flask, request, jsonify
from password_generator import (
    generate_password,
    generate_memorable_password,
    generate_hex_password,
    generate_base64_password,
    generate_pronounceable_password,
    generate_pin,
    generate_alphanumeric_password
)

app = Flask(__name__)

@app.route('/generate_password', methods=['POST'])
def generate():
    data = request.get_json()
    try:
        length = int(data['length'])
        include_uppercase = data['include_uppercase']
        include_digits = data['include_digits']
        include_symbols = data['include_symbols']
        
        algorithm = data.get('algorithm', 'Random Characters')
        
        if algorithm == 'Random Characters':
            password = generate_password(length, include_uppercase, include_digits, include_symbols)
        elif algorithm == 'Memorable Words':
            words_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
            password = generate_memorable_password(words_list, num_words=length // 4)
        elif algorithm == 'Hexadecimal':
            password = generate_hex_password(length)
        elif algorithm == 'Base64':
            password = generate_base64_password(length)
        elif algorithm == 'Pronounceable':
            password = generate_pronounceable_password(length)
        elif algorithm == 'PIN':
            password = generate_pin(length)
        elif algorithm == 'Alphanumeric':
            password = generate_alphanumeric_password(length)
        else:
            return jsonify({"error": "Invalid algorithm selected."}), 400
        
        return jsonify({"password": password})
    except (KeyError, ValueError) as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
