# https://docs.ollama.com/openai

from openai import OpenAI

client = OpenAI(
	base_url = "http://localhost:11434/v1",
	api_key = "some-random-api-key"
)

response = client.chat.completions.create(
	model = "llama3.2",
	messages = [
		{"role": "system", "content": "You are a helpful teacher. Keep the response concise and easy to understand."},
		{"role": "user", "content": "Explain what an AI agent is in simple terms."}
		# {"role": "assistant", "content": "something. this is used to provide example outputs or previous output for context."}
	],
	temperature = 0.7,
	max_tokens = 2000,
	# response_format = {"type": "json_object"},
)

# print("------------------")
# print(response)
# print("------------------")
# print(response.choices)
# print("------------------")
# print(response.choices[0])
# print("------------------")
# print(response.choices[0].message)
print("------------------")
print(response.choices[0].message.content)
print("------------------")
print(response.usage)
print("------------------")
