import json
import pandas as pd
from PIL import Image
from aiohttp import ClientSession
from io import BytesIO
from Data.ublData2nd import *
import asyncio
from concurrent.futures import ThreadPoolExecutor


body = {}

async def getImageData(img_url, session):
    async with session.get(img_url) as response:
        img_data = await response.read()
        return BytesIO(img_data)


async def objectDetection(model,img_content):
    img = Image.open(img_content)

    result = model(img)
    detection = {}
    data = json.loads(result[0].tojson())

    if len(data) == 0:
        res = {"AI":"no detection"}
        detection.update(res)
    else:
    
        df = pd.DataFrame(data)
    
        name_counts = df['name'].value_counts().sort_index()
        for name, count in name_counts.items():
            res = {name: count}
            detection.update(res)
    return detection


# old
# async def startDetection(model, url):
#     async with ClientSession() as session:
#         image = await getImageData(url, session)
#         detec = await objectDetection(model, image)
#         return detec


async def startDetection(model, url):
    async with ClientSession() as session:
        image = await getImageData(url, session)
        detect_items = await objectDetection(model, image)
        detect_st = await objectDetection(qpdsModel,image)
        for sku,count in detect_st.items():
            add = {sku:count}
            detect_items.update(add)
        return detect_items

# def loop_over_object(object):
#     for key,value in object.items():
#         if isinstance(value, dict):
#             loop_over_object(value)
#         elif isinstance(value, list):
#             for items in value:
#                 it = {key:items}
#                 body.update(it)
#     return body
                
async def checkCategories(object):
    mainDetectionData = {}
    fc = {}
    fw = {}
    hc= {}
    ns = {}
    ds = {}
    qpds = {}
    sos = {}

    for type,items in object.items():
        if type == "fc":
            for item in items:
                detectedData = await startDetection(daModel,item)
                for sku, count in detectedData.items():
                    if sku in psFC and sku not in fc:
                        singleData = 
                    elif sku
                        
