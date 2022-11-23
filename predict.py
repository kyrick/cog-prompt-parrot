import itertools

from cog import BasePredictor, Input
from transformers import AutoModelForCausalLM, AutoTokenizer

start_token = "<BOP>"
pad_token = "<PAD>"
end_token = "<EOP>"

class Predictor(BasePredictor):
    def setup(self):
        """Load the model into memory to make running multiple predictions efficient"""
        self.model = AutoModelForCausalLM.from_pretrained("./model")
        self.tokenizer = AutoTokenizer.from_pretrained(
            "distilgpt2", cache_dir="./model", bos_token=start_token, eos_token=end_token, pad_token=pad_token
        )

    def predict(
        self, prompt: str = Input(description="Input prompt", default="a beautiful painting")
    ) -> str:
        num_prompts_to_generate = 5 
        max_prompt_length = 50
        min_prompt_length = 30
        temperature = 1.0
        top_k = 70
        top_p = 0.9


        if not prompt:
            raise UserWarning("manual_prompt must be at least 1 letter")

        encoded_prompt = self.tokenizer(
            prompt, add_special_tokens=False, return_tensors="pt"
        ).input_ids
        encoded_prompt = encoded_prompt.to(self.model.device)

        output_sequences = self.model.generate(
            input_ids=encoded_prompt,
            max_length=max_prompt_length,
            min_length=min_prompt_length,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            do_sample=True,
            num_return_sequences=num_prompts_to_generate,
            pad_token_id=self.tokenizer.pad_token_id,  # gets rid of warning
        )

        tokenized_start_token = self.tokenizer.encode(start_token)

        generated_prompts = []
        for generated_sequence in output_sequences:
            # precision is a virtue
            tokens = []
            for i, s in enumerate(generated_sequence):
                if s in tokenized_start_token and i != 0:
                    if len(tokens) >= min_prompt_length:
                        break
                tokens.append(s)

            text = self.tokenizer.decode(
                tokens, clean_up_tokenization_spaces=True, skip_special_tokens=True
            )
            text = (
                text.strip().replace("\n", " ").replace("/", ",")
            )  # / remove slash. It causes problems in namings
            # remove repeated adjacent words from `text`. For example: "lamma lamma is cool cool" -> "lamma is cool"
            text = " ".join([k for k, g in itertools.groupby(text.split())])
            generated_prompts.append(text)

        return "\n------------------------------------------\n".join(generated_prompts)


