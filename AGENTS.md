# Repository working rules

The project is currently under collaboration, and the manuscript is being written. For questions, please contact me at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## Scientific sources

This repository presents the established precision–heat result. Read the current scientific account before editing. The resource model is `science/model.md`; statements are in `science/theorem.md`; `science/README.md` maps the proof across kinematics, environmental information, heat accounting, channel accuracy, and exact-output obstruction. The attaining device is `science/thermal_implementation.md`.

Preserve exact hypotheses, quantifiers, equations, accuracy measures, signs, units, entropy conventions, source attribution, and resource qualifications. Do not replace conditional tests by an average-state task, charge a mathematical purification as a physical resource, or silently interchange heat, work, and battery cost. A suspected scientific issue is separate from presentation cleanup.

Give each result one authoritative home under `science/`. Keep related work and the structured bibliography under `references/`, shared learning material under `learning/`, and reproducibility guidance under `verification/`. Repair incoming links when reorganizing. Preserve the complete connected argument, not just its headline.

## Learning and presentation

Retain the single Schumacher–Westmoreland anchor, the source-to-project bridge, and `learning/MILESTONES.md`. The common map has exactly M01–M30 with 14 background/preliminaries and 16 narrative/innovation targets, ordered locally to globally in each phase. Keep its settled understanding targets and dependencies independent of a learner's performance.

Personal coaching contracts, session instructions, retry rules, answers, and learner records stay outside the scientific repository. Do not recreate a public coaching guide or make shared scientific reading depend on private material. Repository furnishing does not start lessons or establish a reader's mastery.

Use GitHub-native Markdown, plain headings, fenced display mathematics, and protected inline mathematics. Keep math outside emphasis wrappers, and display equations outside tables and block quotes. Preserve readable desktop layout. Break long derivations at mathematical steps, not individual terms. Local MathJax compilation is not a hosted-rendering certificate: inspect the actual hosted README, learning entrance, and representative mathematical pages before declaring display verified.

Keep public prose about the scientific question, results, evidence, and consequential scope. Preserve the exact purpose/contact wording. Direct inquiries to Ruge Lin by email; do not replace the collaboration invitation with a public request for validation. Keep publication planning private. Do not start manuscript drafting, a new research campaign, release tagging, metadata changes, or external correspondence without the owner's instruction.

## Preservation and verification

Preserve the MIT license, numerical implementation, committed reference values, and source inventory. `verification/source_map.json` records the source-preserving reorganization; `scripts/check_structure.py` checks its retained code and equation records. Changes to those records require the corresponding scientific or documented maintenance reason.

Run:

```bash
python -m unittest discover -s tests -v
python scripts/reproduce.py
python scripts/check_repository.py
python scripts/make_figures.py
```

Documentation checks require `npm ci --ignore-scripts`. Keep the source-distribution and outside-checkout installation checks working. Distinguish analytic proof, finite numerical checks, local rendering, and actual hosted inspection; never infer an executed check from a command's presence. Report concrete access or verification limits without claiming unperformed validation.
