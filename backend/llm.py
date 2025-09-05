import openai
openai.api_key = 'YOUR_API_KEY'
def get_llm_answer(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content":prompt}]
    )
    return response.choices.message.content
