"""
Image generation module using Stable Diffusion API
"""

import os
from typing import Tuple, Optional
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from stability_sdk import client
import stability_sdk.utils as utils
from PIL import Image
import io

class ImageGenerator:
    """Handles image generation using Stable Diffusion API"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the image generator
        
        Args:
            api_key (str, optional): Stability AI API key. If not provided, will look for STABILITY_API_KEY env var
        """
        self.api_key = api_key or os.getenv("STABILITY_API_KEY")
        if not self.api_key:
            raise ValueError("Stability API key is required. Set STABILITY_API_KEY environment variable or pass api_key parameter.")
            
        self.stability_api = client.StabilityInference(
            key=self.api_key,
            verbose=True,
            engine="stable-diffusion-xl-1024-v1-0"
        )
        
    def generate(self, prompt: str, resolution: Tuple[int, int] = (1024, 1024)) -> Image.Image:
        """
        Generate an image using Stable Diffusion
        
        Args:
            prompt (str): Image generation prompt
            resolution (tuple): Output image resolution (width, height)
            
        Returns:
            PIL.Image: Generated image
        """
        # Ensure resolution is valid
        width, height = resolution
        if width > 1024 or height > 1024:
            raise ValueError("Maximum resolution supported is 1024x1024")
            
        # Generate the image
        answers = self.stability_api.generate(
            prompt=prompt,
            seed=utils.generate_random_seed(),
            steps=30,
            cfg_scale=7.0,
            width=width,
            height=height,
            samples=1,
            sampler=generation.SAMPLER_K_DPMPP_2M
        )
        
        # Process the response
        for resp in answers:
            for artifact in resp.artifacts:
                if artifact.type == generation.ARTIFACT_IMAGE:
                    # Convert the image data to a PIL Image
                    img = Image.open(io.BytesIO(artifact.binary))
                    return img
                    
        raise RuntimeError("No image was generated")
        
    def generate_variations(self, image: Image.Image, num_variations: int = 3) -> list:
        """
        Generate variations of an existing image
        
        Args:
            image (PIL.Image): Base image to generate variations from
            num_variations (int): Number of variations to generate
            
        Returns:
            list: List of generated variation images
        """
        # Convert PIL Image to bytes
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        
        # Generate variations
        answers = self.stability_api.generate(
            prompt="variation of the provided image, maintaining style and composition",
            init_image=img_byte_arr,
            start_schedule=0.6,
            seed=utils.generate_random_seed(),
            steps=30,
            cfg_scale=7.0,
            width=image.width,
            height=image.height,
            samples=num_variations,
            sampler=generation.SAMPLER_K_DPMPP_2M
        )
        
        # Process the response
        variations = []
        for resp in answers:
            for artifact in resp.artifacts:
                if artifact.type == generation.ARTIFACT_IMAGE:
                    img = Image.open(io.BytesIO(artifact.binary))
                    variations.append(img)
                    
        return variations 