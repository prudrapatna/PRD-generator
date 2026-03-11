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

# Prompt 1: The Unified View
prompt_unified = """
Create a professional User Journey Map for the "Google Health App 2026" - CUJ: "The Unified View".

**Target User:** "The Seeker" (Data Fragmented). Needs to see all data in one place.

**Visual Stages (Left to Right):**
1.  **Fragmentation:** User holds phone with multiple app icons (Oura, Peloton, Apple Health) floating around confusingly. (Icon: Scattered Puzzle Pieces).
2.  **Connection:** User taps "Connect" in Google Health. A beam of light connects the external icons to the Google G. (Icon: Link/Chain).
3.  **Ingestion:** The "Data Fabric" processes the data. (Icon: Abstract Cloud with Gear/Processing nodes).
4.  **Unification:** The Dashboard appears. It shows a single "Sleep Score" that combines Oura + Pixel Watch data seamlessly. (Icon: Unified Dashboard UI).
5.  **Clarity:** User smiles, looking at a clean summary. A "Saved Time" badge appears. (Icon: Clock with Checkmark).

**Style Requirements:**
*   **Format:** Linear Journey Map with Sentiment Wave below.
*   **Aesthetic:** Clean, Modern Tech, "Google Material Design" influence but schematic.
*   **Colors:** White background. Google Blue, Teal, Soft Grey. High contrast for readability.
"""

# Prompt 2: The Proactive Nudge
prompt_nudge = """
Create a professional User Journey Map for the "Google Health App 2026" - CUJ: "The Proactive Nudge".

**Target User:** "The Regular" (Needs Motivation). Needs guidance based on how they feel.

**Visual Stages (Left to Right):**
1.  **The Signal:** It is morning. The AI detects low HRV and poor sleep data in the background. (Icon: Moon with Down Arrow).
2.  **The Nudge:** A "Daily Brief" notification appears on the phone lock screen: "Take it easy today." (Icon: Notification Bubble with Sparkles).
3.  **The Adjustment:** User opens the app. The "Workout Plan" automatically changes from "5K Run" to "20 min Yoga". (Icon: UI Transition / Swap).
4.  **The Action:** User rolls out a yoga mat, following the video on the phone. (Icon: Person doing Yoga).
5.  **The Reward:** A "Restored" badge appears. The user feels supported, not guilty. (Icon: Battery Recharging).

**Style Requirements:**
*   **Format:** Linear Journey Map with Sentiment Wave below.
*   **Aesthetic:** Clean, Modern Tech, "Google Material Design" influence but schematic.
*   **Colors:** White background. Google Blue, Teal, Soft Grey. High contrast for readability.
"""

# Execution
success1 = generate_cuj_map(prompt_unified, "google_health_cuj_unified.png")
time.sleep(2) # Pause to respect rate limits
success2 = generate_cuj_map(prompt_nudge, "google_health_cuj_nudge.png")

if success1 and success2:
    print("All CUJ maps generated successfully.")
else:
    print("Some CUJ maps failed to generate.")
