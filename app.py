from flask import Flask, request, jsonify, render_template
from lang import Languages

app = Flask(__name__)
l = Languages()

maps = {
    '1': 'aNbN',
    '2': 'aNb2N',
    '3': 'aMbNcM+N',
    '4': 'aNbMcMdN',
    '5': 'wcwR',
    '6': 'wwR',
    '7': 'aMbN_mGeN',
    '8': 'balancedParens',
    '9': 'aNbNcM',
    '10': 'equalAsBsAnyOrder',
    '11': 'aNbN_or_aNb2N'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    lang_choice = data.get('language')
    input_string = data.get('input_string', '')

    if lang_choice not in maps:
        return jsonify({"error": "Invalid language selected"}), 400

    pda = l.get_lang(maps[lang_choice])
    
    result = pda.exec_web(input_string) 
    
    return jsonify({"trace": result})

if __name__ == '__main__':
    app.run(debug=True)