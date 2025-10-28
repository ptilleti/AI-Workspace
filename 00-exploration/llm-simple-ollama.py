# https://docs.ollama.com/quickstart#python
# https://github.com/ollama/ollama-python
# https://github.com/ollama/ollama/blob/main/docs/api.md

from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(
	model="llama3.2",
	messages=[
		{"role": "system", "content": "You are a helpful teacher."},
		{"role": "user", "content": "Explain what an AI agent is in simple terms."},
		{"role": "assistant", "content": "Keep the response concise and easy to understand."}
	]
	# format="json"
)

# print("------------------")
# print(response)
# print("------------------")
# print(response.message)
print("------------------")
print(response.message.content)
print("------------------")


