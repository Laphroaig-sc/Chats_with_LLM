import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

save_directory = 'model/'

# loading
tokenizer = AutoTokenizer.from_pretrained("llm-jp/llm-jp-13b-v2.0")
model = AutoModelForCausalLM.from_pretrained("llm-jp/llm-jp-13b-v2.0", device_map="auto", torch_dtype=torch.bfloat16)

# saving
model.save_pretrained(save_directory)
tokenizer.save_pretrained(save_directory)