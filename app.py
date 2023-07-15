from fastapi import FastAPI

app = FastAPI()

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/main", response_class=HTMLResponse)
async def get_page_with_image_and_wish_note(request: Request):
    # Retrieve the image and wish note data and pass it to the template
    image_url = "/static/invoice.jpg"
    wish_note = "With Love and Blessings from MIE 16"

    return templates.TemplateResponse(
        "main_web_page.html",
        {"request": request, "image_url": image_url, "wish_note": wish_note},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)