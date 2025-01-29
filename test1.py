from google.cloud import translate_v3
from google.cloud import vision

# Replace with the path to your service account key file
credentials_path = 'billing-project-449315-ac67f1bcc38e.json'
project_id = "billing-project-449315"
#


# Initialize the Translate client
translate_client = translate_v3.TranslationServiceClient.from_service_account_file(credentials_path)

# Initialize the Vision client
vision_client = vision.ImageAnnotatorClient.from_service_account_file(credentials_path)

# Define the parent resource for Translation API
parent = f"projects/{project_id}/locations/us-central1"

# Specify the path to your image file
image_path = 'arabic_image.jpg'

# Read the image file as bytes
with open(image_path, 'rb') as image_file:
    image_content = image_file.read()

# Use Vision API to detect text in the image
image = vision.Image(content=image_content)
response = vision_client.text_detection(image=image)
texts = response.text_annotations

# Extract the detected text
detected_text = texts[0].description

# Set source and target languages
source_language_code = "ar"  # Assuming the image text is in Arabic
target_language_code = "en"

# Create the TranslateTextRequest object
request = translate_v3.TranslateTextRequest(
    parent=parent,
    contents=[detected_text],
    source_language_code=source_language_code,
    target_language_code=target_language_code,
)

# Make the API call
response = translate_client.translate_text(request=request)

# Extract the translated text
translated_text = response.translations[0].translated_text

print(f"Translated text: {translated_text}")