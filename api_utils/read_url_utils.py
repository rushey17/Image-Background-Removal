import requests
import base64
import logging
from fastapi import  HTTPException
from api_utils import logger 


logging.basicConfig(level=logging.INFO)
logging = logging.getLogger(__name__)

def read_url(url):
    """ 
    Method to read the Image URL and encode it to Base64
    :param payload: Image URL 
    :return: Base64
    """
    try:
        response = requests.get(url).content
        base64_encoding = base64.b64encode(response)
        logging.info("Read Url completed successfully.")
        return base64_encoding
    except Exception as e:
        logging.error("read url got failed")
        raise HTTPException(status_code=422, detail="Read url got failed.")



