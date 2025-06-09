# PacMan Game v1.0.0

A classic PacMan clone built with Pygame. Navigate through mazes, eat pellets, 
avoid ghosts, and aim for the high score!

## Features
- Authentic PacMan gameplay mechanics
- Classic sound effects
- Multiple levels with increasing difficulty
- Lives system and score tracking

## Controls
- Arrow keys: Move Pac-Man
- Space: Pause/unpause the game
- ESC: Exit the game

## Download
- Windows: Download PacMan.exe from the Assets section below
- No installation required, just download and run!

## Requirements
- Windows 10 or newer (for the executable)
- For source code: Python 3.6+ with Pygame installed

## Building from Source

If you want to build the game from source:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/PacManGame.git
   cd PacManGame
   ```

2. Install requirements:
   ```
   pip install -r requirements.txt
   ```

3. Run the game:
   ```
   python main/run.py
   ```

4. Or build your own executable:
   ```
   pip install pyinstaller
   pyinstaller PacMan.spec
   ```

## Development

This project uses GitHub Actions for automated builds:

- Every push to `main` automatically builds the executable
- Tagged releases (like `v1.0.0`) automatically create GitHub Releases with the executable

To create a new release:
```
git tag v1.0.1
git push origin v1.0.1
```

## License

[MIT License](LICENSE)