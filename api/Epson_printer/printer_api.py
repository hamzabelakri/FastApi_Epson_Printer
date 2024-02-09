from fastapi import FastAPI
from PIL import Image
from escpos.printer import Usb
from config.log_config import logger
import imgkit 
from fastapi import HTTPException, APIRouter

printer_router = APIRouter()

html_file = 'receipt.html'
image_file = 'receipt.png'

options = {
    'quiet': '',
    'disable-smart-width': '',
    'width': '512'
}

def generate_receipt_and_open_drawer():
    try:
        imgkit.from_file(html_file, image_file, options=options)
        image = Image.open(image_file)
        image.show()
        printer = Usb(0x04b8, 0x0202, 0, profile="TM-T88V")
        """ with open(image_file, 'rb') as f:
            printer.image(Image.open(f))
            printer.ln(5)
            printer.cut()
            printer.cashdraw(2) """
    except Exception as e:
        logger.error(f"Error generating receipt and opening cash drawer: {e}")
        raise HTTPException(status_code=500, detail="Error generating receipt and opening cash drawer")

@printer_router.post("/print_ticket")
async def print_ticket():
    generate_receipt_and_open_drawer()
    return {"message": "Receipt generated and cash drawer opened successfully."}


