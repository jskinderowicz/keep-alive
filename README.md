# Keep Alive

A Python project that builds a keep-alive application.

## Project Structure

```
\
├── dist/                  # Distribution directory
│   └── keep_alive.exe     # Compiled executable (14.2 MB)
├── keep_alive.py          # Main Python script
├── requirements.txt       # Project dependencies
└── README.md              # This file
```

## Files

- **keep_alive.py** - Main application script
- **keep_alive.exe** - Compiled standalone executable in the `dist/` folder
- **requirements.txt** - Python package dependencies

## Installation

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Building

To build the executable from source:

```bash
pyinstaller keep_alive.spec
```

The compiled executable will be generated in the `dist/` directory.

## Usage

Run the application directly:

```bash
python keep_alive.py
```

Or use the compiled executable:

```bash
./dist/keep_alive.exe
```