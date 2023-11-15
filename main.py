# === THESE CODES ARE UNUSED ATM ===

import traceback
import httpx
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

async def store_data():
    base_url = f"https://zuscoffee.com/category/store/melaka"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(base_url)
            if response.status_code == 200:
                data = response.text
                print(data)
                return "a"
            else:
                raise HTTPException(status_code=500, detail="Failed to fetch data from the website")

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="An error occurred while processing the request")

@app.get("/")
async def read_store():
    try:
        data = await store_data()
        # parsed_data = json.loads(data)
        # pretty_json = json.dumps(parsed_data, indent=2)
        # with open("output.json", "w") as json_file:
        #   json.dump(parsed_data, json_file, indent=2)
        # return JSONResponse(content=pretty_json)
        return {"data": data}
    except HTTPException as e:
        raise e

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
