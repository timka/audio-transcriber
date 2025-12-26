## Requirements

  * [zsh-autoenv](https://github.com/Tarrasch/zsh-autoenv)
  * [zsh-autoenv-track](https://github.com/timka/zsh-autoenv-track)
  * [uv](https://docs.astral.sh/uv/)

## Usage

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
find-audio | transcribe
find-dafts | pipe-edit-drafts

# Override defaults
find-audio | MODEL_SIZE=large-v3 MODEL_LANGUAGE=ru transcribe

# Persist overrides
echo "MODEL_SIZE=large-v3" >> ./.env
echo "MODLE_LANGUAGE=ru" >> ./.env
```
