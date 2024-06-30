from openai import AzureOpenAI
from config import *

client = AzureOpenAI(
    azure_endpoint= api_base,
    api_key= api_key,
    api_version= api_version
)


def scan_code_with_chatgpt(code):
    system_content = open("system_prompt.md", "r")
    system_content = system_content.read()

    completion = client.chat.completions.create(
        model="gpt-4o",  # gpt4-large
        messages=[
            {
                "role": "system",
                "content": system_content
            },
            {
                "role": "user",
                "content": f"Please analyze the following code and provide any security vulnerabilities you find:\n\n```{code}\n```",
            },
        ],
    )
    # print(completion.choices[0].message.content)
    return str(completion.choices[0].message.content)

