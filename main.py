import streamlit as st
import requests
from PIL import Image
import numpy as np
from PIL import ImageDraw
import io


st.title("顔認証アプリ")
subscription_key="fa8d9e46e87748fda0a1932dfc6de642"
assert subscription_key
face_api_url='https://20201128tokuno.cognitiveservices.azure.com/face/v1.0/detect'


uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    img=Image.open(uploaded_file)

    with io.BytesIO() as output:
        img.save(output, format="JPEG")
        binary_img=output.getvalue()

    headers = {
        "content-Type":"application/octet-stream",
        'Ocp-Apim-Subscription-Key': subscription_key}

    params = {
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
        'returnFaceId': 'true'
    }

    res = requests.post(face_api_url, params=params,
                             headers=headers, data=binary_img)
    result = res.json()
    draw =ImageDraw.Draw(img)
    for rect in result:
     rect =rect["faceRectangle"]
     draw.rectangle([(rect["left"],rect["top"]), (rect["left"]+rect["width"],rect["top"]+rect["height"])],fill=None,outline="green",width=5 )
    st.image(img , caption="Uploaded Image.", use_colums_width= True)
