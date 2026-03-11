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

# Prompt 1: Peace of Mind Onboarding
prompt_1 = """
Create a linear User Journey Map for "Google Health Guardian" - CUJ: "Peace of Mind Onboarding".
Target User: "The Worried Well" (Ages 30-50).

Visual Stages (Left to Right):
1.  **Passive Setup:** User puts on a sleek smartwatch (Pixel Watch/Radiance). No cuff, no setup screen. (Icon: Watch on Wrist).
2.  **The Wait:** A calendar page flipping. 14 days pass. The watch is worn while sleeping. (Icon: Moon & Calendar).
3.  **The Reveal:** A notification "Your Guardian Report is Ready". (Icon: Sparkle Notification).
4.  **The Assurance:** The user looks at the phone app. A green shield icon says "In Range". (Icon: Shield with Checkmark).
5.  **Peace of Mind:** The user smiles, feeling relieved. (Icon: Relaxed Face / Heart).

Style: Clean, minimalist, reassuring, high-tech but human. White background. Teal and Soft Blue palette.
"""

# Prompt 2: The Gentle Nudge
prompt_2 = """
Create a linear User Journey Map for "Google Health Guardian" - CUJ: "The Gentle Nudge".
Target User: "The At-Risk User".

Visual Stages (Left to Right):
1.  **Drift:** A line graph gently trending upward over 30 days. (Icon: Graph w/ Upward Trend).
2.  **The Nudge:** A soft notification (Leaf icon) "Insight available". NOT a red alert. (Icon: Gentle Leaf Notification).
3.  **Understanding:** The app shows the trend correlated with "Low Sleep". (Icon: Sleep Moon overlaid on Graph).
4.  **Action:** The user chooses "Bedtime Wind-down" routine. (Icon: Book/Tea).
5.  **Result:** The graph stabilizes. (Icon: Flat Line Graph).

Style: Soft, non-alarming, supportive. White background. Pastel colors (Sage Green, Soft Blue).
"""

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
success1 = generate_cuj_map(prompt_1, "tidal_cuj_onboarding.png")
time.sleep(2)
success2 = generate_cuj_map(prompt_2, "tidal_cuj_nudge.png")
time.sleep(2)
success3 = generate_cuj_map(prompt_3, "tidal_cuj_doctor.png")

if success1 and success2 and success3:
    print("All Tidal CUJ maps generated.")
else:
    print("Some maps failed.")
