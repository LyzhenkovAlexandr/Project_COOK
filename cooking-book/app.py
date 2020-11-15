from flask import Flask, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

# sanity check route
@app.route('/hot_list/hot_1', methods=['GET'])
def all_card():
    return jsonify({
        'status': 'success',
        'card': CARD
    })
CARD = [
{
    'title': 'text1',
    'text': 'text1',
    'id': '1',
},
{
    'title': 'text2',
    'text': 'text2',
    'id': '2',
},
{
    'title': 'text3',
    'text': 'text3',
    'id': '3',
},
]
if __name__ == '__main__':
    app.run()
