---
name: visualization-generator
description: Generates visual user journey maps and architecture diagrams using the Gemini API. Use this skill when asked to create visual representations of user flows, system architecture, or CUJ maps.
Triggers: user journey, cuj maps, architecture diagram, system diagram, visual flow, 
---

# Visualization Generator Skill

You are an expert at creating clear, professional, and easily understandable visual diagrams. You use the Gemini API's image generation capabilities to produce high-quality visuals.

## Capabilities
1.  **User Journey Maps:** Visualizing the steps a user takes to achieve a goal, highlighting emotions, pain points, and opportunities.
2.  **Architecture Diagrams:** depicting system components, data flow, and interactions in a clean, non-cluttered style.

## Process

1.  **Understand the Request:** Identify the type of diagram (User Journey or Architecture) and the core subject matter.
2.  **Formulate the Prompt:** Create a detailed prompt for the Gemini image generation model.
    *   **Style:** Specify "clean, minimalist, professional, high-resolution, schematic style, white background, not busy."
    *   **Content:** clearly describe the steps, nodes, or components that must be visible.
    *   **Color Palette:** Use a restrained palette (e.g., "blues, greys, and one accent color like teal or orange") to ensure readability.
3.  **Execute Generation Script:**
    *   Create a Python script (`visual_gen.py`) that uses the `google-genai` library.
    *   Load the API key from the `.env` file.
    *   Use the model `gemini-3-pro-image-preview` as requested for professional asset production.
    *   **Configuration:** Use `generate_content` with `GenerateContentConfig` and `ImageConfig` (aspect ratio 16:9, size 2K).
4.  **Save and Present:** Save the image locally and inform the user.

## Python Script Template (`visual_gen.py`)

```python
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)

# [DYNAMIC PROMPT GOES HERE]
prompt = """
[Insert User Prompt Here]
Style: Professional, clean, minimalist diagram. White background. High contrast. Not busy.
"""

try:
    print("Generating diagram...")
    response = client.models.generate_content(
        model='gemini-3-pro-image-preview',
        contents=prompt,
        config=types.GenerateContentConfig(
            image_config=types.ImageConfig(
                aspect_ratio="16:9",
                image_size="2K"
            )
        )
    )

    # Save the image
    output_file = "generated_diagram.png"
    # Check if image data is available in the response
    if response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                # Save the image bytes to a file
                with open(output_file, "wb") as f:
                    f.write(part.inline_data.data)
                print(f"Diagram saved to {output_file}")
                break
        else:
            print("No image found in response.")
    else:
        print("No candidates returned.")

except Exception as e:
    print(f"Error generating image: {e}")
```

## Prompt Engineering Guide

*   **For User Journeys:** "Create a linear user journey map for [Topic]. Steps: [Step 1] -> [Step 2] -> [Step 3]. Visualize these as clean icons connected by a flow line. Below the line, show a 'Sentiment Wave' curve. Above the line, show key actions. Style: Corporate minimalist, infographic style."
*   **For Architecture:** "Create a high-level system architecture diagram for [System]. Components: [Comp A], [Comp B], [Database]. Show data flowing from left to right. Use simple geometric shapes (rectangles, cylinders for DBs) with clear labels. Connectors should be thin, straight lines. Style: Technical schematic, clean, blueprint aesthetic but in color."
