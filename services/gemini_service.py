import os
from google import genai
from flask import session

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_pc_explanation(build, use_case):

    lang = session.get("lang", "en")

    spec_text = f"""
CPU: {build['cpu'].name}
GPU: {build['gpu'].name}
RAM: {build['ram'].size}GB
Total Price: ₹{build['total_price']}
Bottleneck: {build['bottleneck']['type']} ({build['bottleneck']['percentage']}%)
"""

    prompt = f"""
You are a professional PC performance analyst.

Explain in this language: {lang}

Language codes:
en = English
ta = Tamil
hi = Hindi

User Selected Use Case: {use_case}

PC Specifications:
{spec_text}

IMPORTANT:
Explain ONLY in the selected language.
Use the same language consistently.

Structure the output in clean HTML using:
<h2>, <h3>, <ul><li>, <p>

Return only HTML.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "<h3>AI Explanation Unavailable</h3><p>The AI recommendation builder is currently experiencing high traffic (API Quota Exceeded). Please review the specifications listed above.</p>"



def generate_laptop_explanation(laptop, use_case):

    spec_text = f"""
Laptop: {laptop.name}
CPU Score: {laptop.cpu_score}
GPU Score: {laptop.gpu_score}
RAM: {laptop.ram}GB
Price: ₹{laptop.price}
"""

    prompt = f"""
You are a professional laptop performance analyst.

User Selected Use Case: {use_case}

Laptop Specifications:
{spec_text}

IMPORTANT:
Only explain performance for the selected use case: {use_case}.
Do NOT explain other use cases.
Do NOT include sections for other categories.
Do NOT use markdown symbols.

Structure output in clean HTML using:

<h2> for main section title
<h3> for sub sections
<ul><li> for bullet points
<p> for key insights

Keep explanation sharp, technical, structured and visually clean.
Avoid long paragraphs.
Be realistic about laptop thermals and sustained performance.
Return only valid HTML.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "<h3>AI Explanation Unavailable</h3><p>The AI recommendation builder is currently experiencing high traffic (API Quota Exceeded). Please review the specifications listed above.</p>"

