# Video Generation System - Implementation Guide

## Overview

This system automatically generates educational slideshow videos from JSON files containing image descriptions and narration content. It uses Google's Gemini AI for image generation and text-to-speech, then combines them using MoviePy.

## Features

- **Automated Image Generation**: Creates images from text descriptions using Gemini 2.5 Flash Image
- **Text-to-Speech**: Converts narration content to audio using Gemini 2.5 Pro TTS
- **Video Compilation**: Combines images and audio into slideshow videos with MoviePy
- **Batch Processing**: Processes multiple JSON files automatically
- **Organized Output**: Creates structured folders for images, audio, and final videos

## File Structure

The system processes JSON files from `vlsi/video/` and creates organized output:

```
vlsi/video/
├── 1.json, 2.json, ..., 8.json    # Input JSON files
├── output_1/
│   ├── images/
│   │   ├── section_0.png
│   │   ├── section_1.png
│   │   └── ...
│   ├── audio/
│   │   ├── section_0.wav
│   │   ├── section_1.wav
│   │   └── ...
│   └── final_video.mp4
├── output_2/
│   └── ... (same structure)
└── ...
```

## JSON File Format

Each JSON file should contain a `sections` array with objects having:

```json
{
  "sections": [
    {
      "image_description": "Detailed description of the visual to generate",
      "content": "The narration text that will be converted to speech"
    }
  ]
}
```

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages:
- `google-genai` - For Gemini AI image and audio generation
- `python-dotenv` - For environment variable management
- `moviepy` - For video creation and editing
- `pillow` - For image processing

### 2. Configure API Key

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Usage

### Option 1: Process All Videos (Recommended)

```python
from agent.video_genrator import process_all_videos

# Process all JSON files (1.json through 8.json)
process_all_videos()
```

Or run from command line:
```bash
python agent/video_genrator.py
```

### Option 2: Process Single Video

```python
from agent.video_genrator import generate_video_from_json

# Generate video from a single JSON file
video_path = generate_video_from_json(
    json_path="vlsi/video/1.json",
    output_dir="vlsi/video/output_1"
)
print(f"Video saved to: {video_path}")
```

### Option 3: Use Example Script

```bash
python example_video_usage.py
```

## How It Works

1. **Read JSON**: Loads the JSON file and extracts sections
2. **For Each Section**:
   - Generates an image from `image_description` using Gemini Image model
   - Generates audio from `content` using Gemini TTS model
   - Saves both with organized naming (`section_0`, `section_1`, etc.)
3. **Create Video Clips**: 
   - Creates ImageClip for each image
   - Sets duration to match audio length
   - Attaches audio to image
4. **Concatenate**: Combines all clips into one video
5. **Export**: Saves final video as MP4 with H.264 video and AAC audio

## Modified Files

### `agent/create_image.py`
- Added `output_path` parameter to `generate()` function
- Returns the saved file path
- Maintains backward compatibility (output_path is optional)

### `agent/voice_genrator.py`
- Added `output_path` parameter to `generate()` function
- Returns the saved file path
- Maintains backward compatibility (output_path is optional)

### `agent/video_genrator.py` (New)
- Main video generation logic
- `generate_video_from_json()`: Processes single JSON file
- `process_all_videos()`: Batch processes all JSON files

## Video Specifications

- **Format**: MP4
- **Video Codec**: H.264 (libx264)
- **Audio Codec**: AAC
- **Frame Rate**: 24 fps
- **Duration**: Each image is displayed for the duration of its audio
- **Resolution**: Based on generated images (typically 1024x1024 or similar)

## Error Handling

The system includes robust error handling:
- Skips sections with missing data
- Continues processing if a single section fails
- Provides detailed console output for debugging
- Validates JSON structure before processing

## Performance Notes

- Each section requires 2 API calls (image + audio)
- Processing time depends on:
  - Number of sections per JSON
  - API response times (typically 3-10 seconds per generation)
  - Video encoding time (depends on video length)
- Estimated time: 30-60 seconds per section

## Example Output

When running `process_all_videos()`, you'll see:

```
Found 8 JSON files to process
============================================================
Processing 1.json -> output_1/
============================================================

Processing 10 sections from vlsi/video/1.json...

--- Processing Section 0 ---
Generating image for section 0...
File saved to: vlsi/video/output_1/images/section_0.png
Generating audio for section 0...
File saved to: vlsi/video/output_1/audio/section_0.wav
Section 0 completed (duration: 15.23s)

[... continues for all sections ...]

Combining all clips into final video...
Exporting video to vlsi/video/output_1/final_video.mp4...
✓ Video generation complete: vlsi/video/output_1/final_video.mp4

[... continues for all JSON files ...]
```

## Troubleshooting

### Import Error for moviepy
```bash
pip install moviepy
```

### API Key Error
- Ensure `.env` file exists with valid `GEMINI_API_KEY`
- Check that `python-dotenv` is installed

### Video Encoding Error
- Ensure FFmpeg is installed on your system
- MoviePy uses FFmpeg for video encoding

### Memory Issues
- Process videos one at a time instead of batch processing
- Close clips properly (handled automatically in the code)

## Next Steps

You can now:
1. Run `python agent/video_genrator.py` to process all videos
2. Find your generated videos in `vlsi/video/output_X/final_video.mp4`
3. Review images and audio in their respective folders
4. Customize video settings in `video_genrator.py` (fps, codec, etc.)

