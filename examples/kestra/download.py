import os
from dotenv import load_dotenv
from filenest import FileNest

load_dotenv()

fn = FileNest(
    api_key=os.getenv("FILENEST_API_KEY"),
    project_id=os.getenv("FILENEST_PROJECT_ID"),
    base_url="https://filenest.drgodly.com"
)

fn.files.download_to_path("6686e10c-2664-4bca-9102-6271f7c9e592", dest="./downloaded_sample_cardio.pdf")

print(f"File successfully downloaded and saved as downloaded_sample_cardio.pdf")