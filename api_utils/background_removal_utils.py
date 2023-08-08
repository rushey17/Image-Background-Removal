from rembg import remove
import base64
import logging
from api_utils import logger 
from fastapi import  HTTPException


logging.basicConfig(level=logging.INFO)
logging = logging.getLogger(__name__)

def bg_removal(pil_img):
    """ 
    Method to handle Removing background of PIL image using rembg remove function.
    :param payload: PIL Image
    :return: Background Removed PIL Image
    """
    try:
        bg_removed_pil = remove(pil_img) 
        logging.info("Background image removal completed successfully.")
        return bg_removed_pil
    except Exception as err:
        logging.error("Background image removal got failed.")
        logging.error(err)
        raise HTTPException(status_code=422, detail="Background image removal got failed.")

