from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


def setup_model():
    model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer


def generate_response(model, tokenizer, prompt, max_length=512):
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model.generate(
            inputs.input_ids,
            attention_mask=inputs.attention_mask,
            max_length=max_length,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            pad_token_id=tokenizer.pad_token_id,
        )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response


def main():
    try:
        model, tokenizer = setup_model()

        prompt = f"""
                You are an AI assistant that extracts skills from text. 
                Extract a list of skills from the following job description:
                Job Description: {"Looking for a frontend developer, needs to know React, TypeScript, MongoDB, Node.js"}
                Skills: 
                """

        response = generate_response(model, tokenizer, prompt)
        print(response)
    except Exception as e:
        print(f"An error occured: {str(e)}")


if __name__ == "__main__":
    main()
