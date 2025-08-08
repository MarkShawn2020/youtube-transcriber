#!/usr/bin/env python3

import json
import sys
import re

def extract_youtube_transcript(json_file, output_file):
    """Extract YouTube transcript from JSON to markdown format without timestamps, with proper speaker formatting"""
    
    try:
        # Read JSON file
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Navigate to transcript segments
        segments = data['actions'][0]['updateEngagementPanelAction']['content']['transcriptRenderer']['content']['transcriptSearchPanelRenderer']['body']['transcriptSegmentListRenderer']['initialSegments']
        
        # Collect all text segments
        full_text = []
        for segment in segments:
            seg_data = segment['transcriptSegmentRenderer']
            
            # Get text from snippet runs
            if 'snippet' in seg_data and 'runs' in seg_data['snippet']:
                for run in seg_data['snippet']['runs']:
                    if 'text' in run:
                        full_text.append(run['text'])
        
        # Join all text
        combined_text = ' '.join(full_text)
        
        # Split by speaker pattern (>> NAME:)
        speaker_pattern = r'>>\s*([A-Z][A-Z\s]+):\s*'
        
        # Write to markdown file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# YouTube Transcript\n\n")
            
            # Split text by speakers
            parts = re.split(speaker_pattern, combined_text)
            
            # First part (before any speaker)
            if parts[0].strip():
                f.write(parts[0].strip() + "\n\n")
            
            # Process speaker sections
            for i in range(1, len(parts), 2):
                if i < len(parts):
                    speaker_name = parts[i].strip()
                    
                    # Write speaker's content on same line as name
                    if i + 1 < len(parts):
                        content = parts[i + 1].strip()
                        if content:
                            # Replace multiple spaces with single space and keep as one paragraph
                            content = re.sub(r'\s+', ' ', content)
                            f.write(f"**{speaker_name}:** {content}\n\n")  # Speaker and content on same line
        
        print(f"Successfully extracted transcript from {json_file} to {output_file}")
        print(f"Processed {len(segments)} segments")
        
    except KeyError as e:
        print(f"Error: Could not find expected data structure in JSON. Missing key: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file '{json_file}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    input_file = "trans.en.json"
    output_file = "transcript.md"
    
    extract_youtube_transcript(input_file, output_file)