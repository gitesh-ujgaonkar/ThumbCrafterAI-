"""
Utility module with style presets and color schemes
"""

from enum import Enum
from typing import Dict, Tuple, List

class StylePresets(Enum):
    """Available style presets for thumbnails"""
    MODERN = "modern"
    MINIMAL = "minimal"
    VIBRANT = "vibrant"
    CORPORATE = "corporate"
    CREATIVE = "creative"

class ColorSchemes:
    """Predefined color schemes for different styles"""
    
    @staticmethod
    def get_modern_scheme() -> Dict[str, Tuple[int, int, int]]:
        """Get modern style color scheme"""
        return {
            "primary": (45, 55, 72),    # Dark blue-gray
            "secondary": (74, 85, 104),  # Medium blue-gray
            "accent": (237, 242, 247)   # Light gray
        }
        
    @staticmethod
    def get_minimal_scheme() -> Dict[str, Tuple[int, int, int]]:
        """Get minimal style color scheme"""
        return {
            "primary": (26, 32, 44),    # Very dark blue
            "secondary": (160, 174, 192), # Light blue-gray
            "accent": (247, 250, 252)   # Off-white
        }
        
    @staticmethod
    def get_vibrant_scheme() -> Dict[str, Tuple[int, int, int]]:
        """Get vibrant style color scheme"""
        return {
            "primary": (220, 38, 38),   # Bright red
            "secondary": (251, 191, 36), # Bright yellow
            "accent": (16, 185, 129)    # Bright green
        }
        
    @staticmethod
    def get_corporate_scheme() -> Dict[str, Tuple[int, int, int]]:
        """Get corporate style color scheme"""
        return {
            "primary": (30, 64, 175),   # Deep blue
            "secondary": (71, 85, 105),  # Slate gray
            "accent": (241, 245, 249)   # Light gray
        }
        
    @staticmethod
    def get_creative_scheme() -> Dict[str, Tuple[int, int, int]]:
        """Get creative style color scheme"""
        return {
            "primary": (139, 92, 246),  # Purple
            "secondary": (236, 72, 153), # Pink
            "accent": (34, 211, 238)    # Cyan
        }
        
    @staticmethod
    def get_scheme_for_style(style: str) -> Dict[str, Tuple[int, int, int]]:
        """Get color scheme for a specific style"""
        schemes = {
            StylePresets.MODERN.value: ColorSchemes.get_modern_scheme,
            StylePresets.MINIMAL.value: ColorSchemes.get_minimal_scheme,
            StylePresets.VIBRANT.value: ColorSchemes.get_vibrant_scheme,
            StylePresets.CORPORATE.value: ColorSchemes.get_corporate_scheme,
            StylePresets.CREATIVE.value: ColorSchemes.get_creative_scheme
        }
        
        return schemes.get(style, ColorSchemes.get_modern_scheme)()
        
def get_optimal_text_color(background_color: Tuple[int, int, int]) -> Tuple[int, int, int]:
    """
    Calculate optimal text color based on background color
    
    Args:
        background_color (tuple): RGB background color
        
    Returns:
        tuple: RGB text color
    """
    # Calculate relative luminance
    r, g, b = [x/255 for x in background_color]
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    
    # Return black or white based on luminance
    return (0, 0, 0) if luminance > 0.5 else (255, 255, 255)
    
def calculate_text_position(
    image_size: Tuple[int, int],
    text_size: Tuple[int, int],
    position: str = "center"
) -> Tuple[int, int]:
    """
    Calculate optimal text position
    
    Args:
        image_size (tuple): Image dimensions (width, height)
        text_size (tuple): Text dimensions (width, height)
        position (str): Desired position ("center", "top", "bottom")
        
    Returns:
        tuple: (x, y) coordinates for text placement
    """
    img_width, img_height = image_size
    text_width, text_height = text_size
    
    if position == "center":
        x = (img_width - text_width) // 2
        y = (img_height - text_height) // 2
    elif position == "top":
        x = (img_width - text_width) // 2
        y = int(img_height * 0.1)  # 10% from top
    elif position == "bottom":
        x = (img_width - text_width) // 2
        y = int(img_height * 0.9) - text_height  # 10% from bottom
    else:
        raise ValueError("Invalid position. Use 'center', 'top', or 'bottom'")
        
    return (x, y) 