#!/usr/bin/env bash
# Builds an Ollama model from your persona prompt plus the emotion layer.
# Usage: ./build-modelfile.sh [base-model] [new-model-name] [compact|full]
# Example: ./build-modelfile.sh qwen2.5:14b mer-twin compact
#   compact (default): about 1,000 tokens, best for 7B-14B local models
#   full:              about 4,500 tokens, every rule and ladder; needs a larger context window
set -euo pipefail
cd "$(dirname "$0")"

BASE="${1:-qwen2.5:14b}"
NAME="${2:-mer-twin}"
LAYER_MODE="${3:-compact}"

case "$LAYER_MODE" in
  compact) LAYER=emotion-layer-compact.md; CTX=8192 ;;
  full)    LAYER=emotion-layer.md;         CTX=16384 ;;
  *) echo "Third argument must be compact or full."; exit 1 ;;
esac

if [ ! -f persona.md ]; then
  echo "persona.md not found. Put your persona prompt in persona.md next to this script, then run again."
  exit 1
fi
if grep -q '"""' persona.md; then
  echo 'persona.md contains """ which would break the Modelfile. Remove it and run again.'
  exit 1
fi

{
  echo "FROM $BASE"
  echo "PARAMETER num_ctx $CTX"
  echo "PARAMETER temperature 0.7"
  echo 'SYSTEM """'
  cat persona.md
  echo
  echo
  cat "$LAYER"
  echo '"""'
} > Modelfile

ollama create "$NAME" -f Modelfile
echo "Done ($LAYER_MODE layer). Try: ollama run $NAME"
