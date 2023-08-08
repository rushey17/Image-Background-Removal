import base64
import logging
from io import BytesIO 
from api_utils import logger
from fastapi import  HTTPException
from PIL import Image


logging.basicConfig(level=logging.INFO)
logging = logging.getLogger(__name__)

def base64_to_pil(input_b64):
    """
    Method to handle base64 bytes to PIL image conversion
    :param payload: base64
    :return: PIL image
    """
    try:
        bytes_img = base64.b64decode(input_b64)   
        file_img= BytesIO(bytes_img)            
        pil_img = Image.open(file_img)   
        logging.info("Base64 to PIL conversion completed successfully.")
        return pil_img
    except Exception as err:
        logging.error("Base64 to PIL conversion got failed.")
        logging.error(err)
        raise HTTPException(status_code=422, detail="Base64 to PIL Img conversion got failed.")
 

def pil_to_base64(bg_removed_pil):
    """
        Method to handle PIL image to base64 bytes conversion
        :param payload: PIL Image
        :return: base64
    """
    try:
        im_file = BytesIO()
        bg_removed_pil.save(im_file, format="PNG")
        im_bytes = im_file.getvalue()     #image in binary format
        im_b64 = base64.b64encode(im_bytes)
        logging.info("PIL Img to Base64 conversion completed successfully.")
        return im_b64
    except Exception as err:
        logging.error("PIL Img to Base64 conversion got failed.")
        logging.error(err)
        raise HTTPException(status_code=422, detail="PIL Img to Base64 conversion got failed.")
    