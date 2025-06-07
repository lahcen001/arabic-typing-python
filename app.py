#!/usr/bin/env python3

from flask import Flask, render_template, request, jsonify
from yamliwrapper import Transliterator
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transliterate', methods=['POST'])
def transliterate():
    try:
        data = request.get_json()
        word = data.get('word', '').strip()
        
        if not word:
            return jsonify({'error': 'No word provided'}), 400
        
        # Create transliterator instance
        transliterator = Transliterator(word)
        candidates = transliterator.candidates
        
        return jsonify({
            'word': word,
            'candidates': candidates,
            'best_match': candidates[0] if candidates else None,
            'success': True
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 