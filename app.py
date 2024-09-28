from flask import Flask, request, jsonify


api = Flask(__name__)

@api.route('/', methods=['GET'])
def weclome():
    return 'Hello, world!'


@api.route('/file/save', methods=['POST'])
def save_data():
    data = request.get_json()
    print ('json packet', data)
    
    if 'obj' not in data:
        return jsonify({'error': 'Invalid request'}), 400
    
    #for item in data: print(item)
    values = data['obj']
    try:
        #for item in value: print(item)
        concaten_val = ' '.join(str(val) for val in values)
        with open("data.txt", "a") as fout:
            fout.write(concaten_val)
            fout.write('\n')
        return jsonify({'answer_data': 'File was save', 'concaten_data': concaten_val}), 202
    except ValueError:
        return jsonify({'error': 'Invalid request'}), 400
    
@api.route('/file/data', methods=['GET'])
def get_file_data():
    with open("data.txt", 'r') as fin:
        data_file = fin.readlines()
        fin.close()
    return {'file_data': data_file}
