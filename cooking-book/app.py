from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


@app.route('/Main', methods=['GET'])
def all_dishes():
    return jsonify({
        'status': 'success',
        'dishes': dishes
    })


dishes = [
    {
        'img': 'category1.png',
        'title': 'Первые блюда',
    },
    {
        'img': 'category2.png',
        'title': 'Вторые блюда',
    },
    {
        'img': 'category3.png',
        'title': 'Десерты',
    },
    {
        'img': 'category4.png',
        'title': 'Закуски',
    }
]

if __name__ == '__main__':
    app.run(debug=True)