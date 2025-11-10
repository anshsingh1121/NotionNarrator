# Notes Agent - Image to Markdown Documentation Generator

This project automatically converts handwritten or typed notes from images into well-formatted Markdown documentation with AI-generated illustrations.

## Features

- 📝 **Automatic Transcription**: Converts image notes to structured Markdown
- 🎨 **Image Generation**: Creates diagrams and illustrations from descriptions
- 🎬 **Video Generation**: Creates educational slideshow videos with AI-generated images and narration
- 🔊 **Voice Generation**: Generates natural-sounding narration from text
- 📚 **Batch Processing**: Processes multiple images automatically
- 🗂️ **Organized Output**: Creates separate markdown files with embedded images

## Prerequisites

1. Python 3.13+ (or compatible version)
2. Google Gemini API Key

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install google-genai python-dotenv moviepy pillow
```

3. Set up your Gemini API key:
```bash
# Windows PowerShell
$env:GEMINI_API_KEY="your-api-key-here"

# Linux/Mac
export GEMINI_API_KEY="your-api-key-here"
```

Or create a `.env` file:
```
GEMINI_API_KEY=your-api-key-here
```

## Usage

### 1. Generate Video from JSON

The video generator creates educational videos from your JSON output files with AI-generated images and narration.

**Process all VLSI folders:**
```bash
python agent/video_genrator.py
```

**Process a specific folder:**
```bash
python agent/video_genrator.py vlsi/1
```

This will:
1. Read the `output_*.json` file from each folder
2. Generate images for each section based on `image_description`
3. Generate audio narration for each section based on `content`
4. Create a video slideshow (`{folder_name}_video.mp4`) combining images and audio

### 2. Process All Images

Place your note images in the `bmsp/files/` directory, then run:

```bash
cd agent
python orchestraor.py
```

### Output Structure

**For markdown generation:**
```
bmsp/
├── files/          # Input images
│   ├── 0.png
│   ├── 1.png
│   └── ...
├── images/         # Generated images
│   ├── 0/
│   │   ├── image_1.png
│   │   └── image_2.png
│   └── 1/
│       └── image_1.png
├── 0.md           # Generated markdown
├── 1.md
└── ...
```

**For video generation:**
```
vlsi/
├── 1/
│   ├── output_1.json       # Input JSON with sections
│   ├── section_0.png       # Generated image for section 0
│   ├── section_0.wav       # Generated audio for section 0
│   ├── section_1.png       # Generated image for section 1
│   ├── section_1.wav       # Generated audio for section 1
│   └── 1_video.mp4         # Final video output
├── 2/
│   └── ...
└── ...
```

Each markdown file contains:
- Formatted, explanatory notes
- Technical definitions and context
- Image references at the bottom

### Example Output

For an input image of circuit notes, you'll get:

**`bmsp/0.md`**:
```markdown
# BJT Common Emitter Amplifier

The Common Emitter (CE) amplifier is one of the three basic...

## Circuit Configuration
...

---

## Generated Images

![Generated Image 1](images/0/image_1.png)
```

## Project Structure

```
Notes_Agent/
├── agent/
│   ├── orchestraor.py              # Main orchestrator
│   ├── json_genrator.py            # JSON generation from images
│   ├── create_image.py             # Image generation from prompts
│   ├── voice_genrator.py           # Voice/audio generation from text
│   └── video_genrator.py           # Video slideshow generator (NEW!)
├── bmsp/
│   ├── files/                      # Input images directory
│   ├── images/                     # Generated images (created automatically)
│   └── *.md                       # Generated markdown files
├── vlsi/
│   ├── 1/                          # Topic folders
│   │   ├── output_1.json          # Structured content
│   │   ├── section_*.png          # Generated images
│   │   ├── section_*.wav          # Generated audio
│   │   └── 1_video.mp4            # Final video
│   └── ...
├── requirements.txt
└── README.md
```

## How It Works

### Markdown Documentation Generation
1. **Image Analysis**: Uses Gemini 2.5 Pro to analyze note images
2. **JSON Generation**: Extracts description and image prompts as structured JSON
3. **Content Enhancement**: Adds explanations, definitions, and context
4. **Image Creation**: Uses Gemini Flash Image to generate diagrams
5. **Markdown Assembly**: Creates formatted documentation with embedded images

### Video Generation Pipeline
1. **JSON Parsing**: Reads `output_*.json` files with sections
2. **Image Generation**: For each section, generates an image from `image_description` using Gemini 2.5 Flash Image
3. **Audio Generation**: Creates narration from `content` using Gemini 2.5 Pro TTS with natural voice
4. **Video Assembly**: Combines images and audio into a seamless slideshow with MoviePy
   - Each section's duration matches its audio length
   - Smooth transitions between sections
   - High-quality video output (H.264, AAC audio)

## JSON Structure for Video Generation

The `output_*.json` files should follow this structure:

```json
{
  "sections": [
    {
      "image_description": "A cinematic shot of a microprocessor...",
      "content": "The narration text that will be converted to speech..."
    },
    {
      "image_description": "An animated diagram showing...",
      "content": "More narration text..."
    }
  ]
}
```

## API Usage

### Video Generation API

```python
from agent.video_genrator import process_json_folder

# Process a single folder
process_json_folder("vlsi/1")
```

### Markdown Generation API

```python
from agent.orchestraor import process_image, process_all_images

# Process a single image
result = process_image("bmsp/files/0.png")

# Process all images in a directory
results = process_all_images(
    input_dir="bmsp/files",
    output_base_dir="bmsp"
)
```

## Troubleshooting

### "GEMINI_API_KEY environment variable not set"
Make sure you've set your API key as an environment variable or in a `.env` file.

### No images generated
Some notes may not contain diagrams. The system will still create markdown documentation.

### Image quality issues
The AI tries to recreate diagrams based on descriptions. You can manually edit the generated images if needed.

## Dependencies

- `google-genai`: Google's Gemini API client for image/audio generation
- `python-dotenv`: Environment variable management
- `moviepy`: Video creation and editing
- `pillow`: Image processing (required by moviepy)

## License

This project is for educational and personal use.

