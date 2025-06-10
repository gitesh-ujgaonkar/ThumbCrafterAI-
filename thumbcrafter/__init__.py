"""
ThumbCrafterAI - Automated blog thumbnail generation system
"""

from .content_analyzer import ContentAnalyzer
from .image_generator import ImageGenerator
from .text_overlay import TextOverlay
from .utils import StylePresets, ColorSchemes

__version__ = "0.1.0"
__all__ = ['ThumbCrafter', 'ContentAnalyzer', 'ImageGenerator', 'TextOverlay', 'StylePresets', 'ColorSchemes']

class ThumbCrafter:
    """Main class for generating blog thumbnails"""
    
    def __init__(self, api_key=None):
        """Initialize the ThumbCrafter with optional API key"""
        self.content_analyzer = ContentAnalyzer()
        self.image_generator = ImageGenerator(api_key)
        self.text_overlay = TextOverlay()
        
    def generate_thumbnail(self, title, summary, style="modern", resolution=(1200, 630)):
        """
        Generate a single thumbnail for a blog post
        
        Args:
            title (str): Blog post title
            summary (str): Blog post summary
            style (str): Style preset to use
            resolution (tuple): Output image resolution (width, height)
            
        Returns:
            PIL.Image: Generated thumbnail
        """
        # Analyze content
        themes = self.content_analyzer.analyze(title, summary)
        color_scheme = self.content_analyzer.extract_color_scheme(themes)
        
        # Generate base image
        prompt = self.content_analyzer.generate_prompt(title, themes, style)
        base_image = self.image_generator.generate(prompt, resolution)
        
        # Add text overlay
        thumbnail = self.text_overlay.add_text(
            base_image,
            title,
            color_scheme,
            style
        )
        
        return thumbnail
    
    def generate_batch(self, title, summary, styles=None, resolution=(1200, 630)):
        """
        Generate multiple thumbnails with different styles
        
        Args:
            title (str): Blog post title
            summary (str): Blog post summary
            styles (list): List of style presets to use
            resolution (tuple): Output image resolution
            
        Returns:
            list: List of generated thumbnails
        """
        if styles is None:
            styles = ["modern", "minimal", "vibrant"]
            
        thumbnails = []
        for style in styles:
            thumbnail = self.generate_thumbnail(title, summary, style, resolution)
            thumbnails.append(thumbnail)
            
        return thumbnails 