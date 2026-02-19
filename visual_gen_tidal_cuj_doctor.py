import os
import time
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    # Fallback to GOOGLE_API_KEY if GEMINI_API_KEY is not set
    api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Warning: GEMINI_API_KEY or GOOGLE_API_KEY not found in .env file.")

client = genai.Client(api_key=api_key)

# Configuration for Image Generation
image_gen_config = types.GenerateContentConfig(
    image_config=types.ImageConfig(
        aspect_ratio="16:9",
        image_size="2K"
    )
)

# Function to generate and save image
def generate_cuj_map(prompt, filename):
    try:
        print(f"Generating diagram for: {filename}...")
        response = client.models.generate_content(
            model='gemini-3-pro-image-preview',
            contents=prompt,
            config=image_gen_config
        )

        # Save the image
        output_path = f"product_specs/{filename}"
        if response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
            for part in response.candidates[0].content.parts:
                if part.inline_data:
                    with open(output_path, "wb") as f:
                        f.write(part.inline_data.data)
                    print(f"Diagram saved to {output_path}")
                    return True
            print(f"No image found in response for {filename}.")
        else:
            print(f"No candidates returned for {filename}.")
            
    except Exception as e:
        print(f"Error generating {filename}: {e}")
    return False

# Prompt 3: The Doctor Connection
prompt_3 = """
Create a linear User Journey Map for "Google Health Guardian" - CUJ: "The Doctor Connection".
Target User: "The Patient".

Visual Stages (Left to Right):
1.  **Preparation:** User taps "Export Report" in the app. (Icon: Export Arrow).
2.  **The Report:** A professional PDF generates, showing clear blood pressure trends. (Icon: PDF Document).
3.  **The Visit:** User hands the report (or phone) to a Doctor in a white coat. (Icon: Doctor & Patient).
4.  **Validation:** The Doctor nods, pointing at the clear data. (Icon: Thumbs Up / Stethoscope).
5.  **Trust:** The user and doctor shake hands (or smile). (Icon: Handshake).

Style: Professional, credible, clear. White background. Medical Blue and White.
"""

# Execution
success3 = generate_cuj_map(prompt_3, "tidal_cuj_doctor.png")

if success3:
    print("Doctor CUJ map generated.")
else:
    print("Doctor CUJ map failed.")
