GOOGLE_API_KEY = 'AIzaSyAp2pOQwlCHMKe3VJ0OSzmolLXVeDpPHF4'

import google.generativeai as genai

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(input("What is your query? "))

def embed_watermark(text):
    watermark_pattern = ['\u200B', '\u200C', '\u200D', '\uFEFF']  # Zero-width spaces
    words = text.split()
    watermarked_text = ""
    for i, word in enumerate(words):
        space = watermark_pattern[i % len(watermark_pattern)]
        watermarked_text += word + space + ' '
    return watermarked_text

print(embed_watermark(response.text))
