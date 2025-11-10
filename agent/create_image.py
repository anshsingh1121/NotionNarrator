# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import mimetypes
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv(override=True)

def save_binary_file(file_name, data):
    f = open(file_name, "wb")
    f.write(data)
    f.close()
    print(f"File saved to to: {file_name}")


def generate(text: str, output_path: str = None):
    """Generate an image from text description.
    
    Args:
        text: The text description for image generation
        output_path: Optional path where to save the image. If None, uses default naming.
    
    Returns:
        str: Path to the saved image file
    """
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-flash-image"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=text),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_modalities=[
            "IMAGE",
            "TEXT",
        ],
    )

    file_index = 0
    saved_file_path = None
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if (
            chunk.candidates is None
            or chunk.candidates[0].content is None
            or chunk.candidates[0].content.parts is None
        ):
            continue
        if chunk.candidates[0].content.parts[0].inline_data and chunk.candidates[0].content.parts[0].inline_data.data:
            inline_data = chunk.candidates[0].content.parts[0].inline_data
            data_buffer = inline_data.data
            file_extension = mimetypes.guess_extension(inline_data.mime_type)
            
            if output_path:
                file_name = output_path
            else:
                file_name = f"ENTER_FILE_NAME_{file_index}"
                file_name = f"{file_name}{file_extension}"
            
            save_binary_file(file_name, data_buffer)
            saved_file_path = file_name
            file_index += 1
        else:
            print(chunk.text)
    
    return saved_file_path

if __name__ == "__main__":
    generate("A beautiful sunset over a calm ocean")
