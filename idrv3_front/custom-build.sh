#!/bin/bash

# Run the regular build command
npm run build

# Check if the build directory has the expected structure
if [ ! -d "build/public" ]; then
  # Create a public directory inside build
  mkdir build/public

  # Move all files from build to build/public except for the public directory itself
  mv build/* build/public/ 2>/dev/null
fi
