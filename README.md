
# Mashup Generator
A full-stack Python application that automatically creates audio mashups by downloading songs from YouTube, trimming them to a specified duration, merging them together, and delivering the final mashup via email.

---

## Features

- **YouTube Integration** - Automatically searches and downloads songs
- **Smart Trimming** - Trims each song to specified duration
- **Audio Merging** - Seamlessly combines multiple tracks
- **Email Delivery** - Sends mashup directly to user's email
- **Web Interface** - Beautiful Flask-based web UI
- **CLI Support** - Full command-line interface (assignment requirement)
- **Input Validation** - Ensures valid parameters
- **ZIP Compression** - Creates downloadable ZIP files
- **Secure** - Uses environment variables for credentials

---

## Command Line Usage (Assignment Requirement)

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
- `AudioDuration` - Duration in seconds to trim each song (must be > 30)
- `OutputFileName` - Name of the output mashup file

---

## Web Application Usage

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

## Deployment on Railway

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

## Project Structure

```
Mashup-Assignment-102303289/
│
├── 102303289.py           
├── app.py                 
├── mashup.py              
│
├── templates/
│   └── index.html          
│
├── static/
│   └── style.css                      
│
├── images/                
│   ├── webapp-screenshot.png
│   ├── cli-screenshot.png
│   └── email-screenshot.png
│
├── requirements.txt       
├── runtime.txt            
├── Dockerfile             
├── .gitignore             
└── README.md         
```

---

## Technologies Used

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

## How It Works

1. **User submits form** with singer name, video count, duration, and email
2. **YouTube search** finds matching songs using yt-dlp
3. **Download audio** in best available quality
4. **Trim each song** to specified duration using pydub
5. **Merge all clips** into single mashup file
6. **Create ZIP archive** containing the mashup
7. **Send via email** using Gmail SMTP
8. **Cleanup** temporary files

---

---

## Performance Metrics

| Metric | Value |
|--------|-------|
| Average download time (per video) | ~10-15 seconds |
| Processing time (10 videos) | ~2-3 minutes |
| Output file size | ~5-10 MB |
| Email delivery time | ~5-10 seconds |

---
**Project Link:** [https://github.com/yourusername/Mashup-Assignment-102303289](https://github.com/yourusername/Mashup-Assignment-102303289)

---
