import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Any

from digital_notes_json_genrator import generate as generate_json


def process_folder(
    folder_path: str,
    output_base_dir: str = "vlsi"
) -> Dict[str, Any]:
    """
    Process all images in a folder: generate combined JSON.
    
    Args:
        folder_path: Path to the folder containing images
        output_base_dir: Base directory for outputs (default: vlsi)
        
    Returns:
        Dict with processing results
    """
    folder = Path(folder_path)
    folder_name = folder.name
    
    print(f"\n{'='*60}")
    print(f"Processing Folder: {folder_name}")
    print(f"{'='*60}")
    
    # Find all image files in the folder
    image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".bmp"}
    image_files = sorted([
        f for f in folder.iterdir()
        if f.suffix.lower() in image_extensions and not f.name.startswith("Screenshot")
    ])
    
    if not image_files:
        print(f"   ✗ No image files found in folder")
        return {"error": f"No images found in {folder_name}"}
    
    print(f"   Found {len(image_files)} image(s) in folder")
    
    # Process each image and combine results
    combined_descriptions = []
    all_image_prompts = []
    
    for idx, image_file in enumerate(image_files, 1):
        print(f"\n   Processing image {idx}/{len(image_files)}: {image_file.name}")
        
        # Read the image file
        try:
            with open(image_file, "rb") as img_file:
                image_data = img_file.read()
        except Exception as e:
            print(f"   ✗ Failed to read image: {str(e)}")
            continue
        
        # Generate JSON from image
        print(f"      Generating JSON...")
        try:
            json_response = generate_json(image_data)
            response_data = json.loads(json_response)
            
            # Extract the actual content from the nested response structure
            if "candidates" in response_data:
                # Check if there's a pre-parsed field (for structured output)
                if "parsed" in response_data and response_data["parsed"]:
                    parsed_data = response_data["parsed"]
                    print(f"      ✓ Using pre-parsed structured output")
                else:
                    # Fallback: Extract from parts and combine all text parts
                    parts = response_data["candidates"][0]["content"]["parts"]
                    
                    # Combine all text parts
                    text_parts = []
                    for part in parts:
                        if "text" in part and part["text"]:
                            text_parts.append(part["text"])
                    
                    content_text = "".join(text_parts)
                    
                    # Try different parsing approaches
                    try:
                        # First try: direct JSON parse
                        parsed_data = json.loads(content_text)
                    except json.JSONDecodeError:
                        # Second try: fix common issues with escaped strings
                        try:
                            # Remove markdown code blocks if present
                            content_text = content_text.strip()
                            if content_text.startswith("```json"):
                                content_text = content_text[7:]
                            if content_text.startswith("```"):
                                content_text = content_text[3:]
                            if content_text.endswith("```"):
                                content_text = content_text[:-3]
                            content_text = content_text.strip()
                            
                            parsed_data = json.loads(content_text)
                        except json.JSONDecodeError as e:
                            print(f"      ✗ JSON parse error: {str(e)}")
                            continue
            else:
                parsed_data = response_data
            
            # Extract description and image prompts
            description = parsed_data.get("Description", "")
            image_prompts = parsed_data.get("Images", [])
            
            if description:
                combined_descriptions.append({
                    "image": image_file.name,
                    "description": description
                })
                print(f"      ✓ Description extracted ({len(description)} chars)")
            
            if image_prompts:
                all_image_prompts.extend(image_prompts)
                print(f"      ✓ Found {len(image_prompts)} image prompt(s)")
                
        except Exception as e:
            print(f"      ✗ Failed to generate JSON: {str(e)}")
            continue
    
    if not combined_descriptions:
        return {"error": f"No descriptions generated for {folder_name}"}
    
    # Create combined JSON structure
    combined_json = {
        "folder": folder_name,
        "total_images": len(image_files),
        "processed_images": len(combined_descriptions),
        "descriptions": combined_descriptions,
        "image_prompts": all_image_prompts
    }
    
    # Save JSON file to the folder
    json_path = folder / f"{folder_name}.json"
    try:
        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(combined_json, json_file, indent=2, ensure_ascii=False)
        print(f"\n   ✓ JSON saved to: {json_path}")
    except Exception as e:
        return {"error": f"Failed to save JSON: {str(e)}"}
    
    return {
        "folder": folder_name,
        "json_file": str(json_path),
        "images_processed": len(combined_descriptions),
        "total_images": len(image_files),
        "image_prompts_count": len(all_image_prompts)
    }


def process_all_folders(
    base_dir: str = "vlsi"
) -> List[Dict[str, Any]]:
    """
    Process all folders in the base directory.
    
    Args:
        base_dir: Base directory containing numbered folders
        
    Returns:
        List of processing results for each folder
    """
    base_path = Path(base_dir)
    
    if not base_path.exists():
        print(f"Error: Base directory '{base_dir}' does not exist")
        return []
    
    # Find all subdirectories (numbered folders)
    folders = [
        f for f in base_path.iterdir()
        if f.is_dir()
    ]
    
    if not folders:
        print(f"No folders found in '{base_dir}'")
        return []
    
    # Sort folders numerically if they have numeric names
    try:
        folders = sorted(folders, key=lambda x: int(x.name) if x.name.isdigit() else x.name)
    except ValueError:
        folders = sorted(folders)
    
    print(f"\nFound {len(folders)} folder(s) to process: {[f.name for f in folders]}")
    
    results = []
    for folder in folders:
        result = process_folder(str(folder), base_dir)
        results.append(result)
    
    # Print summary
    print(f"\n{'='*60}")
    print("PROCESSING SUMMARY")
    print(f"{'='*60}")
    successful = sum(1 for r in results if "error" not in r)
    print(f"Total folders processed: {len(results)}")
    print(f"Successful: {successful}")
    print(f"Failed: {len(results) - successful}")
    
    if successful > 0:
        total_images = sum(r.get("images_processed", 0) for r in results if "error" not in r)
        total_prompts = sum(r.get("image_prompts_count", 0) for r in results if "error" not in r)
        print(f"Total images processed: {total_images}")
        print(f"Total image prompts collected: {total_prompts}")
    
    return results


if __name__ == "__main__":
    
    # Process all folders in vlsi directory
    results = process_all_folders(
        base_dir="vlsi"
    )
    
    # Print detailed results
    print("\nDetailed Results:")
    for result in results:
        if "error" in result:
            print(f"  ✗ Error: {result['error']}")
        else:
            print(f"  ✓ Folder {result['folder']}: {result['images_processed']}/{result['total_images']} images processed")
            print(f"    JSON: {result['json_file']}")
            print(f"    Image prompts: {result['image_prompts_count']}")
