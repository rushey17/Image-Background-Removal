from pydantic import BaseModel, validator
from urllib.request import urlopen
# import logger.logger_utils as log
from api_utils import logger
import logging
import base64


logging.basicConfig(level=logging.INFO)
logging = logging.getLogger(__name__)



class ImageBackgroundRemoval(BaseModel):
    image: str


    """Method for Validating Empty Input """
    @validator('image')  
    def validate_length(cls, image):
        if len(image) == 0:
            logger.logging.error("Input string should not be empty")
            raise ValueError('Input string should not be empty')
        return image


    """Method for Validating Input either Valid Image URL or Valid Base64 Bytes"""
    @validator('image')
    def validate_input(cls,image):
        if validate_url(image) or validate_bytes(image) == True:
            return image
        else:
            logging.error("Invalid Image Input")
            raise ValueError("Invalid Image Input")

""" Method for handling  valid Base64 check"""
def validate_bytes(image):
    if isinstance(image, str):    
        image = bytes(image, 'ascii')
    try:
        if base64.b64encode(base64.b64decode(image)) == image:
            return True 
    except Exception as e:
        logging.error("e")
        return False

""" Method for handling valid Image URL check"""
def validate_url(image_url):
    
    if "http" in image_url:
        try:
            site = urlopen(image_url)
            meta = site.info() 
            content_type = meta['content-type'].split('/')[0]
            if content_type == 'image':
                return True
            
        except Exception as err:
            logging.error(err)
            return False


