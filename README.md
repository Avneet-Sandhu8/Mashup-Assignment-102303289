# 🎵 Mashup Generator

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Railway](https://img.shields.io/badge/Deployed%20on-Railway-blueviolet.svg)](https://railway.app/)

A full-stack Python application that automatically creates audio mashups by downloading songs from YouTube, trimming them to a specified duration, merging them together, and delivering the final mashup via email.

---

## 📸 Screenshots

### Web Interface
<div align="center">
  <img src="images/webapp-screenshot.png" alt="Mashup Generator Web Interface" width="600"/>
  <p><i>Beautiful and intuitive web interface for creating mashups</i></p>
</div>

### Command Line Interface
<div align="center">
  <img src="images/cli-screenshot.png" alt="CLI Version" width="600"/>
  <p><i>Full-featured command-line interface for advanced users</i></p>
</div>

### Email Delivery
<div align="center">
  <img src="images/email-screenshot.png" alt="Email with Mashup" width="600"/>
  <p><i>Automatic email delivery with ZIP attachment</i></p>
</div>

---

## 🔗 Live Demo

**🌐 Try it now:** [https://your-railway-app.railway.app](https://your-railway-app.railway.app)

> **Note:** Replace the URL above with your actual Railway deployment link

**📺 Video Demo:** [Watch on YouTube](https://youtube.com/your-video-link)

---

## ✨ Features

- 🎵 **YouTube Integration** - Automatically searches and downloads songs
- ✂️ **Smart Trimming** - Trims each song to specified duration
- 🎼 **Audio Merging** - Seamlessly combines multiple tracks
- 📧 **Email Delivery** - Sends mashup directly to user's email
- 🌐 **Web Interface** - Beautiful Flask-based web UI
- 💻 **CLI Support** - Full command-line interface (assignment requirement)
- ✅ **Input Validation** - Ensures valid parameters
- 🗜️ **ZIP Compression** - Creates downloadable ZIP files
- 🔒 **Secure** - Uses environment variables for credentials

---

## 🖥️ Command Line Usage (Assignment Requirement)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Mashup-Assignment-102303289.git
cd Mashup-Assignment-102303289

# Install dependencies
pip install -r requirements.txt

# Install FFmpeg
# Windows: Download from https://ffmpeg.org/download.html
# Mac: brew install ffmpeg
# Linux: sudo apt-get install ffmpeg
```

### Run CLI Version

```bash
python 102303289.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>
```

### Example

```bash
python 102303289.py "Arijit Singh" 15 30 arijit_mashup.mp3
```

**Parameters:**
- `SingerName` - Name of the singer/artist
- `NumberOfVideos` - Number of videos to download (must be > 10)
- `AudioDuration` - Duration in seconds to trim each song (must be > 20)
- `OutputFileName` - Name of the output mashup file

### Sample Output

```
Downloading videos...
Processing audio...
Exporting final mashup...
Mashup created successfully!
✓ Output saved to: arijit_mashup.mp3
```

---

## 🌐 Web Application Usage

### Local Setup

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Set Environment Variables**

**Windows (Command Prompt):**
```cmd
set SENDER_EMAIL=your-email@gmail.com
set APP_PASSWORD=your-app-password
```

**Windows (PowerShell):**
```powershell
$env:SENDER_EMAIL="your-email@gmail.com"
$env:APP_PASSWORD="your-app-password"
```

**Mac/Linux:**
```bash
export SENDER_EMAIL=your-email@gmail.com
export APP_PASSWORD=your-app-password
```

3. **Get Gmail App Password**
   - Go to [Google Account Settings](https://myaccount.google.com/apppasswords)
   - Enable 2-Factor Authentication
   - Generate App Password for "Mail"
   - Use the 16-character password as `APP_PASSWORD`

4. **Run the Application**
```bash
python app.py
```

5. **Open Browser**
```
http://127.0.0.1:5000
```

---

## 🚀 Deployment on Railway

### Quick Deploy

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/your-template)

### Manual Deployment Steps

1. **Fork this repository**

2. **Create Railway Account** at [railway.app](https://railway.app)

3. **Create New Project** → Deploy from GitHub

4. **Add Environment Variables** in Railway Dashboard:
   ```
   SENDER_EMAIL = your-email@gmail.com
   APP_PASSWORD = your-16-char-app-password
   ```

5. **Deploy** - Railway will automatically build and deploy

6. **Access** your app at the provided Railway URL

### Railway Configuration Files

- `railway.toml` - Railway-specific configuration
- `Procfile` - Defines how to run the app
- `Dockerfile` - Container configuration
- `runtime.txt` - Python version specification

---

## 📂 Project Structure

```
Mashup-Assignment-102303289/
│
├── 📄 102303289.py           # CLI version (assignment requirement)
├── 📄 app.py                 # Flask web application
├── 📄 mashup.py              # Core mashup logic
│
├── 📁 templates/
│   └── index.html            # Web UI template
│
├── 📁 static/
│   └── style.css             # Styling
│
├── 📁 downloads/             # Temporary download folder (auto-created)
│
├── 📁 images/                # Screenshots for README
│   ├── webapp-screenshot.png
│   ├── cli-screenshot.png
│   └── email-screenshot.png
│
├── 📄 requirements.txt       # Python dependencies
├── 📄 runtime.txt            # Python version
├── 📄 Dockerfile             # Docker configuration
├── 📄 Procfile               # Railway/Heroku configuration
├── 📄 railway.toml           # Railway-specific config
├── 📄 .gitignore             # Git ignore rules
└── 📄 README.md              # This file
```

---

## ⚙️ Technologies Used

### Backend
- **Python 3.11** - Core programming language
- **Flask 3.1.2** - Web framework
- **yt-dlp** - YouTube video/audio downloader
- **pydub** - Audio processing and manipulation
- **FFmpeg** - Audio/video converter

### Email & Deployment
- **smtplib** - Email sending (Gmail SMTP)
- **Railway** - Cloud deployment platform
- **Gunicorn** - Production WSGI server

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with gradient backgrounds
- **Responsive Design** - Mobile-friendly interface

---

## 🎯 How It Works

1. **User submits form** with singer name, video count, duration, and email
2. **YouTube search** finds matching songs using yt-dlp
3. **Download audio** in best available quality
4. **Trim each song** to specified duration using pydub
5. **Merge all clips** into single mashup file
6. **Create ZIP archive** containing the mashup
7. **Send via email** using Gmail SMTP
8. **Cleanup** temporary files

---

## 🧪 Testing

### Test Cases

```bash
# Valid test case
python 102303289.py "Arijit Singh" 11 30 test1.mp3

# Test with more videos
python 102303289.py "Shreya Ghoshal" 15 25 test2.mp3

# Test with longer duration
python 102303289.py "AR Rahman" 12 45 test3.mp3
```

### Error Handling

```bash
# Should fail: too few videos
python 102303289.py "Singer" 5 30 output.mp3
# Error: Number of videos must be greater than 10

# Should fail: duration too short
python 102303289.py "Singer" 11 15 output.mp3
# Error: Duration must be greater than 20 seconds
```

---

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| Average download time (per video) | ~10-15 seconds |
| Processing time (10 videos) | ~2-3 minutes |
| Output file size | ~5-10 MB |
| Email delivery time | ~5-10 seconds |

---

## 🔒 Security & Privacy

- ✅ Environment variables for sensitive data
- ✅ Gmail App Password (not main password)
- ✅ Automatic file cleanup after sending
- ✅ No data persistence on server
- ✅ Ephemeral filesystem on Railway

---

## 🐛 Troubleshooting

### Issue: "Email authentication failed"
**Solution:** 
- Enable 2FA on Google Account
- Generate App Password (not regular password)
- Use full 16-character App Password

### Issue: "FFmpeg not found"
**Solution:**
- **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH
- **Mac:** `brew install ffmpeg`
- **Linux:** `sudo apt-get install ffmpeg`

### Issue: "No videos found"
**Solution:**
- Check singer name spelling
- Ensure internet connection
- Try with more popular artist names

### Issue: Railway build timeout
**Solution:**
- Use `railway.toml` instead of Dockerfile
- Check Railway logs for specific errors
- Ensure all dependencies are in `requirements.txt`

---

## 📝 Assignment Details

**Course:** Web Technologies  
**Assignment:** Mashup Creator  
**Roll Number:** 102303289  
**Name:** Avneet Sandhu  
**Branch:** Computer Science Engineering  

### Requirements Met ✓

- [x] Command-line interface accepting 4 parameters
- [x] Download videos from YouTube (>10 videos)
- [x] Audio trimming (>20 seconds)
- [x] Merge into single file
- [x] Create ZIP archive
- [x] Email functionality
- [x] Web interface (bonus)
- [x] Cloud deployment (bonus)
- [x] Error handling
- [x] Documentation

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube downloader
- [pydub](https://github.com/jiaaro/pydub) - Audio processing
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Railway](https://railway.app/) - Deployment platform

---

## 📧 Contact

**Avneet Sandhu**  
- Email: asandhu2_be23@thapar.edu
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

**Project Link:** [https://github.com/yourusername/Mashup-Assignment-102303289](https://github.com/yourusername/Mashup-Assignment-102303289)

---

<div align="center">
  <p>⭐ Star this repo if you found it helpful!</p>
  <p>Made with ❤️ for Web Technologies Assignment</p>
</div>
