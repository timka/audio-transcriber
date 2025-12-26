#!/usr/bin/env python3
# /// script
# dependencies = [
#     "faster-whisper>=1.2.1",
#     "soundfile>=0.13.1",
# ]
# ///

import sys
import os
from pathlib import Path
from faster_whisper import WhisperModel

MODEL_SIZE = os.environ.get(
    'MODEL_SIZE',
    'small',
)
DEVICE = os.environ.get(
    'DEVICE',
    'cpu',
)
COMPUTE_TYPE = os.environ.get(
    'COMPUTE_TYPE',
    'int8',
)
TRANSCRIPT_DIR = Path(
    os.environ.get(
        'TRANSCRIPT_DIR',
        './data/transcripts',
    )
)


def transcribe_file(
    audio_path: Path,
    language: str,
):
    TRANSCRIPT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )
    transcript_path = (
        TRANSCRIPT_DIR
        / f'{audio_path.stem}.txt'
    )
    if transcript_path.exists():
        print(
            f'✅ already done: {transcript_path}',
            file=sys.stderr,
        )
        print(transcript_path)
        return

    print(
        f'🗣️ processing: {audio_path} → {transcript_path} … ',
        file=sys.stderr,
        end='',
    )

    model = WhisperModel(
        MODEL_SIZE,
        device=DEVICE,
        compute_type=COMPUTE_TYPE,
    )
    segments, info = model.transcribe(
        str(audio_path),
        language=language,
        beam_size=5,
        vad_filter=True,
    )

    with open(
        transcript_path,
        'w',
        encoding='utf-8',
    ) as fp:
        for segment in segments:
            fp.write(f'{segment.text}\n')
    print(
        '✅ done',
        file=sys.stderr,
    )
    print(transcript_path)


def main():
    if len(sys.argv) < 2:
        print(
            f'Usage: {sys.argv[0]} <audio-file> [language=ru]',
            file=sys.stderr,
        )
        sys.exit(1)

    lang = 'ru'
    if len(sys.argv) == 3:
        lang = sys.argv[2]

    transcribe_file(
        Path(sys.argv[1]),
        lang,
    )


if __name__ == '__main__':
    main()
