'''main app'''
from flask import Flask

app = Flask(__name__)

@app.route('/v1/data')
def get_data():
    '''
    Fetch data from the API
    '''
    return {'data': 'Hi Flask API!'}

if __name__ == '__main__':
    app.run(debug=True)
