import aiohttp
import asyncio
import cv2
import numpy as np
     
async def checkImageQuality(image_url, min_resolution=1000, reflection_threshold=150):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as resp:
                resp.raise_for_status()
                image_array = await read_image_async(resp)
                img = await decode_image_async(image_array)
                blur_value = await assess_blur_async(img)
                resolution_check = await assess_resolution_async(img, min_resolution)
                reflection_check = await assess_reflection_async(img, reflection_threshold)

                return {
                    "blur": "Blurry" if blur_value < 100 else "Not blurry",
                    "resolution": resolution_check,
                    "reflection": reflection_check
                }

    except aiohttp.ClientError as e:
        return f"Error: {e}"

async def read_image_async(resp):
    return np.asarray(bytearray(await resp.read()), dtype=np.uint8)

async def decode_image_async(image_array):
    return cv2.imdecode(image_array, cv2.IMREAD_COLOR)

async def assess_blur_async(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()

async def assess_resolution_async(img, min_resolution):
    height, width, _ = img.shape
    if height < min_resolution or width < min_resolution:
        return "Low resolution"
    else:
        return "Sufficient resolution"

async def assess_reflection_async(img, reflection_threshold):
    avg_intensity = np.mean(img)
    
    if avg_intensity > reflection_threshold:
        return "Excessive reflection"
    else:
        return "Acceptable reflection"

async def main():

    image_url = "https://example.com/image.jpg"
    result = await checkImageQuality(image_url)
    print(result)
asyncio.run(main())
