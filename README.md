# ⚽ Soccer Hackpad

A custom 4-button mechanical keyboard designed for soccer enthusiasts and gamers. This hackpad features soccer-themed keymaps and macros, perfect for soccer games, streaming, or just showing your love for the beautiful game.

## ��️ Hardware

- **PCB**: Custom hackpad design (KiCad files included)
- **Case**: 3D printed case (STL file included)
- **Switches**: 4 mechanical switches
- **Microcontroller**: Compatible with CircuitPython and KMK firmware
- **Pins**: D1, D2, D3, D4

## 🎮 Features

### Default Keymap (Soccer Game Controls)
- **Button 1**: `W` - Pass/Shoot
- **Button 2**: `S` - Tackle/Defend  
- **Button 3**: `SHIFT` - Sprint/Dribble
- **Button 4**: `TAB` - Tactical View

### Alternative Keymaps

#### Soccer Phrases Keymap
- **Button 1**: "GOAL! ⚽"
- **Button 2**: "Nice pass! ��"
- **Button 3**: "Foul! ��"
- **Button 4**: "Substitution 🔄"

#### Advanced Game Controls Keymap
- **Button 1**: Pass + Sprint combo
- **Button 2**: Tackle + Tactical view combo
- **Button 3**: "Kickoff! 🏟️"
- **Button 4**: "Full time! ⏰"

## 🚀 Getting Started

### Prerequisites
- CircuitPython compatible microcontroller
- KMK firmware
- 4 mechanical switches
- 3D printed case (optional)

### Installation

1. **Flash CircuitPython** to your microcontroller
2. **Install KMK firmware**:
   ```bash
   # Copy KMK files to your microcontroller
   # Download from: https://github.com/KMKfw/kmk_firmware
   ```

3. **Copy the firmware**:
   ```bash
   # Copy main.py to your microcontroller's root directory
   ```

4. **Customize keymap** (optional):
   - Edit `main.py` to uncomment your preferred keymap
   - Modify macros to suit your needs

### Pin Configuration
```python
PINS = [board.D3, board.D4, board.D2, board.D1]
```

## 🎯 Use Cases

### Soccer Gaming
- FIFA, PES, or other soccer games
- Quick access to common game controls
- Tactical view switching

### Streaming & Content Creation
- Soccer commentary macros
- Quick reactions during live streams
- Game highlight moments

### General Use
- Custom shortcuts for any application
- Gaming macros
- Productivity shortcuts

## 🎯 Customization

### Adding New Macros
```python
# Example: Add a new celebration macro
KC.MACRO("What a goal! 🎉")
```

### Creating Key Combinations
```python
# Example: Pass + Sprint combo
KC.Macro(Press(KC.W), Tap(KC.LSHIFT), Release(KC.W))
```

### Changing Keycodes
Refer to the [KMK Keycodes Documentation](https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md) for available keycodes.

## 📁 Project Structure 