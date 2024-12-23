# Auto Macro Counter

## Overview
The **Auto Macro Counter** is a Python script that automates typing incrementing numbers using your keyboard. This script is ideal for tasks requiring repetitive typing, such as testing input fields or automating certain workflows.

## Features
- Starts typing from a customizable starting number (default: `1525`).
- Automatically types and sends incrementing numbers every 2 seconds.
- Allows the user to start and stop the macro with keyboard shortcuts.

## Requirements
- Python 3.6 or higher
- `pynput` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mtp-dev/auto-macro-counter.git
   cd auto-macro-counter
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For fish shell, use `source venv/bin/activate.fish`
   ```

3. Install dependencies:
   ```bash
   pip install pynput
   ```

## Usage

1. Run the script:
   ```bash
   python auto_macro.py
   ```

2. Use the following keyboard shortcuts:
   - Press `s` to start the macro.
   - Press `q` to stop the macro.

## Customization

- **Starting Number**: Change the `counter` variable in the script to set the starting number (default: `1525`).
- **Time Interval**: Modify the `time.sleep(2)` line to adjust the delay between each number.

## Example Output

When running, the script will:
- Type the number `1525`.
- Press Enter.
- Increment to `1526`, then `1527`, and so on, with a 2-second interval between each.

## Notes
- The script requires `pynput`, which may not be pre-installed. Use `pip install pynput` to install it.
- Ensure you have the necessary permissions if running in restricted environments.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions
Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

