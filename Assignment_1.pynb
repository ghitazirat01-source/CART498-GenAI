import torch
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

from diffusers import DiffusionPipeline
import torch

model_id = "Lykon/dreamshaper-8"

pipe = DiffusionPipeline.from_pretrained(
    model_id,
    dtype=torch.float16
)

pipe = pipe.to("cuda")
prompt = (
    #"flying computer as a god"
    #"goddess Venus behind a desk in an office working"
    "Jesus using a computer"
    "end of the world, hell"
    "God is a computer"
    "crying"
    "Jesus crying"
    #"smiling too much, creepy"
    "Jesus smoking a cigarette, vape, cigar, pipe"
    "cigarettes, vape"
    "a disturbingly wide frozen smile, vacant staring eyes, an unnaturally fixed gaze, uncanny and deeply unsettling"
    "computer in front"
    #"Jesus at the office"
)

negative_prompt = (
    "photorealistic, 3D render, digital illustration, cartoon, anime, "
    "clean smooth surfaces, glossy, modern photography, "
    "text"
)
image = pipe(
    prompt=prompt,
    negative_prompt=negative_prompt,
    height=512,
    width=512,
    guidance_scale=5 ,
    num_inference_steps=30,
).images[0]

display(image)
