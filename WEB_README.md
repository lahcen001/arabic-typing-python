# 🌙 Arabizi - Arabic Transliterator Web Interface

A beautiful web interface for the Arabizi Arabic Transliterator API.

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Run the web server:**
   ```bash
   python3 app.py
   ```

3. **Open your browser and visit:**
   ```
   http://localhost:5000
   ```

## ✨ Features

- **Beautiful Modern UI** - Clean, responsive design with gradient backgrounds
- **Real-time Transliteration** - Instant Arabic translations as you type
- **Multiple Candidates** - Shows all possible Arabic translations
- **Click to Copy** - Click any Arabic text to copy to clipboard
- **Example Words** - Quick-access buttons for common words
- **Mobile Friendly** - Responsive design works on all devices
- **Error Handling** - Graceful error messages and loading states

## 🎯 How to Use

1. **Enter Text**: Type English or Franco-Arabic text (like "7abibi", "salam")
2. **Get Results**: See the best match highlighted and all candidates below
3. **Copy Text**: Click any Arabic candidate to copy it to your clipboard
4. **Try Examples**: Use the example buttons for quick testing

## 🔧 API Endpoints

- `GET /` - Serves the main HTML interface
- `POST /transliterate` - JSON API for transliteration
  ```json
  {
    "word": "salam"
  }
  ```

## 📱 Screenshots

The interface includes:
- Gradient purple background
- Centered white card with rounded corners
- Input field with focus effects
- Animated buttons with hover effects
- Grid layout for Arabic candidates
- Copy-to-clipboard functionality

## 🌐 Franco-Arabic Support

The system supports common Franco-Arabic number substitutions:
- `7` → `ح` (7abibi → حبيبي)
- `3` → `ع` (3ala → على)
- `2` → `أ` (2ahlan → أهلاً)

## 🛠️ Technical Details

- **Backend**: Flask (Python)
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **API**: Arabic transliteration service
- **Styling**: Modern CSS with gradients and animations
- **Responsive**: Mobile-first design approach 