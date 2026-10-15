# Reproducible writing demo

This is one actual paired run in Google Gemini on October 15, 2026. The same writing task was submitted once without Maya Okafor's context and once with her root, identity, and personal brand files. Maya and her business are fictional public examples. The responses are actual, unedited model outputs.

A [vibegraph is a person's network of identity and context for AI](https://vibegraph.md/what-is-a-vibegraph/). This demo shows what happened when selected files from one were supplied to a writing assistant. It does not establish a general performance improvement.

## What happened

Both responses explained a weekly client update, included three things to cover, and ended with a practical action. The context response used more of Maya's supplied brand language. It also made an unsupported claim that requires correction before publication.

| Observation | Task only | Task with context |
| --- | --- | --- |
| Requested length of 150 to 180 words | 132 whitespace tokens, below the target | 157 whitespace tokens, within the target |
| Words excluding Markdown list markers | 129 | 154 |
| Three update sections and a final action | Present | Present |
| Plain, instructional, second-person prose | Present, with abstract phrases such as “weekly touchpoint” | Present, with brand-specific framing |
| Distinctive language from Maya's brand | No distinctive supplied brand phrases identified | Calm, evenings, boring systems, and a firm ten times your size |
| Exclamation points or fictional personality scores | None | None |
| Invented personal/client anecdote or measured result | None identified | None identified |
| Grounding concern | General assertions about trust and fewer check-ins are not demonstrated by this run | Opens with an unsupported claim about why most solo consultants fail |

**The context output is not ready to publish unchanged.** Its opening says, “Most solo consultants fail not from lack of skill, but from letting client updates slip.” The supplied files do not establish that claim. Adding identity and brand context did not ensure factual accuracy. Its “firm ten times your size” phrase reflects brand rhetoric, not a measured outcome. Neither response uses a deadline or scarcity offer, but both describe negative consequences of silence. The context response's opening overstates those consequences.

Read the complete [baseline response](outputs/baseline.md) and [context response](outputs/context.md). Screenshots of the completed responses are saved for [baseline](outputs/baseline.jpg) and [context](outputs/context.jpg). No response was rewritten, regenerated, or selected from multiple candidates.

## Repeat the procedure

1. Open Gemini and start a fresh Temporary Chat. Select the same available mode for both conditions. This run used **Auto**, whose menu described **Gemini 3 models**.
2. Paste the complete [baseline prompt](baseline-prompt.txt). Submit once and save the first completed response using the provider's Copy control. Record the visible mode and UTC submission and capture times.
3. Start a separate fresh Temporary Chat. Paste the complete [context prompt](context-prompt.txt). Submit once, save the first completed response, and record the same details. Do not continue the baseline conversation or supply its response.
4. Compare both responses using the [recorded protocol](PROTOCOL.md). Preserve failures and unmet criteria. Record any retry and its reason instead of silently replacing an answer.

The [task](task.txt) is identical in both prompts. It asks for a 150 to 180 word LinkedIn post about weekly client updates and forbids browsing, invented client stories, measured outcomes, and unsupported biographical details. The context prompt adds a short fixture wrapper and verbatim copies of these files before the task:

- [VIBEGRAPH.md](inputs/VIBEGRAPH.md)
- [identity/maya-okafor.md](inputs/identity/maya-okafor.md)
- [brands/maya-okafor.brand.md](inputs/brands/maya-okafor.brand.md)

These are version 3.0 fixtures copied from [commit c2e2c3f](https://github.com/vibegraph-ai/vibegraph.md/tree/c2e2c3fedb42eb04cfba5ddc47ad9bae7135b87e/examples/maya-okafor.vibegraph). Only the three included files were supplied. References inside them do not imply that linked files, private areas, or websites were fetched.

## Verify the archive

From the repository root, run:

```sh
python3 examples/reproducible-demo-2026-10-15/verify.py
```

The script uses only Python's standard library and makes no network requests. It checks the archived hashes, confirms that both prompts contain the same task and that the context contains the saved input files, and prints the word counts. It does not generate a new model response or independently authenticate the provider.

[manifest.json](manifest.json) contains SHA-256 hashes and the source commit. [run.json](run.json) records the provider, visible mode, UTC times, capture method, and one generation with zero retries for each condition. The protocol was written before these responses were generated. It was not publicly preregistered.

## Limits

This is a repeatable procedure, not a promise of identical generated text. Gemini's Auto mode can route between backend models. The exact backend model, temperature, and seed were not exposed and are recorded as unknown. The prompts forbade browsing and neither response displayed search or source controls. Network access was not independently disabled or audited.

There is one response per condition, no blinded evaluation, and no control containing equivalent context in ordinary prose. The added wrapper also changes the prompt. This run cannot isolate the effect of the file format, prove a causal improvement, or measure reliability across tasks and models. Files were pasted into chat, so this is not a test of graph traversal, permissions enforcement, or the Vibegraph app. The useful observation is narrower. The supplied context was reflected in the output, alongside a factual overstatement that still needed human review.
