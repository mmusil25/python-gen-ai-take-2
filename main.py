from diffusers import StableDiffusionPipeline
from PIL import Image
import torch

model_id = "dreamlike-art/dreamlike-diffusion-1.0"
 
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
 
pipe = pipe.to("cpu")

prompt = "a brazilian man with short curly hair drawing and a white man with a black beany hat on and a red beard who is coding"
 
image = pipe(prompt).images[0]
 
image.show()
image.save("code.png")