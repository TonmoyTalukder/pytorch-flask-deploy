from flask import Flask, request, jsonify

from torch_utils import transform_image, get_prediction

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    # xxx.png
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Enable debug mode
app.debug = True

@app.route('/')
def hello():
    return 'Hello, World! I am from Flask.'

if __name__ == '__main__':
    app.run()

@app.route('/predict', methods=['POST'])
def predict():
    # 1. load image
    if request.method == 'POST':
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({'error': 'no file'})
        if not allowed_file(file.filename):
            return jsonify({'error': 'format not supported'})
        

        try:
            img_bytes = file.read()
    # 2. image -> tensor
            tensor = transform_image(img_bytes)
    # 3. prediction
            prediction = get_prediction(tensor)
            data = {'prediction': prediction.item(), 'class_name': str(prediction.item())}
            return jsonify(data)
        except:
            return jsonify({'error': 'error during prediction'})

    # 4. return json
    # return jsonify({'result': '1'})

    # if request.method == 'POST':
    #     file = request.files.get('file')
    #     if file is None or file.filename == "":
    #         return jsonify({'error': 'no file'})
    #     if not allowed_file(file.filename):
    #         return jsonify({'error': 'format not supported'})

    #     try:
    #         img_bytes = file.read()
    #         tensor = transform_image(img_bytes)
    #         prediction = get_prediction(tensor)
    #         data = {'prediction': prediction.item(), 'class_name': str(prediction.item())}
    #         return jsonify(data)
    #     except:
    #         return jsonify({'error': 'error during prediction'})