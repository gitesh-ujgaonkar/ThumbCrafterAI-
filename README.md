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

### Prerequisites

1. **Python Version**: This project requires Python 3.10.x. It is not compatible with Python 3.12 or higher due to dependency constraints with `stability-sdk`.

2. **Visual Studio Build Tools**: Required for compiling some Python packages
   - Download and install [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
   - During installation, select "Desktop development with C++"
   - This is necessary for compiling packages like `grpcio` and other dependencies

### Step-by-Step Installation

1. **Clone the repository**:
```bash
git clone https://github.com/gitesh-ujgaonkar/ThumbCrafterAI-.git
cd ThumbCrafterAI-
```

2. **Set up Python Environment**:
```bash
# Create a virtual environment with Python 3.10
python -m venv venv --python=python3.10

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

3. **Upgrade pip and install wheel**:
```bash
python -m pip install --upgrade pip
pip install wheel
```

4. **Install dependencies**:
```bash
pip install -r requirements.txt
```

5. **Environment Variables**:
   - Create a `.env` file in the project root directory
   - Add your Stability AI API key:
```env
STABILITY_API_KEY=your_stability_api_key
```

### Troubleshooting

1. **Visual Studio Build Tools Issues**:
   - If you encounter compilation errors, ensure Visual Studio Build Tools are properly installed
   - Run the Visual Studio Installer and repair/reinstall if necessary
   - Make sure you have the "Desktop development with C++" workload installed

2. **Python Version Issues**:
   - If you have multiple Python versions installed, ensure you're using Python 3.10:
   ```bash
   python --version  # Should show Python 3.10.x
   ```
   - If not, install Python 3.10 from [python.org](https://www.python.org/downloads/release/python-3109/)

3. **Package Installation Issues**:
   - If you encounter errors with `stability-sdk` or other packages:
   ```bash
   # Try installing packages individually
   pip install Pillow==10.2.0
   pip install python-dotenv==1.0.1
   pip install numpy==1.26.4
   pip install scikit-learn==1.4.2
   pip install colorthief==0.2.1
   pip install transformers==4.38.2
   pip install torch==2.2.1
   pip install stability-sdk==0.8.5
   ```

### Development Environment Setup (Optional)

For the best development experience, we recommend:

1. **IDE Setup**:
   - VS Code with Python extension
   - PyCharm Professional/Community Edition

2. **Code Quality Tools**:
```bash
pip install black flake8 pytest
```

3. **Git Configuration**:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Verifying Installation

To verify your installation is working correctly:

```python
from thumbcrafter import ThumbCrafter

# Initialize the thumbnail creator
creator = ThumbCrafter()

# Test with a simple thumbnail
thumbnail = creator.generate_thumbnail(
    title="Test Thumbnail",
    summary="Testing installation",
    style="modern"
)
```

If you encounter any issues during installation, please:
1. Check the [Issues](https://github.com/gitesh-ujgaonkar/ThumbCrafterAI-/issues) section
2. Ensure all prerequisites are properly installed
3. Verify your Python version and environment setup

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