# Manim Animation: Shape Transformation

A simple animation project created using Manim (Mathematical Animation Engine) that demonstrates shape transformation between a rectangle and a circle.

## 📋 Project Overview

This project contains a basic Manim animation that transforms a filled rectangle into a filled circle using Manim's `Transform` animation. It serves as a simple example of Manim's capabilities for creating mathematical animations and visualizations.

## 🚀 Features

- **Shape Creation**: Creates a rectangle and a circle with different properties
- **Visual Styling**: Applies distinct fill colors and opacities to each shape
- **Smooth Transformation**: Animates the transformation from rectangle to circle
- **Simple Structure**: Clean, minimal code demonstrating Manim's basic concepts

## 🛠️ Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.7 or higher
- Manim Community Edition (manim)
- FFmpeg (for rendering videos)

## 📦 Installation

1. **Install Manim** (if not already installed):
   ```bash
   pip install manim
    Install FFmpeg:

        Ubuntu/Debian: sudo apt install ffmpeg

        macOS: brew install ffmpeg

        Windows: Download from FFmpeg website

    Clone or download this project to your local machine.

🎬 Usage
Running the Animation

Navigate to the directory containing hello_world.py and run:
bash

# Render in low quality (for testing)
manim -pql hello_world.py HelloWorld

# Render in high quality
manim -pqh hello_world.py HelloWorld

# Render in 4K quality
manim -pqk hello_world.py HelloWorld

Command Options

    -p or --preview: Automatically open the rendered video

    -q or --quality: Specify quality level

        l: Low (480p)

        h: High (1080p)

        k: 4K (2160p)

    -o or --output_file: Specify custom output filename

📁 Project Structure
text

manim-shape-transformation/
│
├── hello_world.py          # Main animation script
├── README.md               # Project documentation (this file)
└── media/                  # Rendered videos (created after running)
    └── videos/
        └── hello_world/
            └── 1080p60/
                └── HelloWorld.mp4

🧩 Code Explanation

The animation consists of:

    Scene Definition: HelloWorld class inheriting from Scene

    Shape Creation:

        Rectangle() with grey-brown fill (opacity 1.5)

        Circle() with pink fill (opacity 0.5)

    Animation: Transform() effect morphing rectangle into circle

Key Components:

    Rectangle(): Creates a rectangle shape

    Circle(): Creates a circle shape

    set_fill(): Sets the fill color and opacity

    Transform(): Animates transformation between two mobjects

    self.play(): Plays the animation in the scene

🎨 Customization

You can modify the animation by:

    Changing colors (Manim has predefined colors like BLUE, RED, GREEN, etc.)

    Adjusting opacity values (0.0 to 1.0)

    Modifying transformation duration

    Adding more shapes or animations

Example modification:
python

# Change colors
rectangle.set_fill(BLUE, opacity=0.8)
circle.set_fill(YELLOW, opacity=0.6)

# Change animation
self.play(Transform(rectangle, circle), run_time=3)  # Slower animation

📚 Learning Resources

    Manim Documentation

    Manim GitHub Repository

    3Blue1Brown's Manim Tutorials

    Manim Examples Gallery

🤝 Contributing

Feel free to fork this project and experiment with different animations! Some ideas:

    Add multiple shape transformations

    Include text animations

    Create mathematical visualizations

    Experiment with different Manim features

📄 License

This project is open source and available under the MIT License.
✨ Acknowledgments

    Manim Community for maintaining this powerful animation engine

    3Blue1Brown (Grant Sanderson) for creating the original Manim library

    All contributors to the Manim ecosystem
