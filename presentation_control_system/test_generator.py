from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import csv

class TestGenerator:
    def __init__(self):
        self.model_name = "HuggingFaceTB/SmolLM2-1.7B-Instruct"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def generate_chat_response(self, prompt: str, max_new_tokens: int = 500) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(
          **inputs,
          max_new_tokens=max_new_tokens,
          temperature=0.7,
          do_sample=True,
          no_repeat_ngram_size=2,
          pad_token_id=self.tokenizer.eos_token_id
        )
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
        return response[len(prompt):].strip()
