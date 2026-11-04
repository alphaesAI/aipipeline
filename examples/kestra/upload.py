import os
from dotenv import load_dotenv
from filenest import FileNest

load_dotenv()

# Initialize the SDK with environment variables passed as strings
fn = FileNest(
    api_key=os.getenv("FILENEST_API_KEY"),
    project_id=os.getenv("FILENEST_PROJECT_ID"),
    base_url="https://filenest.drgodly.com"
)

# Example: Uploading a file
with open("/home/logidhasan/Documents/filenest_reports/sample_dicom.DCM", "rb") as f:
    file = fn.files.upload(
        data=f,
        filename="sample_dicom.DCM",
        mime_type="application/dicom"a
    )

print("Uploaded file ID:", file.id)