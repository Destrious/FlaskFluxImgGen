from flask import Flask, request, jsonify
import os
import fal_client
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()
os.environ["FAL_KEY"] = os.getenv('FAL_AI_API_KEY')

def generate_image(prompt):
    handler = fal_client.submit(
        "fal-ai/flux/schnell",
        arguments={
            "prompt": prompt,
        },
    )

    result = handler.get()
    return result

@app.route('/generate_image', methods=['GET'])
def generate_image_endpoint():
    data = request.json
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    result = generate_image(prompt)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)