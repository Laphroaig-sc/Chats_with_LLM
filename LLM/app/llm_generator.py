import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import gc


def response_by_llm(context,question):
    model_directory='/root/app/model/llm-jp/llm-jp-13b-v2.0'

    tokenizer = AutoTokenizer.from_pretrained(model_directory)
    model = AutoModelForCausalLM.from_pretrained(model_directory, device_map="auto", torch_dtype=torch.bfloat16)

    text = f"以下の文脈を必ず使って、最後にある質問に答えてください。\n{context}\n質問: {question}\n回答:"

    tokenized_input = tokenizer.encode(text, add_special_tokens=False, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(
            tokenized_input,
            max_new_tokens=100,
            do_sample=True,
            top_p=0.95,
            temperature=0.7,
            repetition_penalty=1.05,
        )[0]
    response = tokenizer.decode(output)
    # Remove the question from the response
    response = response.replace(text, '')

    ans=response.strip()

    # gpu operation
    del tokenizer
    del model
    torch.cuda.empty_cache()
    gc.collect()

    return ans


if __name__ == '__main__':
    context='test context'
    question='test message'

    print(response_by_llm(context,question))