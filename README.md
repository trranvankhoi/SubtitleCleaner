# SubtitleCleaner

SubtitleCleaner is a local desktop application for removing hardcoded subtitles from video files. It is designed for non-commercial and educational use only.

## Features

- Remove burned-in subtitles from MP4, MKV, MOV, AVI, WEBM
- Manual selection or automatic subtitle region detection
- High-quality inpainting with GPU/CPU fallback
- Preserves audio and minimizes re-encoding
- Modern PySide6 interface with preview and queue support

## Installation

1. Install Python 3.11+.
2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate  # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> `torch` must be installed for your specific CUDA version. See https://pytorch.org/get-started/locally/ for the right install command.

## Run

```bash
python main.py
```

## Build with PyInstaller

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

Note: bundled application size may be large because of `torch` and model weights.

## Project Structure

- `main.py` - application entry point
- `app.py` - application bootstrap
- `gui/` - UI components
- `core/` - video processing and inpainting pipeline
- `utils/` - shared utilities
- `models/` - inpainting and detection model integrations
- `assets/` - icons and resources

## License Notice

The `ProPainter` high-quality inpainting model used in this project is licensed under S-Lab License 1.0 for non-commercial and research use only.

## FAQ

- Q: Does this app send video data to the cloud?
  A: No. All processing is local.

- Q: Can I use this project commercially?
  A: Not with the included ProPainter mode. Replace the model with a compatible commercial license before any commercial use.
