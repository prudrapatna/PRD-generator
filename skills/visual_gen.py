import os
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

# Prompt for the "No Calibration" CUJ Visual (v9)
prompt = """
Create a linear user journey map for a "No-Calibration Blood Pressure Wellness" feature on a smartwatch.

**Steps to Visualize:**
1.  **Glance:** A user (Sarah) looks at her smartwatch. The watch face shows a subtle "Amber" ring indicator next to a small heart icon. (Sentiment: Curious/Alert).
2.  **Tap:** She taps the amber ring. A screen opens showing a "Wellness Range" meter. Her current dot is slightly to the right (Elevated), connected by a dotted line to a "Moon" icon (Sleep).
3.  **Insight:** The screen displays text: "3 Nights < 6h Sleep -> Trending Out of Range." (Sentiment: Understanding).
4.  **Action:** She taps a button "Set Sleep Goal."
5.  **Result:** A confirmation screen shows a "Green" checkmark and "Bedtime set for 10:30 PM." (Sentiment: Empowered/Relieved).

**Style:**
*   **Aesthetic:** Clean, minimalist, modern tech/health UI. White background.
*   **Colors:** Use Google-style colors: Soft Green (`#34A853`) for success, Amber (`#FBBC04`) for the alert, and Grey (`#F1F3F4`) for structure. NO RED.
*   **Icons:** Simple, outlined icons (Heart, Moon, Checkmark).
*   **Layout:** Horizontal flow with arrows connecting the screens. Below the screens, show a "Sentiment Wave" curve moving from "Neutral" to "Concern" to "Relief."

**Output:** A high-resolution, professional diagram suitable for a product presentation.
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
    # You can change this filename to match your specific need
    output_file = "product_specs/prds/cujs/blood_pressure_cuj_v9_visual.png"
    
    # Check if image data is available in the response
    # Nano Banana (Gemini 3 Pro) returns images in response.parts
    if response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                # Ensure directory exists
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                
                with open(output_file, "wb") as f:
                    f.write(part.inline_data.data)
                print(f"Diagram saved to {output_file}")
                break
        else:
            print("No image found in response parts.")
    else:
        print("No candidates returned.")

except Exception as e:
    print(f"Error generating image: {e}")
