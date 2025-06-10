"""
Text overlay module for adding text to generated images
"""

from typing import Dict, Tuple
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from .utils import StylePresets

class TextOverlay:
    """Handles text overlay on generated images"""
    
    def __init__(self):
        """Initialize the text overlay handler"""
        self.font_sizes = {
            "small": 0.05,    # 5% of image height
            "medium": 0.08,   # 8% of image height
            "large": 0.12     # 12% of image height
        }
        
        self.font_weights = {
            "light": "Light",
            "regular": "Regular",
            "bold": "Bold"
        }
        
    def add_text(self, image: Image.Image, text: str, color_scheme: Dict[str, Tuple[int, int, int]], style: str) -> Image.Image:
        """
        Add text overlay to the image
        
        Args:
            image (PIL.Image): Base image
            text (str): Text to overlay
            color_scheme (dict): Color scheme for text
            style (str): Style preset to use
            
        Returns:
            PIL.Image: Image with text overlay
        """
        # Create a copy of the image to work with
        img = image.copy()
        draw = ImageDraw.Draw(img)
        
        # Get image dimensions
        width, height = img.size
        
        # Determine font size based on image height
        font_size = int(height * self.font_sizes["medium"])
        
        # Load appropriate font
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            # Fallback to default font if Arial is not available
            font = ImageFont.load_default()
            
        # Calculate text size
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # Calculate text position
        x = (width - text_width) // 2
        y = (height - text_height) // 2
        
        # Add text shadow for better readability
        shadow_offset = int(font_size * 0.02)  # 2% of font size
        draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=(0, 0, 0, 128))
        
        # Add main text
        draw.text((x, y), text, font=font, fill=color_scheme["primary"])
        
        # Add style-specific effects
        if style == "modern":
            self._add_modern_effects(img, text, color_scheme)
        elif style == "minimal":
            self._add_minimal_effects(img, text, color_scheme)
        elif style == "vibrant":
            self._add_vibrant_effects(img, text, color_scheme)
            
        return img
        
    def _add_modern_effects(self, image: Image.Image, text: str, color_scheme: Dict[str, Tuple[int, int, int]]):
        """Add modern style effects to the image"""
        # Add subtle gradient overlay
        gradient = Image.new('RGBA', image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(gradient)
        
        # Create a vertical gradient
        for y in range(image.size[1]):
            alpha = int(128 * (1 - y / image.size[1]))  # Fade from top to bottom
            draw.line([(0, y), (image.size[0], y)], fill=(0, 0, 0, alpha))
            
        # Composite the gradient
        image.paste(gradient, (0, 0), gradient)
        
    def _add_minimal_effects(self, image: Image.Image, text: str, color_scheme: Dict[str, Tuple[int, int, int]]):
        """Add minimal style effects to the image"""
        # Add subtle border
        border_width = int(image.size[0] * 0.01)  # 1% of image width
        draw = ImageDraw.Draw(image)
        draw.rectangle(
            [(border_width, border_width), 
             (image.size[0] - border_width, image.size[1] - border_width)],
            outline=color_scheme["secondary"],
            width=border_width
        )
        
    def _add_vibrant_effects(self, image: Image.Image, text: str, color_scheme: Dict[str, Tuple[int, int, int]]):
        """Add vibrant style effects to the image"""
        # Increase saturation
        img_array = np.array(image)
        img_array = img_array.astype(np.float32)
        img_array[:, :, :3] = np.clip(img_array[:, :, :3] * 1.2, 0, 255)  # Increase color intensity by 20%
        image = Image.fromarray(img_array.astype(np.uint8))
        
        # Add subtle vignette
        vignette = Image.new('RGBA', image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(vignette)
        
        # Create radial gradient
        center_x, center_y = image.size[0] // 2, image.size[1] // 2
        max_radius = max(center_x, center_y)
        
        for radius in range(max_radius, 0, -1):
            alpha = int(128 * (1 - radius / max_radius))  # Fade from center to edges
            draw.ellipse(
                [center_x - radius, center_y - radius,
                 center_x + radius, center_y + radius],
                outline=(0, 0, 0, alpha)
            )
            
        # Composite the vignette
        image.paste(vignette, (0, 0), vignette) 