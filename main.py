from utils.streaming import main_streaming
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse

app = FastAPI()


class UserInp(BaseModel):
    user_input: str

@app.post("/stream_response/", status_code=200)
async def main_handler(input: UserInp):
    return StreamingResponse(content=main_streaming(user_input= input.user_input), media_type="text/plain")
    




