from fastapi import FastAPI, HTTPException, APIRouter
from PIL import Image
from escpos.printer import Usb
from jinja2 import Environment, FileSystemLoader
import imgkit
from config.log_config import logger
import os
from models.ticket_base_model import Ticket_Base_Model

printer_router = APIRouter()

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')

# Create Jinja2 environment
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template('receipt.html')

image_file = 'receipt.png'

options = {
    'quiet': '',
    'disable-smart-width': '',
    'width': '512'
}

def generate_receipt_and_open_drawer(receipt_data):
    try:
        # Render HTML template with dynamic data
        rendered_html = template.render(receipt_data=receipt_data)

        # Save rendered HTML to a temporary file
        with open('rendered_receipt.html', 'w') as f:
            f.write(rendered_html)

        imgkit.from_file('rendered_receipt.html', image_file, options=options)
        image = Image.open(image_file)
        image.show()

        # Uncomment this part when you want to print the receipt
        # printer = Usb(0x04b8, 0x0202, 0, profile="TM-T88V")
        # with open(image_file, 'rb') as f:
        #     printer.image(Image.open(f))
        #     printer.ln(5)
        #     printer.cut()
        #     printer.cashdraw(2)
    except Exception as e:
        logger.error(f"Error generating receipt and opening cash drawer: {e}")
        raise HTTPException(status_code=500, detail="Error generating receipt and opening cash drawer")


@printer_router.post("/print_ticket")
async def print_ticket(receipt_data: Ticket_Base_Model):
    generate_receipt_and_open_drawer(receipt_data)
    return {"message": "Receipt generated and cash drawer opened successfully."}
