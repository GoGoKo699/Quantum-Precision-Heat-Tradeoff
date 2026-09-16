# Repository working rules

This repository presents a fixed precision–heat research result. The canonical scientific statement is `docs/THEOREM.md`, its resource model is `docs/MODEL.md`, and its complete argument is `docs/PROOF.md` plus `docs/CONSTRUCTION.md`.

Manuscript preparation is on hold. Do not start manuscript drafting, a new research campaign, release tagging, or external correspondence without the owner's instruction.

Preserve the distinction between proofs, finite tests, source comparisons, and experimental evidence. Do not infer universal correctness from sampled matrices or claim external validation that has not occurred. Public collaboration wording belongs in README; do not replace it with a request for validation. Direct collaboration, questions, corrections, suggestions, and other project inquiries to Ruge Lin at gogoko699@gmail.com. Do not instruct readers to open issues or pull requests. Keep maintainer instructions and literal math-markup examples out of the public contact section.

Use GitHub-native Markdown, plain-text headings, and `math` fenced blocks for display equations. Keep each equation outside tables and block quotes. Typeset mathematical notation in prose, lists, and tables with GitHub's protected inline math form, outside bold or italic wrappers. Reserve code formatting for executable code, commands, paths, and program identifiers. Do not introduce custom macros, a documentation website, or a separate site deployment stack.

Optimize layout for normal desktop GitHub reading. Keep related short definitions together and break derivations at mathematical steps rather than individual terms. Preserve readable font sizes and protected inline math; do not split every display to fit a phone-width column.

Keep one textbook as the teaching anchor while retaining primary-research attribution. Do not redistribute textbook chapters, scans, or third-party papers. Every current local link and reproduction command must work without earlier conversations or archives.

Run `python -m unittest discover -s tests -v`, `python scripts/reproduce.py`, and `python scripts/check_repository.py`. Update expected numerical data only when the corresponding derivation or an identified numerical correction justifies it. Preserve the MIT license and source inventory.

For scientific or implementation changes, identify the precise claim, affected assumptions, calculations, and any additional physical resources. Preserve stable source identifiers, explicit error conventions, and complete energy accounting. Do not replace the conditional two-input task by an average-state task, treat a formal purification as a physical resource, or switch between mean heat and a battery-resource cost.
