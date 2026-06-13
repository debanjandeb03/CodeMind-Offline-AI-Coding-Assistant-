from pydantic import BaseModel

class chatRequest(BaseModel):
    prompt:str

class chatResponse(BaseModel):
    response:str