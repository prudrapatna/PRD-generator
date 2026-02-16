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

# Dynamic Prompt based on PRD v7: "The Trust Builder" CUJ
prompt = """
Create a professional, high-resolution User Journey Map for the "Blood Pressure Wellness App" - CUJ: The Trust Builder.

**Target User:** "Data Skeptic" (Mike). He needs to verify the data to trust it.

**Visual Stages (Left to Right):**

1.  **Doubt:** Mike sees an "Elevated Trend" alert on his phone. He looks skeptical. (Icon: Phone with Amber Alert + Question Mark).
2.  **The Test:** He puts on a standard medical blood pressure cuff on his arm to check the real number. (Icon: Arm with BP Cuff).
3.  **Input:** He types the cuff reading (135/85) into the "Calibrate" screen of the app. (Icon: Smartphone with Number Input).
4.  **The Proof:** The app displays a graph. A "Manual" dot appears exactly on top of the "Sensor" trend line. They match perfectly. (Icon: Line Graph with matching point).
5.  **Trust:** A green badge appears: "Trend Verified." Mike feels confident. (Icon: Shield with Checkmark).

**Style Requirements:**
*   **Format:** Horizontal Process Flow.
*   **Aesthetic:** Technical, Clean, "Blueprint" or "Schematic" style to appeal to the skeptic persona. High precision feel.
*   **Colors:** White background. Technical Blue (Grid lines), Amber (Alert), Medical Green (Verified).
*   **Layout:** Icons top, Steps middle, Sentiment curve bottom (Starts Low/Skeptical, ends High/Trusted).
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
    output_file = "product_specs/blood_pressure_cuj_v7_visual.png"
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
