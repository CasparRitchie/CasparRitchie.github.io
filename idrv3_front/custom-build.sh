#!/bin/bash

# Run the regular build command
npm run build

# Navigate to the build directory
cd build

# Check if the build directory has the expected structure
if [ ! -d "public" ]; then
  # Create a public directory inside build
#   mkdir public

#   # Move all files from build to build/public except for the public directory itself
#   mv * public/ 2>/dev/null
cd ..
fi
