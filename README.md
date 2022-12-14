# COG Prompt Parrot

<p align="center">
  <img width="384" height="256" src="parrot2.png">
</p>

[Run Prompt Parrot on Replicate!](https://replicate.com/kyrick/prompt-parrot)

This is the official "fork" of the [Prompt Parrot Colab](https://colab.research.google.com/drive/1GtyVgVCwnDfRvfsHbeU0AlG-SgQn1p8e?usp=sharing) for Replicate. But you can also run it locally!

# What is Prompt Parrot?

Prompt Parrot takes a text input and generates text2image prompts you can use with Stable Diffusion, Midjourney, etc. To use the parrot, you provide a base prompt and the parrot completes the rest of the prompt. It's a bit like mad libs for text prompts except more orderly (in theroy)! Prompt Parrot is an idea generating tool. It may present you with interesting styles and fantastic combinations!

Example usage: input a base prompt such as "a majestic horse in a field" and see what the Parrot comes up with! 

### What is it?

Prompt Parrot started life as a colab to finetune your own distilgpt2 model on your own prompts and then generate prompts in your style. This version is still online and you can try it out here: [Prompt Parrot Colab](https://colab.research.google.com/drive/1GtyVgVCwnDfRvfsHbeU0AlG-SgQn1p8e?usp=sharing)

Eventually, it became clear that providing many prompts was a barrier to entry. It's difficult to pull together a large amount of prompts. So the hosted model is distilgpt2 fine-tuned on a corpus of 51,747 community provided text prompts. The model uses this training data to geberate prompts for text2image prompt generators.

# Online Runs

[Run Prompt Parrot on Replicate!](https://replicate.com/kyrick/prompt-parrot)

# Local Runs

Steps: 
1. create a python virtualenv
1. `pip install cog`
1. [Download the model from gdrive](https://drive.google.com/drive/folders/1X7PoqEEN8qxV6wvHnHuOWGm7T3Zr2l2w?usp=sharing). 
  1. Download `config.json` and `pytorch_model.bin` into folder `models/`.  
1. in terminal execute: `sudo cog predict -i prompt="a crystal fortress in a field of flowers"`

# Credits
Lead Developer - [Stephen Young](https://linktr.ee/KyrickYoung)

Special thanks to members of the AI art community for providing data train prompt parrot!

# License
The MIT License (MIT)

Copyright 2022 Stephen Young

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
