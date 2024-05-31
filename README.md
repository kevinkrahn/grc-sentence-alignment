# Ancient Greek Translation Sentence Alignment

This repo is a demonstration of how to use [Bertalign](https://github.com/kevinkrahn/grc-bertalign) to align Ancient Greek text with English translations using
the [shlm-grc-en](https://huggingface.co/kevinkrahn/shlm-grc-en) sentence embedding model, trained specifically for this task.

## Usage

Run the `eval_alignment.py` script to compare alignment quality using different sentence embedding models.

Run the `run_alignment.py` script to align Greek texts with an English translation.

If your texts are already aligned in chunks such as paragraphs or chapters, you can improve your alignment quality by aligning these chunks separately.

The alignment confidence range depends on the model used and varies based on the anisotropy of the embedding space.

## Evaluation Results

The following is the output from running the evaluation script on the documents in the `documents/aligned` folder, which include:

* Didache
* Polycarp's Letter to the Philippians
* Gospel of Mark
* Epistle to the Romans

The F1 score ranges from 93% to 100%.

```
Aligning documents/didache_eng.txt and documents/didache_grc.txt
Embedding source text...
Embedding target text...
Performing first-step alignment...
Performing second-step alignment...
Finished! Successfully aligned 104 source sentences to 185 target sentences

Alignment confidence: 0.40148880037481904
 ---------------------------------
|             |  Strict |    Lax  |
| Precision   |   0.933 |   1.000 |
| Recall      |   0.933 |   1.000 |
| F1          |   0.933 |   1.000 |
 ---------------------------------
Aligning documents/polycarp_epistle_to_the_philippians_eng.txt and documents/polycarp_epistle_to_the_philippians_grc.txt
Embedding source text...
Embedding target text...
Performing first-step alignment...
Performing second-step alignment...
Finished! Successfully aligned 54 source sentences to 60 target sentences

Alignment confidence: 0.3896088653382997
 ---------------------------------
|             |  Strict |    Lax  |
| Precision   |   1.000 |   1.000 |
| Recall      |   1.000 |   1.000 |
| F1          |   1.000 |   1.000 |
 ---------------------------------
Aligning documents/mark_eng.txt and documents/mark_grc.txt
Embedding source text...
Embedding target text...
Performing first-step alignment...
Performing second-step alignment...
Finished! Successfully aligned 661 source sentences to 1046 target sentences

Alignment confidence: 0.45279582084667297
 ---------------------------------
|             |  Strict |    Lax  |
| Precision   |   0.979 |   1.000 |
| Recall      |   0.979 |   1.000 |
| F1          |   0.979 |   1.000 |
 ---------------------------------
Aligning documents/romans_eng.txt and documents/romans_grc.txt
Embedding source text...
Embedding target text...
Performing first-step alignment...
Performing second-step alignment...
Finished! Successfully aligned 432 source sentences to 571 target sentences

Alignment confidence: 0.38396531817949253
 ---------------------------------
|             |  Strict |    Lax  |
| Precision   |   0.986 |   1.000 |
| Recall      |   0.986 |   1.000 |
| F1          |   0.986 |   1.000 |
 ---------------------------------
```
