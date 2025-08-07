#!/usr/bin/env python3

import json
import sys

def extract_youtube_transcript(json_file, output_file):
    """Extract YouTube transcript from JSON to markdown format with **time**: content structure"""
    
    try:
        # Read JSON file
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Navigate to transcript segments
        segments = data['actions'][0]['updateEngagementPanelAction']['content']['transcriptRenderer']['content']['transcriptSearchPanelRenderer']['body']['transcriptSegmentListRenderer']['initialSegments']
        
        # Write to markdown file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# YouTube Transcript\n\n")
            
            for segment in segments:
                seg_data = segment['transcriptSegmentRenderer']
                
                # Extract time and text
                time = seg_data.get('startTimeText', {}).get('simpleText', 'Unknown')
                
                # Get text from snippet runs
                text_parts = []
                if 'snippet' in seg_data and 'runs' in seg_data['snippet']:
                    for run in seg_data['snippet']['runs']:
                        if 'text' in run:
                            text_parts.append(run['text'])
                
                text = ' '.join(text_parts) if text_parts else 'No text'
                
                # Write in markdown format
                f.write(f"**{time}**: {text}\n\n")
        
        print(f"Successfully extracted {len(segments)} segments from {json_file} to {output_file}")
        
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