# PDA Simulator

A Pushdown Automata simulator built with Flask.

This project lets you test strings against predefined context-free language patterns and view each computation step, including state, remaining input, and stack contents.

## Features

- Web interface for interactive simulation
- Step-by-step trace output
- Accept/Reject result with dead-state visibility
- CLI mode for terminal-based runs
- 11 built-in PDA language definitions
- Ready-to-deploy Vercel configuration

## Supported Languages

Choose one of the following language sets in the UI or CLI:

1. L = { a^n b^n : n >= 0 }
2. L = { a^n b^(2n) : n >= 0 }
3. L = { a^m b^n c^(m+n) : m,n >= 0 }
4. L = { a^n b^m c^m d^n : m,n >= 0 }
5. L = { w c w^R : w in {a,b}* }
6. L = { w w^R : w in {a,b}* }
7. L = { a^m b^n : m >= n >= 0 }
8. Balanced parentheses
9. L = { a^n b^n c^m : n,m >= 0 }
10. L = { w in {a,b}* : #a = #b }
11. L = { a^n b^n } U { a^n b^(2n) }

## Tech Stack

- Python 3.11
- Flask
- HTML + Tailwind CSS + JavaScript

## Project Structure

- app.py: Flask routes and API endpoint
- pda.py: PDA engine and transition execution logic
- lang.py: predefined PDA language configurations
- runner.py: command-line simulator
- templates/index.html: web interface
- api/index.py: Vercel serverless entry point
- vercel.json: Vercel routing/build configuration
- requirements.txt: dependencies

## Run Locally

1. Create and activate a virtual environment.

    Windows PowerShell:

    ```powershell
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

    macOS/Linux:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Start the app:

    ```bash
    python app.py
    ```

4. Open in browser:

    http://127.0.0.1:5000

## CLI Usage

Run the simulator from terminal:

```bash
python runner.py -i <language_id>
```

Example:

```bash
python runner.py -i 1
```

Then type the input string when prompted.

## Final Notes

- This simulator is designed for learning, experimentation, and classroom demos.
- You can extend it by adding new PDA definitions in lang.py.
- For deployments, keep vercel.json, api/index.py, and requirements.txt in sync.

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request with a clear description.

## Contributors

[![Contributors](https://contrib.rocks/image?repo=Akshith-cdr/PDA-SIMULATOR)](https://github.com/Akshith-cdr/PDA-SIMULATOR/graphs/contributors)

See full list with commit counts: [Contributors-Graphs](https://github.com/Akshith-cdr/PDA-SIMULATOR/graphs/contributors)

## Acknowledgment

If this project helps your automata theory practice, consider starring the repository and sharing it with classmates.
