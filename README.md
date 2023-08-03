I modified the script slightly to process multiple images in an input folder and save them to an out folder.
![image](https://github.com/toyxyz/AdverseCleaner/assets/8006000/a948e71d-b7a0-4dbc-a0b2-9c2703d70b3a)

---------------------------------------------------------------------------------
# AdverseCleaner

The shortest ever code (**16 lines of Python codes**) to remove some [adversarial noise](https://arxiv.org/abs/1412.6572) from images.

It does not even use deep learning.

And I personally think anisotropic filtering methods are more effective than training noise-removal neural networks because convolution operations are essentially non-anisotropic. 

In frequency domain, anisotropic methods are usually more “killing”.

No GPU is needed. Each 1024px image only need less than 3 seconds on my laptop CPU.

# Update

2023/03/28 – Seems that using guided filter is not safe enough because the guidance already has adversarial noise in it; the guided filter may bring the adversarial noise back. Perhaps a ‘safer’ idea is to use some other things to process the initial anisotropic filtered image. I will try some random ideas when I have free time but it seems that I do not have so much free time recently.

# Run

    conda env create -f environment.yaml
    conda activate advc
    python clean.py

Feel free to take a look at the code to change input images.

# Result

The test image is from [here](https://twitter.com/aifurryart/status/1636208457715187714).

Input (with adversarial noise):

![p](input.png)

Output (removing adversarial noise, 2.13 seconds on my laptop CPU):

![p](output.png)

# Implementations

Thank the community for making more implementations!

[HuggingFace Space](https://huggingface.co/spaces/p1atdev/AdverseCleaner)

[Automatic1111's Webui Plugin (with Script)](https://github.com/gogodr/AdverseCleanerExtension)

[Automatic1111's Webui Plugin (with Tab)](https://github.com/p1atdev/stable-diffusion-webui-adverse-cleaner-tab)
