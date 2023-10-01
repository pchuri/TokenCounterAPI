from fastapi import FastAPI, HTTPException, Query
import tiktoken

app = FastAPI()

@app.get("/count_tokens")
async def count_tokens(model_name: str = Query(...), text: str = Query(...)):
    
    try:
        enc = tiktoken.encoding_for_model(model_name)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid model name")

    tokens = enc.encode(text)
    token_count = len(tokens)

    return {"token_count": token_count}