from flask import Flask, request, jsonify
from videohash import VideoHash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域请求

@app.route('/compare', methods=['POST'])
def compare_videos():
    try:
        data = request.json
        url1 = data.get('url1')
        url2 = data.get('url2')
        
        videohash1 = VideoHash(url=url1)
        videohash2 = VideoHash(url=url2)
        
        result = {
            'hash1': videohash1.hash,
            'hash2': videohash2.hash,
            'distance': videohash1 - videohash2,
            'is_similar': videohash2.is_similar(videohash1)
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)