from fastapi import FastAPI
from escpos.printer import Usb
from fastapi import HTTPException, APIRouter
from config.log_config import logger

cash_draw_router = APIRouter()

printer = Usb(0x04b8, 0x0202, 0, profile="TM-T88V")

@cash_draw_router.post("/open_cash_drawer")
async def open_cash_drawer():
    try:
        printer.cashdraw(2)
        return {"message": "Cash drawer opened successfully."}
    except Exception as e:
        logger.error(f"Error opening cash drawer: {e}")
        raise HTTPException(status_code=500, detail="Error opening cash drawer")
