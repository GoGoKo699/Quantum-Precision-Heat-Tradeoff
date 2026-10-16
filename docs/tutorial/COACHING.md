# Coaching through the thirty milestones

[Tutorial home](README.md) · [Milestone map](MILESTONES.md) · [Model](../MODEL.md) · [Theorem](../THEOREM.md)

Use the settled [M01–M30 map](MILESTONES.md) in order. Its understanding targets, 14/16 phase allocation, and count are common to every learner, including LLMs. Adapt explanations and targeted repair within a milestone, not the map to a learner's self-assessment. The single educational anchor and the locally supplied research bridges are specified in the [tutorial guide](README.md#textbook).

## One milestone, one challenge

Every round contains **Revise → Learn → Test**. Each milestone has one challenge with as many attempts as needed. A multi-question challenge is one round, not a new teaching round for every question.

Revise supplies the necessary definitions, notation, assumptions, and earlier results. Learn explains the idea or repairs the relevant misconception. For a challenge, keep these blocks compact and do not reveal the test answers. The first attempt is not an unprepared diagnostic.

Every test question has **four options and exactly one correct answer**. All answers are selection-only. A milestone passes only when **every answer in one complete challenge attempt is correct**. Correct answers from different failed attempts cannot be pooled, and a correct learning-test answer does not itself pass the milestone.

## Initial attempt

Provide a compact Revise → Learn introduction and then a **two-question challenge**. Both correct passes the milestone. Any incorrect answer makes the completed challenge a failed attempt and triggers a dedicated learning phase.

Keep the introduction even for a learner who appears familiar with the topic. Prior knowledge can make this route short; it does not remove the initial Learn block or certify a pass in advance.

## Learning after a failed challenge

Conduct **1–3 learning rounds**. The map's suggested learning block is a project-based default; use the observed misconception to choose the actual block length. Each round contains one Revise section, one Learn section, and **one four-option test question**.

Give correctness feedback and an explanation **immediately after each learning-test answer**, including incorrect answers. Use mistakes to target the next explanation. A learning-test error **does not increase the next challenge size** and does not count as a failed challenge.

The 1–3 rounds bound each learning phase; they are not another pass gate. Correct an error in the last learning round immediately, then address any remaining misconception in the next challenge's preparation. Do not create an unlimited remedial loop inside the learning phase. After the block, make a fresh challenge attempt.

## Challenge retry rule

Let `f` be the number of completed failed challenges in the current milestone. The next challenge size is `min(2 + f, 6)`.

| Completed failed challenges | Questions in the next challenge | Requirement |
|---|---:|---|
| 0 | 2 | All correct |
| 1 | 3 | All correct |
| 2 | 4 | All correct |
| 3 | 5 | All correct |
| 4 or more | 6 | All correct |

Only a failed challenge changes `f`. Once the size reaches six, another failure still requires a 1–3-round learning block followed by a fresh six-question challenge. There is no seven-question challenge, automatic pass, or reduced threshold.

After a pass, move to the next milestone and reset `f` to zero. An interrupted or unanswered challenge is not automatically a failure; preserve the answers already submitted and resume the same attempt.

## Feedback within a challenge

The working presentation default is **one question at a time, with correctness feedback withheld until the entire challenge is answered**. Complete the whole set even after a wrong answer, then report the result and explain the mistakes. Do not let feedback on an early question disclose the answer to a later one.

This delayed feedback applies to multi-question challenges only. Learning-round feedback remains immediate. Presenting questions sequentially does not turn them into separate Revise → Learn → Test rounds.

## Teach understanding, not formula recall

Keep the scientific model visible. Explain a concrete operation or physical distinction, introduce notation before using it, and connect equations to their operational meaning. Use the existing worked examples or a checked, model-consistent variant. Teach in the session rather than requiring the learner to read an entire textbook before receiving an explanation.

Questions should ask for an inference, changed-condition prediction, mechanism, resource-accounting judgment, or distinction between plausible explanations. Supply necessary definitions and formulas in the preparation, but do not make the correct option a copied sentence. Require at most minimal mental calculation, not lengthy algebra or numerical work. Not every question needs to be mathematical.

Use plausible conceptual distractors and unambiguous single answers. Retry questions must be fresh applications, not merely relabeled repetitions. Larger challenges collect broader evidence within the same understanding target rather than demand harder arithmetic.

An ambiguous, malformed, or unreadable item is a presentation failure, not a conceptual mistake by the learner. Repair or replace it without increasing `f` or awarding an unsupported pass. The open worked checkpoints in the three reading chapters are explanatory material, not ready-made challenge attempts or evidence of milestone completion.

## Answer selection and mathematical display

Prefer genuine native answer buttons or selectable quiz options when the interface actually supports answer submission. Plain Markdown options, ordinary links, or decorative buttons are not such controls. When native selection is unavailable, state the limitation briefly and use a minimal fallback such as one option letter. Do not require free-text explanations as the answer format or claim that static options are interactive.

Keep equations readable and notation consistent with the canonical files. In repository Markdown, use the [repository's formatting rules](../../AGENTS.md); in a teaching interface, use the math syntax that actually renders there. Repair a display problem before treating the response as assessment evidence.

## Session state and resumption

Keep learner state separate from the common map and out of public repository progress records. A resumable session should retain:

| State | Meaning |
|---|---|
| Map version and passed IDs | The understanding map used and milestones actually passed under it |
| Current milestone and mode | Initial challenge, learning phase, or retry challenge |
| Failed-challenge count `f` | Escalation for this milestone only |
| Active challenge | Its fixed size, question positions, submitted selections, and grading record held until completion |
| Learning block | Its chosen length, current round, misconception, and immediate feedback already given |

Previously completed study can inform explanations, but old question counts and answers do not automatically become passes under this map. A continuation request, acceptance of an explanation, or repository approval is not a test answer. Resume valid state rather than inventing progress or repeatedly resetting completed milestones.

## Completion and evidence

Passing **all 30 milestones** completes this project-understanding tutorial. State that completion explicitly. The integrative final milestones supply the endpoint; do not append a hidden final examination, extra curriculum, or additional mastery gate.

The shortest route is **60 challenge questions**, when every initial two-question challenge is passed. Learning rounds and retries increase the total. The six-question cap is per attempt, not a cap on total questions per milestone; repeated failures imply no fixed maximum course length.

Completion supports the conceptual understanding actually demonstrated. It does not establish exhaustive technical mastery, independent scientific correctness, or guaranteed readiness for every collaborator question. Distinguish those evidence boundaries without withholding the tutorial-completion declaration once all milestones are passed.
