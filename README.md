```zsh
# Should be sourced manually or loaded via zsh-autoenv
source ./.autoenv.zsh

uv sync
source .venv/bin/activate

# Put some urls into data/urls
echo "https://rutube.ru/video/16bebfc371c4e2f4940fdc908f35993d/" > data/urls

# Run pipeline (idempotent)
cat data/urls | run-pipeline

# Or run separate steps 
cat data/urls | dl-audio
find ./data/audio -type f | transcribe

# Override defaults
find ./data/audio -type f | MODEL_SIZE=small MODE_LANGUAGE=en transcribe
```
