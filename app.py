from wsgiref import validate
from fastapi import FastAPI, HTTPException
import logging
from schemas import image_schema as schema
from pydantic import ValidationError
from api_utils import logger
from api_utils import func_handler_utils

logging.basicConfig(level=logging.INFO)
logging = logging.getLogger(__name__)


app = FastAPI()

@app.post('/',response_model=schema.ImageBackgroundRemoval)
def image_background_removal(image: schema.ImageBackgroundRemoval):
    input_image = image.image
    response = func_handler_utils.func_handler(input_image)
    logging.info(f"Endpoint: / completed")
    return {"image":response}


 
 








    