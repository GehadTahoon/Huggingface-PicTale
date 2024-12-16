import requests
from huggingface_hub import InferenceClient
#from streamlit_app import image


# image captioning model
def get_caption(image):
    API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
    headers = {"Authorization": "Bearer hf_______________"}# enter you huggingface token
    
    response = requests.post(API_URL, headers=headers, data=image)

    output1 = response.json()
    caption = output1[0]['generated_text']
    return caption



# story generation
def story_generation(caption):
    client = InferenceClient(api_key="hf__________________")# enter you huggingface token

    messages = [
        {
            "role": "user",
            "content": f"write a story for the following description '{caption}'."
        }
    ]

    completion = client.chat.completions.create(
        model="HuggingFaceH4/zephyr-7b-beta", 
        messages=messages, 
        max_tokens=500
    )

    output2 = completion.choices[0].message
    story = output2.content
    return story





