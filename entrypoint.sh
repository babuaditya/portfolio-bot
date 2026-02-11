#!/bin/bash
set -e

# echo "📦 Training Rasa model..."
rasa train

# rasa run actions

echo "🚀 Starting Rasa server..."
rasa run --enable-api --cors "*"  --debug
