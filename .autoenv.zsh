export MODEL_LANGUAGE=${MODEL_LANGUAGE:-ru}
export MODEL_SIZE=${MODEL_SIZE:-large-v3}
alias dl-audio='./dl-audio'
alias transcribe='./transcribe'
alias run-pipeline='dl-audio | transcribe'
