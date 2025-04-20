#!/bin/bash

# 1. Upgrade pip first
pip install --upgrade pip

# 2. Install Rust compiler (required for tokenizers)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
export PATH="$HOME/.cargo/bin:$PATH"

# 3. Install PyTorch with CUDA support
pip install torch==2.2.1 torchaudio==2.2.1 --index-url https://download.pytorch.org/whl/cu118

# 4. Install other requirements
pip install -r requirements.txt
