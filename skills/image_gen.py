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

# Define the prompt for the infographic
prompt = """
Create a professional, clean, and modern infographic summarizing user research findings on "Blood Pressure Monitoring Features".

The infographic should visually represent the following key data points:

1.  **User Preference Split:** A clear pie chart or bar showing:
    *   50% prefer "Wellness/Coaching Approach" (Concept A) - Keywords: "Less scary", "Routine", "Soft Nudges"
    *   40% prefer "Medical/Diagnostic Approach" (Concept B) - Keywords: "Accuracy", "FDA Cleared", "Hard Proof"
    *   10% are "Unsure" (Cost/Insurance dependent)

2.  **Key Themes (Represent with icons and brief text):**
    *   **Anxiety & Avoidance:** 40% of users fear diagnosis. Solution: "Soft Nudge UI" (no scary red alerts).
    *   **The "Proof" Divide:** High-knowledge users want transparency (algorithms, raw data); Busy users want simplicity.
    *   **Verification Loop:** 40% of users will "Wait and Re-measure" at home before seeing a doctor.

3.  **Top Motivator:** "Context is King" - Explaining *why* a reading is high (e.g., linked to poor sleep) drives action.

4.  **Recommendations (Checklist style):**
    *   [Must Have] Contextual Alerts
    *   [Must Have] "Soft Nudge" Mode
    *   [Should Have] In-App Cuff Verification Flow

**Style:**
*   Clean, minimalist, corporate but approachable.
*   Color palette: Blues, teals, and soft greys (trustworthy, medical but not alarming). Avoid aggressive reds.
*   High resolution, suitable for a presentation slide.
*   Text should be legible and concise.
"""

try:
    print("Generating infographic...")
    # Use the correct method for generating images with the new SDK
    response = client.models.generate_images(
        model='imagen-3.0-generate-001',
        prompt=prompt,
        config=types.GenerateImagesConfig(
            number_of_images=1,
            aspect_ratio="16:9",
            safety_filter_level="block_only_high",
            person_generation="allow_adult",
        )
    )

    # Save the image
    output_file = "survey_infographic.png"
    if response.generated_images:
        image = response.generated_images[0]
        image.image.save(output_file)
        print(f"Infographic saved to {output_file}")
    else:
        print("No image generated.")

except Exception as e:
    print(f"Error generating image: {e}")
