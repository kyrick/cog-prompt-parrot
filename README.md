# COG Prompt Parrot

<p align="center">
  <img width="384" height="256" src="parrot2.png">
</p>

[Run Prompt Parrot on Replicate!](https://replicate.com/kyrick/prompt-parrot)

This is the official "fork" of the [Prompt Parrot Colab](https://colab.research.google.com/drive/1GtyVgVCwnDfRvfsHbeU0AlG-SgQn1p8e?usp=sharing) for Replicate. But you can also run it locally!

To run: 
1. create a python virtualenv
1. `pip install cog`
1. create folder `models/` and download into it `config.json` and `pytorch_model.bin` from gdrive:  
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