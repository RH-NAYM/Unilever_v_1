import json
import pandas as pd
from PIL import Image
from aiohttp import ClientSession
from io import BytesIO
from Data.ublData import *
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
    for categories,details in object.items():
        if categories=="da":
            for subCategories,items in details.items():
                if subCategories=="ps":
                    glCRM = {}
                    pondsCRM = {}
                    glFW = {}
                    pondsFW = {}
                    sunsilk = {}
                    clear = {}
                    tresemme = {}
                    dove = {}
                    doveCond = {}

                    for item in items:
                        detectdata = await startDetection(daModel,item)
                        if len(detectdata)==0:
                            perfectStore = {"da_ps": "no perfect store item detected"}
                        else:
                            for sku,count in detectdata.items():
                                if sku in psSkinCare_cream_GL:
                                    if sku in glCRM:
                                        glCRM[sku]=glCRM[sku]+count
                                    else:
                                        result = {sku:count}
                                        glCRM.update(result)
                                elif sku in psSkinCare_cream_ponds:
                                    if sku in pondsCRM:
                                        pondsCRM[sku]=pondsCRM[sku]+count
                                    else:
                                        result = {sku:count}
                                        pondsCRM.update(result)
                                elif sku in psSkinCare_face_wash_GL:
                                    if sku in glFW:
                                        glFW[sku]=glFW[sku]+count
                                    else:
                                        result = {sku:count}
                                        glFW.update(result)
                                elif sku in psSkinCare_face_wash_ponds:
                                    if sku in pondsFW:
                                        pondsFW[sku]=pondsFW[sku]+count
                                    else:
                                        result = {sku:count}
                                        pondsFW.update(result)
                                elif sku in psHairCare_shampoo_sunsilk:
                                    if sku in sunsilk:
                                        sunsilk[sku]=sunsilk[sku]+count
                                    else:
                                        result = {sku:count}
                                        sunsilk.update(result)
                                elif sku in psHairCare_shampoo_clear:
                                    if sku in clear:
                                        clear[sku]=clear[sku]+count
                                    else:
                                        result = {sku:count}
                                        clear.update(result)
                                elif sku in psHairCare_shampoo_tresemme:
                                    if sku in tresemme:
                                        tresemme[sku]=tresemme[sku]+count
                                    else:
                                        result = {sku:count}
                                        tresemme.update(result)
                                elif sku in psHairCare_shampoo_dove:
                                    if sku in dove:
                                        dove[sku]=dove[sku]+count
                                    else:
                                        result = {sku:count}
                                        dove.update(result)
                                elif sku in psHairCare_conditioner_dove:
                                    if sku in doveCond:
                                        doveCond[sku]=doveCond[sku]+count
                                    else:
                                        result = {sku:count}
                                        doveCond.update(result)
                                else:
                                    continue

                        
                            if len(glCRM) == 0 and len(pondsCRM)==0 and len(glFW)==0 and len(pondsFW)==0 and len(sunsilk)==0 and len(clear)==0 and len(tresemme)==0 and len(dove)==0 and len(doveCond)==0:
                                perfectStore = {"da_ps": "no perfect store item detected"}
                            else:
                                perfectStore = {
                                                    "perfect_store":{
                                                                        "skin_care":{
                                                                                        "cream":{
                                                                                                    "glow_and_lovely":glCRM,
                                                                                                    "ponds":pondsCRM
                                                                                                },
                                                                                        "face_wash":{
                                                                                                        "glow_and_lovely":glFW,
                                                                                                        "ponds":pondsFW
                                                                                                    },
                                                                        "hair_care":{
                                                                                        "shampoo":{
                                                                                                    "sunsilk":sunsilk,
                                                                                                    "clear":clear,
                                                                                                    "tresemme":tresemme,
                                                                                                    "dove":dove
                                                                                                    },
                                                                                        "conditioner":doveCond
                                                                                    }
                                                                                    }
                                                                        }
                                                    }
                        mainDetectionData.update(perfectStore)

                elif subCategories=="ns":
                    boost = {}
                    horlicks = {}
                    maltova = {}
                    for item in items:
                        detectdata = await startDetection(daModel,item)
                        if len(detectdata)==0:
                            nutritionStore = {"da_ns":"no nutrition store item detected"}
                            
                        else:
                            for sku,count in detectdata.items():
                                if sku in nsBoost:
                                    if sku in boost:
                                        boost[sku]=boost[sku]+count
                                    else:
                                        result = {sku:count}
                                        boost.update(result)
                                elif sku in nsHorlicks:
                                    if sku in horlicks:
                                        horlicks[sku]=horlicks[sku]+count
                                    else:
                                        result = {sku:count}
                                        horlicks.update(result)
                                elif sku in nsMaltova:
                                    if sku in maltova:
                                        maltova[sku]=maltova[sku]+count
                                    else:
                                        result = {sku:count}
                                        maltova.update(result)
                                else:
                                    continue
                            if len(boost)==0 and len(horlicks)==0 and len(maltova)==0:
                                nutritionStore = {"da_ns":"no nutrition store item detected"}
                            else:
                                nutritionStore = {
                                                    "nutrition_store":{
                                                                        "nutrition":{
                                                                                        "boost":boost,
                                                                                        "horlicks":horlicks,
                                                                                        "maltova":maltova
                                                                                        }
                                                                        }
                                                    }
                        mainDetectionData.update(nutritionStore)

                elif subCategories=="ds":
                    pepsodent = {}
                    for item in items:
                        detectdata = await startDetection(daModel,item)
                        if len(detectdata)==0:
                            drugStore = {"da_ds":"no drug store item detected"}
                            
                        else:
                            for sku,count in detectdata.items():
                                if sku in dsPepsodent:
                                    if sku in pepsodent:
                                        pepsodent[sku]=pepsodent[sku]+count
                                    else:
                                        result = {sku:count}
                                        pepsodent.update(result)
                                else:
                                    continue
                            if len(pepsodent)==0:
                                drugStore = {"da_ds":"no drug store item detected"}
                            else:
                                drugStore = {
                                                "drug_store":{
                                                                "oral_care":pepsodent
                                                                }
                                                }
                        mainDetectionData.update(drugStore)
        elif categories=="qpds":
            vaseline = {}
            doveQPDS = {}
            for item in details:
                detectdata = await startDetection(qpdsModel,item)
                if len(detectdata)==0:
                    qpdsStore = {"qpds":"no qpds item detected"}
                else:
                    for sku,count in detectdata.items():
                        if sku in qpdsSkinCare_vaseline:
                            if sku in vaseline:
                                vaseline[sku]=vaseline[sku]+count
                            else:
                                result = {sku:count}
                                vaseline.update(result)
                        elif sku in qpdsSkinCare_dove:
                            if sku in doveQPDS:
                                doveQPDS[sku]=doveQPDS[sku]+count
                            else:
                                result = {sku:count}
                                doveQPDS.update(result)                                
                        else:
                            continue
                    

                    if len(vaseline)==0 and len(doveQPDS)==0:
                        qpdsStore = {"qpds":"no qpds item detected"}
                    else:
                    
                        qpdsStore = {
                                        "qpds":{
                                                    "skin_care":{
                                                                    "vaseline":vaseline,
                                                                    "dove":doveQPDS
                                                                    }
                                                    }
                                        }
            mainDetectionData.update(qpdsStore)

        elif categories=="sos":
            soap = {}
            fw = {}
            milk = {}
            paste = {}
            cleaning = {}
            for item in details:
                detectdata = await startDetection(sosModel,item)
                if len(detectdata)==0:
                    sosStore = {"sos":"no sos item detected"}
    
                else:
                    for sku,count in detectdata.items():
                        if sku in comSkinCleansing_soap:
                            if sku in soap:
                                soap[sku]=soap[sku]+count
                            else:
                                result = {sku:count}
                                soap.update(result)
                        elif sku in comSkinCare_faceWash:
                            if sku in fw:
                                fw[sku]=fw[sku]+count
                            else:
                                result = {sku:count}
                                fw.update(result)
                        elif sku in comNutrition_milk:
                            if sku in milk:
                                milk[sku]=milk[sku]+count
                            else:
                                result = {sku:count}
                                milk.update(result)                          
                        elif sku in comOralCare_paste:
                            if sku in paste:
                                paste[sku]=paste[sku]+count
                            else:
                                result = {sku:count}
                                paste.update(result)
                        elif sku in comHomeHyg_clean:
                            if sku in cleaning:
                                cleaning[sku]=cleaning[sku]+count
                            else:
                                result = {sku:count}
                                cleaning.update(result)
                        else:
                            continue
                    if len(soap)==0 and len(fw)==0 and len(milk)==0 and len(paste)==0 and len(cleaning)==0:
                        sosStore = {"sos":"no sos item detected"}
                    else:
                    
                        sosStore = {
                                        "sos":{
                                                    "skin_cleansing":{
                                                                        "soap":soap
                                                                        },
                                                    "skin_care":{
                                                                    "face_wash":fw
                                                                    },
                                                    "nutrition":{
                                                                    "milk":milk
                                                                    },
                                                    "oral_care":{
                                                                    "paste":paste
                                                                    },
                                                    "home_and_hygiene":{
                                                                            "cleaning":cleaning
                                                                            }

                                                    }
                                        }
                mainDetectionData.update(sosStore)
    return mainDetectionData

