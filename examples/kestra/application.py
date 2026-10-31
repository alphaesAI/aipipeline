import os
from fastapi import FastAPI, UploadFile, Request, HTTPException
from filenest import AsyncFileNest
from filenest.namespaces.webhooks import verify_webhook_signature
from dotenv import load_dotenv

load_dotenv()
 
app = FastAPI()
fn = AsyncFileNest(
    api_key=os.getenv("FILENEST_API_KEY"),
    project_id=os.getenv("FILENEST_PROJECT_ID"),
) 
 
@app.post("/upload")
async def upload(file: UploadFile, user_id: str):
    folder = await fn.folders.ensure_path(f"users/{user_id}/uploads")
    result = await fn.files.upload(
        filename=file.filename,
        data=await file.read(),
        mime_type=file.content_type,
        folder_id=folder["id"],
    )
    return {"file_id": result.id, "status": result.status}
 
 
@app.post("/webhooks/filenest")
async def webhook(request: Request):
    body = await request.body()
    sig = request.headers.get("x-filenest-signature", "")
    if not verify_webhook_signature(body, sig, secret="..."):
        raise HTTPException(status_code=401, detail="Invalid signature")
    event = await request.json()
    print(event["type"], event["data"])
    return {"ok": True}