export AUTOENV_TRACK_DEBUG=true

which zinit > /dev/null \
|| zsh -c "$( \
  curl \
    --fail \
    --show-error \
    --silent \
    --location \
    https://raw.githubusercontent.com/zdharma-continuum/zinit/HEAD/scripts/install.sh \
)"

zinit load "timka/zsh-autoenv-track"

@autoenv-track-pre

# Defaults
export DATA_DIR=data
export AUDIO_DIR=$DATA_DIR/audio
export DRAFTS_DIR=$DATA_DIR/drafts
export TRANSCRIPTS_DIR=transcripts
export MODEL_SIZE=large-v3
export MODEL_LANGUAGE=en
export MODEL_BEAM_SIZE=5
export MODEL_DEVICE=cpu
export MODEL_CPU_THREADS=5

export ENV_FILE=./.env
test -f $ENV_FILE || touch "$ENV_FILE"
setopt allexport
. "$ENV_FILE"
unsetopt allexport

mkdir -p "$DATA_DIR"
mkdir -p "$AUDIO_DIR"
mkdir -p "$DRAFTS_DIR"
mkdir -p "$TRANSCRIPTS_DIR"

alias dl-audio='./dl-audio'
alias transcribe='./transcribe'
alias run-pipeline='dl-audio | transcribe'
alias find-audio='find $AUDIO_DIR -type f'
alias find-drafts='find $DRAFTS_DIR -type f'

function edit-drafts() {
  local args=("$@")
  for arg in "$args[@]" ; do
    fname="${arg:?Empty value in args}"
    basename="${fname:t}"
    cp "$fname" "$TRANSCRIPTS_DIR/${basename}"
    "$EDITOR" "$TRANSCRIPTS_DIR/${basename}"
  done
}

alias pipe-edit-drafts='xargs ${EDITOR:?}'

@autoenv-track-post
