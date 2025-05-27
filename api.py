import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = "your-api-key"

def test_openai_api():
    try:
        # Send a test query to OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "What is the capital of France?"}
            ]
        )
        print("Response:", response.choices[0].message.content.strip())
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    test_openai_api()