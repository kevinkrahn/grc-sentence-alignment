import re
from bertalign import Bertalign, Encoder
from bertalign.eval import *
from sentence_transformers import SentenceTransformer

punc = ['.', '·', '·', ':', ';', '?', '!']
split_pattern = re.compile(rf'(?<=[{"|".join("\\" + ch for ch in punc)}])')

files = [
    ('didache_eng.txt', 'didache_grc.txt'),
    ('polycarp_epistle_to_the_philippians_eng.txt', 'polycarp_epistle_to_the_philippians_grc.txt'),
    ('mark_eng.txt', 'mark_grc.txt'),
    ('romans_eng.txt', 'romans_grc.txt'),
]

# Use a sentence embedding model trained on English and Ancient Greek text
encoder = Encoder(SentenceTransformer('kevinkrahn/shlm-grc-en', trust_remote_code=True))

# 1. Load the English text, which is already split into sentences or verses at the level of granularity desired (one per line).
# 2. Split the Greek text by punctuation into small segments.
# 3. Align the English and Greek segments.
# 4. Evaluate how well the new alignment matches the original aligned text.

for eng_file, grc_file in files:
    print(f"Aligning {eng_file} and {grc_file}")

    with open('documents/aligned/'+eng_file, 'r') as f:
        eng_lines = [l for l in map(lambda l: l.strip(), f.readlines()) if l]
    with open('documents/aligned/'+grc_file, 'r') as f:
        grc_lines = [l for l in map(lambda l: l.strip(), f.readlines()) if l]

    all_eng_segments = []
    all_grc_segments = []

    gold_alignments = []
    for eng_line, grc_line in zip(eng_lines, grc_lines):
        eng_segments = [eng_line]
        grc_segments = [s for s in map(lambda s: s.strip(), re.split(split_pattern, grc_line)) if s]
        gold_alignments.append((
            [*range(len(all_eng_segments), len(all_eng_segments)+len(eng_segments), 1)],
            [*range(len(all_grc_segments), len(all_grc_segments)+len(grc_segments), 1)],
        ))
        all_eng_segments.extend(eng_segments)
        all_grc_segments.extend(grc_segments)

    aligner = Bertalign(all_eng_segments, all_grc_segments, encoder, show_logs=True)
    aligner.align_sents()
    #aligner.print_sents()

    scores = score_multiple(gold_list=[gold_alignments], test_list=[aligner.result])
    log_final_scores(scores)
