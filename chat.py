
import openai
from passwords import *

openai.api_key = api_key()


question = input(">>>")

response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

print(response.choices[0].text)

