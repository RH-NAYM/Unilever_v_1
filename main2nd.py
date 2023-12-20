import json
import pandas as pd
from PIL import Image
from aiohttp import ClientSession
from io import BytesIO
from Data.ublData2nd import *
import asyncio
from concurrent.futures import ThreadPoolExecutor


mainDetectionData = {}
fc = {}
fw = {}
hc = {}
ns = {}
ds = {}
qpds = {}
sos = {}


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



async def startDetection(model, url):
    async with ClientSession() as session:
        image = await getImageData(url, session)
        detect_items = await objectDetection(model, image)
        detect_st = await objectDetection(qpdsModel,image)
        for sku,count in detect_st.items():
            add = {sku:count}
            detect_items.update(add)
        return detect_items
    

async def slpitFC(singleDataFromMainData,detectedAllData):
    if singleDataFromMainData in psFC and singleDataFromMainData in mainDetectionData:
        item = {singleDataFromMainData:mainDetectionData[singleDataFromMainData]+detectedAllData[singleDataFromMainData]}
    elif singleDataFromMainData in psFC and singleDataFromMainData not in mainDetectionData:
        item = {singleDataFromMainData:detectedAllData[singleDataFromMainData]}
    fc.update(item)

async def slpitFW(singleDataFromMainData,detectedAllData):
    if singleDataFromMainData in psFW:
        item = {singleDataFromMainData:detectedAllData[singleDataFromMainData]}
        fw.update(item)

async def slpitHC(singleDataFromMainData,detectedAllData):
    if singleDataFromMainData in psHC:
        item = {singleDataFromMainData:detectedAllData[singleDataFromMainData]}
        hc.update(item)

async def slpitNS(singleDataFromMainData,detectedAllData):
    if singleDataFromMainData in nsNT:
        item = {singleDataFromMainData:detectedAllData[singleDataFromMainData]}
        ns.update(item)

async def slpitDS(singleDataFromMainData,detectedAllData):
    if singleDataFromMainData in dsOC:
        item = {singleDataFromMainData:detectedAllData[singleDataFromMainData]}
        ds.update(item)

async def slpitsQPDS(singleDataFromMainData,detectedAllData):
    if singleDataFromMainData in qpdsSC:
        item = {singleDataFromMainData:detectedAllData[singleDataFromMainData]}
        qpds.update(item)


                
async def checkCategories(object):
    # print(object)
    mainDetectionData = {}
    for key,value in object.items():
        print(key)
        print(value)
        if key=="da":
            dataDA = {}
            for item in value:
                data = await startDetection(daModel,item)
                for sku,count in data.items():
                    add = {sku:count}
                    dataDA.update(add)
    processFC_task = [slpitFC(singleDataFromMainData, dataDA) for singleDataFromMainData in dataDA]
    processFW_task = [slpitFW(singleDataFromMainData, dataDA) for singleDataFromMainData in dataDA]
    processHC_task = [slpitHC(singleDataFromMainData, dataDA) for singleDataFromMainData in dataDA]
    processNS_task = [slpitNS(singleDataFromMainData, dataDA) for singleDataFromMainData in dataDA]
    processDS_task = [slpitDS(singleDataFromMainData, dataDA) for singleDataFromMainData in dataDA]
    processQPDS_task = [slpitsQPDS(singleDataFromMainData, dataDA) for singleDataFromMainData in dataDA]

    await asyncio.gather(*processFC_task,*processFW_task,*processHC_task,*processNS_task,*processDS_task,*processQPDS_task)

    mainDetectionData = {
                            "da": {
                                        "fc":fc,
                                        "fw":fw,
                                        "hc":hc,
                                        "ns":ns,
                                        "ds":ds
                                    },
                            "qpds": 
    }



    


    return mainDetectionData
  

