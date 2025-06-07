from flask import Flask, render_template, request, jsonify
from yamliwrapper.yamli import Transliterator

class Yamli:
    def transliterate(self, word):
        """Wrapper to match the expected API"""
        transliterator = Transliterator(word)
        return transliterator.candidates

app = Flask(__name__)
yamli = Yamli()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/transliterate', methods=['POST'])
def transliterate():
    try:
        data = request.get_json()
        text = data.get('text', '') or data.get('word', '')
        
        if not text:
            return jsonify({'error': 'No text provided', 'success': False}), 400
        
        # Get transliteration suggestions
        suggestions = yamli.transliterate(text)
        
        return jsonify({
            'success': True,
            'candidates': suggestions,
            'best_match': suggestions[0] if suggestions else text,
            'original': text
        })
    
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500

@app.route('/robots.txt')
def robots_txt():
    """Generate robots.txt for SEO"""
    robots_content = """User-agent: *
Allow: /
Allow: /terms
Allow: /privacy
Sitemap: https://arabizi.com/sitemap.xml

# Crawl-delay for respectful crawling
Crawl-delay: 1
"""
    return robots_content, 200, {'Content-Type': 'text/plain'}

@app.route('/sitemap.xml')
def sitemap_xml():
    """Generate sitemap.xml for SEO"""
    sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://arabizi.com/</loc>
        <lastmod>2024-12-01</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://arabizi.com/terms</loc>
        <lastmod>2024-12-01</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>https://arabizi.com/privacy</loc>
        <lastmod>2024-12-01</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
</urlset>"""
    return sitemap_content, 200, {'Content-Type': 'application/xml'}

if __name__ == '__main__':
    app.run(debug=True, port=5001) 