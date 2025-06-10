"""
Content analysis module for extracting themes and generating image prompts
"""

import re
from typing import List, Dict, Tuple
from transformers import pipeline
from colorthief import ColorThief
import numpy as np
from .utils import StylePresets, ColorSchemes

class ContentAnalyzer:
    """Analyzes blog content to extract themes and generate image prompts"""
    
    def __init__(self):
        """Initialize the content analyzer with necessary models"""
        self.theme_extractor = pipeline("zero-shot-classification")
        self.candidate_themes = [
            "technology", "business", "lifestyle", "health", "education",
            "entertainment", "sports", "science", "art", "food",
            "travel", "fashion", "finance", "environment", "politics"
        ]
        
    def analyze(self, title: str, summary: str) -> List[str]:
        """
        Analyze blog content to extract main themes
        
        Args:
            title (str): Blog post title
            summary (str): Blog post summary
            
        Returns:
            List[str]: List of identified themes
        """
        # Combine title and summary for analysis
        content = f"{title} {summary}"
        
        # Extract themes using zero-shot classification
        result = self.theme_extractor(
            content,
            candidate_labels=self.candidate_themes,
            multi_label=True
        )
        
        # Get themes with confidence > 0.3
        themes = [
            theme for theme, score in zip(result['labels'], result['scores'])
            if score > 0.3
        ]
        
        return themes[:3]  # Return top 3 themes
    
    def extract_color_scheme(self, themes: List[str]) -> Dict[str, Tuple[int, int, int]]:
        """
        Generate a color scheme based on themes
        
        Args:
            themes (List[str]): List of identified themes
            
        Returns:
            Dict[str, Tuple[int, int, int]]: Color scheme with primary and secondary colors
        """
        # Map themes to color schemes
        theme_colors = {
            "technology": [(0, 120, 212), (0, 153, 204)],  # Blue shades
            "business": [(44, 62, 80), (52, 73, 94)],      # Dark blue
            "lifestyle": [(231, 76, 60), (192, 57, 43)],   # Red shades
            "health": [(46, 204, 113), (39, 174, 96)],     # Green shades
            "education": [(155, 89, 182), (142, 68, 173)], # Purple shades
            "entertainment": [(241, 196, 15), (243, 156, 18)], # Yellow shades
            "sports": [(230, 126, 34), (211, 84, 0)],      # Orange shades
            "science": [(52, 152, 219), (41, 128, 185)],   # Light blue
            "art": [(231, 76, 60), (192, 57, 43)],         # Red shades
            "food": [(230, 126, 34), (211, 84, 0)],        # Orange shades
            "travel": [(46, 204, 113), (39, 174, 96)],     # Green shades
            "fashion": [(155, 89, 182), (142, 68, 173)],   # Purple shades
            "finance": [(44, 62, 80), (52, 73, 94)],       # Dark blue
            "environment": [(46, 204, 113), (39, 174, 96)], # Green shades
            "politics": [(231, 76, 60), (192, 57, 43)]     # Red shades
        }
        
        # Get colors for the first theme
        primary_theme = themes[0] if themes else "technology"
        colors = theme_colors.get(primary_theme, theme_colors["technology"])
        
        return {
            "primary": colors[0],
            "secondary": colors[1]
        }
    
    def generate_prompt(self, title: str, themes: List[str], style: str) -> str:
        """
        Generate an image prompt based on content and style
        
        Args:
            title (str): Blog post title
            themes (List[str]): List of identified themes
            style (str): Style preset to use
            
        Returns:
            str: Generated image prompt
        """
        # Style-specific prompt templates
        style_templates = {
            "modern": "modern minimalist {theme} concept, clean design, professional photography, high quality, 4k",
            "minimal": "minimalist {theme} illustration, simple shapes, flat design, pastel colors, clean background",
            "vibrant": "vibrant {theme} scene, bold colors, dynamic composition, eye-catching, professional photography",
            "corporate": "professional {theme} business concept, corporate style, clean design, high-end photography",
            "creative": "creative {theme} concept, artistic composition, unique perspective, professional photography"
        }
        
        # Get the main theme
        main_theme = themes[0] if themes else "general"
        
        # Generate the prompt
        template = style_templates.get(style, style_templates["modern"])
        prompt = template.format(theme=main_theme)
        
        # Add style-specific modifiers
        if style == "modern":
            prompt += ", contemporary design, sleek"
        elif style == "minimal":
            prompt += ", white space, elegant"
        elif style == "vibrant":
            prompt += ", saturated colors, energetic"
        elif style == "corporate":
            prompt += ", business environment, professional"
        elif style == "creative":
            prompt += ", artistic interpretation, unique"
            
        return prompt 