"""
Example script demonstrating the ThumbCrafterAI system
"""

import os
from pathlib import Path
from thumbcrafter import ThumbCrafter

def main():
    # Create output directory if it doesn't exist
    output_dir = Path("examples/sample_thumbnails")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize the thumbnail creator
    creator = ThumbCrafter()
    
    # Example blog posts
    blog_posts = [
        {
            "title": "The Future of Artificial Intelligence",
            "summary": "Exploring the latest developments in AI and their impact on society",
            "style": "modern"
        },
        {
            "title": "10 Tips for Better Productivity",
            "summary": "Simple yet effective strategies to boost your daily productivity",
            "style": "minimal"
        },
        {
            "title": "The Art of Photography",
            "summary": "Master the fundamentals of photography and take stunning pictures",
            "style": "vibrant"
        }
    ]
    
    # Generate thumbnails for each blog post
    for i, post in enumerate(blog_posts):
        print(f"Generating thumbnail for: {post['title']}")
        
        # Generate single thumbnail
        thumbnail = creator.generate_thumbnail(
            title=post["title"],
            summary=post["summary"],
            style=post["style"]
        )
        
        # Save the thumbnail
        output_path = output_dir / f"thumbnail_{i+1}.png"
        thumbnail.save(output_path)
        print(f"Saved to: {output_path}")
        
        # Generate variations
        variations = creator.image_generator.generate_variations(thumbnail, num_variations=2)
        for j, variation in enumerate(variations):
            variation_path = output_dir / f"thumbnail_{i+1}_variation_{j+1}.png"
            variation.save(variation_path)
            print(f"Saved variation to: {variation_path}")
            
    print("\nAll thumbnails generated successfully!")

if __name__ == "__main__":
    main() 