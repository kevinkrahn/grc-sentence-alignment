import re
from bertalign import Bertalign, Encoder
from bertalign.eval import *
from sentence_transformers import SentenceTransformer

files = ('documents/unaligned/first_clement_eng.txt', 'documents/unaligned/first_clement_grc.txt')

# Use a sentence embedding model trained on English and Ancient Greek text
encoder = Encoder(SentenceTransformer('kevinkrahn/shlm-grc-en', trust_remote_code=True))

# 1. Load the English and Greek text.
# 2. Split the English text into the level of granularity desired (sentences).
# 3. Split the Greek text into the smallest possible meaningful segments.
# 4. Align the English and Greek segments.
# 5. Save to file.

eng_file, grc_file = files
print(f"Aligning {eng_file} and {grc_file}")

all_eng_segments = []
all_grc_segments = []

with open(eng_file, 'r') as f:
    punc = ['.', ';', '?', '!']
    split_pattern = re.compile(rf'(?<=[{"|".join("\\" + ch for ch in punc)}])')
    for line in f.readlines():
        all_eng_segments.extend(
            s for s in map(lambda s: s.strip(), re.split(split_pattern, line)) if s)

with open(grc_file, 'r') as f:
    punc = ['.', '·', '·', ':', ';', '?', '!']
    split_pattern = re.compile(rf'(?<=[{"|".join("\\" + ch for ch in punc)}])')
    for line in f.readlines():
        all_grc_segments.extend(
            s for s in map(lambda s: s.strip(), re.split(split_pattern, line)) if s)

aligner = Bertalign(all_eng_segments, all_grc_segments, encoder, show_logs=True)
aligner.align_sents()
#aligner.print_sents()

print("Saving alignment to alignment.txt")
with open('alignment.txt', 'w') as f:
    for eng, grc in aligner.pairs():
        f.write(f"{eng}\n{grc}\n\n")