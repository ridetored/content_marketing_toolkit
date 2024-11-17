#!/bin/bash

echo "=== Installing Content Marketing Toolkit ==="

# Step 1: Update and upgrade the system (optional)
echo "Updating the system..."
sudo apt-get update && sudo apt-get upgrade -y

# Step 2: Check for Python installation
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Installing Python 3..."
    sudo apt-get install python3 -y
fi

# Step 3: Check for pip installation
if ! command -v pip &>/dev/null; then
    echo "pip is not installed. Installing pip..."
    sudo apt-get install python3-pip -y
fi

# Step 4: Create and activate a virtual environment (optional but recommended)
if [ ! -d "venv" ]; then
    echo "Creating a virtual environment..."
    python3 -m venv venv
    echo "Activating the virtual environment..."
    source venv/bin/activate
else
    echo "Virtual environment already exists. Activating it..."
    source venv/bin/activate
fi

# Step 5: Install required Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Step 6: Create necessary directories
echo "Creating necessary directories..."
mkdir -p config modules data

# Step 7: Generate default configuration file
CONFIG_FILE="config/settings.yaml"
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Generating default configuration file..."
    cat <<EOL >"$CONFIG_FILE"
# Settings for Content Marketing Toolkit

# API key for Semrush (used in keyword_research.py)
semrush_api_key: "your_semrush_api_key"

# Path to Google Analytics credentials (used in performance.py)
google_analytics_credentials: "path_to_your_google_credentials.json"

# API key for OpenAI (used in ai_suggestions.py)
openai_api_key: "your_openai_api_key"

# General settings
output_directory: "data/"
default_calendar_frequency: "weekly"
EOL
    echo "Default configuration file created at $CONFIG_FILE. Please update it with your API keys."
else
    echo "Configuration file already exists. Skipping generation."
fi

# Step 8: Finish setup
echo "=== Installation Complete ==="
echo "To start using the toolkit, activate the virtual environment with 'source venv/bin/activate', and run 'python main.py --help' for available commands."
