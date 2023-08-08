from asyncore import read
from api_utils import pil_convertions_utils
from api_utils import background_removal_utils
from api_utils import read_url_utils
from fastapi import  HTTPException
from api_utils import logger
import validators
import logging



logging.basicConfig(level=logging.INFO)
logging = logging.getLogger(__name__)


def check_url(input_image):
    """ 
    Method to check if a given input is URL or Not
    :param payload: Image URL or Base64
    :return: Base64 or False
    """
    valid = validators.url(input_image)
    if valid == True:
        logging.info("Checking url function completed successfully.")
        return read_url_utils.read_url(input_image)
    else:
        return False


def func_handler(input_image):
    """ 
    Method to call all the conversion methods and background removal operation method
    :param payload: Image URL or Image in Base64
    :return: Base64
    """
    try:
        check_url_response = check_url(input_image)
        if check_url_response:
            input_image = check_url_response

        pil_img = pil_convertions_utils.base64_to_pil(input_image)
        bg_removed_pil = background_removal_utils.bg_removal(pil_img)
        encoded_base64 = pil_convertions_utils.pil_to_base64(bg_removed_pil)
        logging.info("func_handler completed successfully.")
        return encoded_base64

    except Exception as err:
        logging.error("func_handler got failed.")
        logging.error(err)
        raise HTTPException(status_code=422, detail="function handler got failed.")
