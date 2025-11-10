import json
import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, Tuple, Optional
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from dotenv import load_dotenv
from agent import create_image, voice_genrator

load_dotenv(override=True)


def _generate_image(image_description: str, image_path: Path, idx: int) -> Optional[str]:
    """Generate image for a section.
    
    Args:
        image_description: Description of the image to generate
        image_path: Path where the image will be saved
        idx: Section index for logging
        
    Returns:
        str: Path to generated image or None if failed
    """
    # Check if image already exists
    if image_path.exists():
        print(f"Image for section {idx} already exists. Skipping generation.")
        return str(image_path)
    
    enhanced_description = (
        "Generate an image in a modern educational infographic style, using clean typography "
        "and stylized scientific or technical illustrations. IF description requires multiple "
        f"images try combine them into a single image. {image_description}"
    )
    
    print(f"Generating image for section {idx}...")
    try:
        generated_image = create_image.generate(enhanced_description, str(image_path))
        if not generated_image:
            print(f"Warning: Image generation failed for section {idx}")
            return None
        return str(image_path)
    except Exception as e:
        print(f"Error generating image for section {idx}: {e}")
        return None


def _generate_audio(content: str, audio_path: Path, idx: int) -> Optional[str]:
    """Generate audio for a section.
    
    Args:
        content: Text content to convert to speech
        audio_path: Path where the audio will be saved
        idx: Section index for logging
        
    Returns:
        str: Path to generated audio or None if failed
    """
    # Check if audio already exists
    if audio_path.exists():
        print(f"Audio for section {idx} already exists. Skipping generation.")
        return str(audio_path)
    
    print(f"Generating audio for section {idx}...")
    try:
        generated_audio = voice_genrator.generate(content, str(audio_path))
        if not generated_audio:
            print(f"Warning: Audio generation failed for section {idx}")
            return None
        return str(audio_path)
    except Exception as e:
        print(f"Error generating audio for section {idx}: {e}")
        return None


def _process_section_assets(
    idx: int,
    section: Dict,
    images_dir: Path,
    audio_dir: Path
) -> Tuple[int, Optional[str], Optional[str]]:
    """Process image and audio generation for a section in parallel.
    
    Args:
        idx: Section index
        section: Section data dictionary
        images_dir: Directory for images
        audio_dir: Directory for audio
        
    Returns:
        Tuple of (index, image_path, audio_path)
    """
    image_description = section.get("image_description", "")
    content = section.get("content", "")
    
    if not image_description or not content:
        print(f"Warning: Section {idx} missing image_description or content. Skipping.")
        return (idx, None, None)
    
    image_path = images_dir / f"section_{idx}.png"
    audio_path = audio_dir / f"section_{idx}.wav"
    
    # Generate image and audio in parallel using ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=2) as executor:
        image_future = executor.submit(_generate_image, image_description, image_path, idx)
        audio_future = executor.submit(_generate_audio, content, audio_path, idx)
        
        image_result = image_future.result()
        audio_result = audio_future.result()
    
    return (idx, image_result, audio_result)


def generate_video_from_json(json_path: str, output_dir: str, max_workers: int = 4):
    """Generate a video from a JSON file containing sections with image descriptions and content.
    
    Uses parallel processing to generate images and audio simultaneously for better performance.
    
    Args:
        json_path: Path to the JSON file containing sections
        output_dir: Directory where output files will be saved
        max_workers: Maximum number of parallel workers for section processing (default: 4)
    
    Returns:
        str: Path to the final video file
    """
    # Create output directories
    output_path = Path(output_dir)
    images_dir = output_path / "images"
    audio_dir = output_path / "audio"
    
    images_dir.mkdir(parents=True, exist_ok=True)
    audio_dir.mkdir(parents=True, exist_ok=True)
    
    # Read JSON file
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    sections = data.get("sections", [])
    if not sections:
        raise ValueError(f"No sections found in {json_path}")
    
    print(f"\nProcessing {len(sections)} sections from {json_path}...")
    print(f"Using parallel processing with {max_workers} workers\n")
    
    # Process all sections in parallel
    section_results = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all section processing tasks
        futures = {
            executor.submit(_process_section_assets, idx, section, images_dir, audio_dir): idx
            for idx, section in enumerate(sections)
        }
        
        # Collect results as they complete
        for future in as_completed(futures):
            idx, image_path, audio_path = future.result()
            section_results[idx] = (image_path, audio_path)
            print(f"✓ Section {idx} assets generated")
    
    # Create video clips in order
    print("\nCreating video clips...")
    video_clips = []
    for idx in sorted(section_results.keys()):
        image_path, audio_path = section_results[idx]
        
        if not image_path or not audio_path:
            print(f"Skipping section {idx} due to missing assets")
            continue
        
        # Create video clip with image and audio
        try:
            audio_clip = AudioFileClip(str(audio_path))
            duration = audio_clip.duration
            
            image_clip = ImageClip(str(image_path)).set_duration(duration)
            image_clip = image_clip.set_audio(audio_clip)
            
            video_clips.append(image_clip)
            print(f"✓ Section {idx} clip created (duration: {duration:.2f}s)")
        except Exception as e:
            print(f"Error creating video clip for section {idx}: {e}")
            continue
    
    if not video_clips:
        raise ValueError("No video clips were created successfully")
    
    # Concatenate all clips
    print("\nCombining all clips into final video...")
    final_video = concatenate_videoclips(video_clips, method="compose")
    
    # Export final video
    video_output_path = output_path / "final_video.mp4"
    print(f"Exporting video to {video_output_path}...")
    final_video.write_videofile(
        str(video_output_path),
        fps=24,
        codec="libx264",
        audio_codec="aac"
    )
    
    # Clean up
    final_video.close()
    for clip in video_clips:
        clip.close()
    
    print(f"\n✓ Video generation complete: {video_output_path}")
    return str(video_output_path)


def _process_single_video(json_file: Path, base_path: Path) -> Tuple[str, bool, Optional[str]]:
    """Process a single JSON file to generate a video.
    
    Args:
        json_file: Path to the JSON file
        base_path: Base directory path
        
    Returns:
        Tuple of (filename, success, error_message)
    """
    json_number = json_file.stem
    output_dir = base_path / f"output_{json_number}"
    video_output_path = output_dir / "final_video.mp4"
    
    # Check if final video already exists
    if video_output_path.exists():
        print(f"\n{'='*60}")
        print(f"Video for {json_file.name} already exists. Skipping.")
        print(f"{'='*60}")
        return (json_file.name, True, None)
    
    print(f"\n{'='*60}")
    print(f"Processing {json_file.name} -> output_{json_number}/")
    print(f"{'='*60}")
    
    try:
        generate_video_from_json(str(json_file), str(output_dir))
        return (json_file.name, True, None)
    except Exception as e:
        error_msg = f"Error processing {json_file.name}: {e}"
        print(f"\n✗ {error_msg}")
        return (json_file.name, False, str(e))


def process_all_videos(
    base_dir: str = "vlsi/video",
    max_workers: int = 2,
    parallel: bool = True
):
    """Process all JSON files in the base directory and generate videos.
    
    Args:
        base_dir: Base directory containing JSON files (default: vlsi/video)
        max_workers: Maximum number of videos to process in parallel (default: 2)
        parallel: Whether to process multiple videos in parallel (default: True)
    """
    base_path = Path(base_dir)
    
    if not base_path.exists():
        raise FileNotFoundError(f"Directory {base_dir} not found")
    
    # Find all JSON files (1.json through 8.json)
    json_files = sorted([f for f in base_path.glob("[1-8].json")])
    
    if not json_files:
        print(f"No JSON files found in {base_dir}")
        return
    
    print(f"Found {len(json_files)} JSON files to process")
    print(f"Parallel processing: {'Enabled' if parallel else 'Disabled'}")
    if parallel:
        print(f"Max parallel videos: {max_workers}")
    
    if parallel and len(json_files) > 1:
        # Process videos in parallel
        results = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(_process_single_video, json_file, base_path): json_file
                for json_file in json_files
            }
            
            for future in as_completed(futures):
                results.append(future.result())
        
        # Print summary
        print(f"\n{'='*60}")
        print("SUMMARY")
        print(f"{'='*60}")
        successful = [r for r in results if r[1]]
        failed = [r for r in results if not r[1]]
        
        print(f"✓ Successfully processed: {len(successful)}/{len(results)}")
        for filename, _, _ in successful:
            print(f"  • {filename}")
        
        if failed:
            print(f"\n✗ Failed: {len(failed)}")
            for filename, _, error in failed:
                print(f"  • {filename}: {error}")
    else:
        # Process videos sequentially
        for json_file in json_files:
            _process_single_video(json_file, base_path)
    
    print(f"\n{'='*60}")
    print("All videos processed!")
    print(f"{'='*60}")


if __name__ == "__main__":
    # Process all videos
    process_all_videos()

