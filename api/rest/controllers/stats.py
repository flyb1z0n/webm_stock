from flask import jsonify
from rest import app


@app.route('/', methods=['GET'])
def index():
    links = []
    for rule in app.url_map.iter_rules():
        methods = rule.methods
        methods.discard('HEAD')
        methods.discard('OPTIONS')
        links.append({
            'methods': list(methods),
            'url': str(rule)
            })
    return jsonify(links)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'ok'
    })
