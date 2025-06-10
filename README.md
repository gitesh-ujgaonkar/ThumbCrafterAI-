# ThumbCrafterAI

An automated system for creating eye-catching blog thumbnails using AI image generation and smart text placement.

## Features

- Content Analysis
  - Blog title and summary extraction
  - Key theme identification
  - Smart image prompt generation
  - Color scheme detection

- Image Generation
  - Stable Diffusion API integration
  - Multiple style presets
  - Customizable resolution
  - Batch generation support

- Text Overlay
  - Dynamic text placement
  - Smart font selection
  - Readability optimization
  - Brand consistency

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ThumbCrafterAI.git
cd ThumbCrafterAI
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with your API keys:
```
STABILITY_API_KEY=your_stability_api_key
```

## Usage

1. Basic usage:
```python
from thumbcrafter import ThumbCrafter

# Initialize the thumbnail creator
creator = ThumbCrafter()

# Generate a thumbnail
thumbnail = creator.generate_thumbnail(
    title="Your Blog Title",
    summary="Your blog summary or description",
    style="modern"  # Optional: choose from available styles
)

# Save the thumbnail
thumbnail.save("output/thumbnail.png")
```

2. Batch generation:
```python
# Generate multiple thumbnails with different styles
thumbnails = creator.generate_batch(
    title="Your Blog Title",
    summary="Your blog summary",
    styles=["modern", "minimal", "vibrant"]
)
```

## Project Structure

```
ThumbCrafterAI/
├── thumbcrafter/
│   ├── __init__.py
│   ├── content_analyzer.py
│   ├── image_generator.py
│   ├── text_overlay.py
│   └── utils.py
├── tests/
│   └── test_thumbcrafter.py
├── examples/
│   └── sample_thumbnails/
├── requirements.txt
└── README.md
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 