# https://docs.ollama.com/quickstart#python
# https://github.com/ollama/ollama-python
# https://github.com/ollama/ollama/blob/main/docs/api.md

from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(
	model = "llama3.2",
	messages = [
		{"role": "system", "content": "You are a helpful teacher. Keep the response concise and easy to understand."},
		{"role": "user", "content": "Explain what an AI agent is in simple terms."}
		# {"role": "assistant", "content": "something. this is used to provide example outputs or previous output for context."}
	]#,
	#format = "json"
)

# print("------------------")
# print(response)
# print("------------------")
# print(response.message)
print("------------------")
print(response['message']['content'])
print("------------------")
print(f"Total Duration: {response.get('total_duration')}")
print(f"Load Duration: {response.get('load_duration')}")
print(f"Prompt Eval Count: {response.get('prompt_eval_count')}")
print(f"Prompt Eval Duration: {response.get('prompt_eval_duration')}")
print(f"Eval Count: {response.get('eval_count')}")
print(f"Eval Duration: {response.get('eval_duration')}")
print("------------------")

