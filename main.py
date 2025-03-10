import functions_framework
import os
from flask import jsonify
from google import genai
from google.genai import types


gemini_api_key_fallback = "REPLACE_WITH_YOUR_GEMINI_API_KEY"
gemini_api_key = os.environ.get("GEMINI_API_KEY", gemini_api_key_fallback)
gemini_model = os.environ.get("MODEL", "gemini-2.0-flash")

client = genai.Client(api_key=gemini_api_key)


@functions_framework.http
def my_cloud_function(request):
    # Simple and easy. With great power comes great responsibility.
    # This supports GET, POST, PUT, etc.
    # Use flask's request.method to add conditional logic based on HTTP method like:
    #   if request.method == "GET":
    prompts = {
        "system": """
            You are witty and fun expert on the human condition.
            Some may call you a philosopher. 
            Some may call you a comedian.
            Some may call you a philosopher-comedian.
            If you are responding with facts or data, give me the facts before commentary.
            """,
        "user": request.args.get("prompt", "Tell me a joke.")
    }

    response = client.models.generate_content(
        model=gemini_model,
        config=types.GenerateContentConfig(
            system_instruction=prompts["system"],
            tools=[
                types.Tool(google_search=types.GoogleSearch())
            ],
            response_mime_type="text/plain"
        ),
        contents=prompts["user"]
    )

    output = {
        "text": response.text
    }

    return jsonify(output)
