#!/bin/bash

# 1. Upgrade pip first
pip install --upgrade pip

# 2. Install Rust compiler (required for tokenizers)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
export PATH="$HOME/.cargo/bin:$PATH"

# 3. Verify Rust installation and PATH
echo "Checking Rust version..."
rustc --version
echo "Current PATH:"
echo "$PATH"

# 4. Install PyTorch with CUDA support
echo "Installing PyTorch..."
pip install torch==2.2.1 torchaudio==2.2.1 --index-url https://download.pytorch.org/whl/cu118

# 5. Install other requirements
echo "Installing requirements..."
pip install -r requirements.txt
