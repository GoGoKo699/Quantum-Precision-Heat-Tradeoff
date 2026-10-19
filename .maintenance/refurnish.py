#!/usr/bin/env python3
"""One-use, base-pinned documentation migration for this repository only.

Read scientific source from the verified base commit, relocate it without
changing equations, retain scientific code/data, and validate before publishing.
The temporary runner is removed from the finished tree.
"""
from __future__ import annotations
import hashlib
import json
import posixpath
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
BASE = 'f71a388d84387f9a1cb6d2b7376c9c02743cf1d9'
REPO = 'GoGoKo699/Quantum-Precision-Heat-Tradeoff'
RAW = f'https://raw.githubusercontent.com/{REPO}/main/'
BRIDGE = 'learning/SCHUMACHER_WESTMORELAND_BRIDGE.md'

def git(*args: str) -> str:
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True)

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

origin = git('remote', 'get-url', 'origin').strip().removesuffix('.git')
assert origin in (f'https://github.com/{REPO}', f'git@github.com:{REPO}'), origin
assert git('branch', '--show-current').strip() == 'maintenance/refurnish-20261019'
for changed in git('diff', '--name-only', BASE, 'HEAD').splitlines():
    assert changed.startswith(('.maintenance/', '.github/workflows/')), changed
names = git('ls-tree', '-r', '--name-only', BASE).splitlines()
source = {name: subprocess.check_output(['git', 'show', f'{BASE}:{name}'], cwd=ROOT)
          for name in names}
text = {name: data.decode('utf-8') for name, data in source.items()
        if name.endswith(('.md', '.py', '.cjs', '.txt', '.json', '.toml', '.in', '.yml', '.cff'))}

moves = {
    'docs/MODEL.md': 'science/model.md',
    'docs/THEOREM.md': 'science/theorem.md',
    'docs/PROOF.md': 'science/README.md',
    'docs/CONSTRUCTION.md': 'science/thermal_implementation.md',
    'docs/FINITE_BENCHMARK.md': 'science/finite_benchmark.md',
    'docs/NOTATION.md': 'science/notation.md',
    'docs/CLAIMS.md': 'verification/CLAIMS.md',
    'docs/REPRODUCIBILITY.md': 'verification/README.md',
    'docs/LITERATURE.md': 'references/LITERATURE.md',
    'docs/RELATED_WORK.md': 'references/RELATED_WORK.md',
    'docs/tutorial/README.md': 'learning/README.md',
    'docs/tutorial/MILESTONES.md': 'learning/MILESTONES.md',
    'docs/tutorial/01_task.md': 'learning/01_task.md',
    'docs/tutorial/02_device.md': 'learning/02_device.md',
    'docs/tutorial/03_precision.md': 'learning/03_precision.md',
}
for name in names:
    if name.startswith('docs/figures/'):
        moves[name] = name.replace('docs/figures/', 'science/figures/', 1)

proof_groups = [
    ('output-tests', 'information-bound', 'science/kinematics.md',
     'Output accuracy and arbitrary-unitary kinematics',
     'The two output tests constrain every allowed joint unitary before Gibbs structure is used. Lemmas 1–3 translate the required coherence and small transition probabilities into spectral separation of comparison environment states.'),
    ('information-bound', 'heat-ledger', 'science/environment_information.md',
     'The information retained by the environment',
     'Lemmas 4–6 turn the spectral separation into information in the actual environment and then an entropy increase. The continuity correction depends on the binary label, not on the environment dimension.'),
    ('heat-ledger', 'channel-equivalence', 'science/heat_bound.md',
     'Heat accounting and the optimal limiting law',
     'The environmental entropy bound becomes a heat bound only after the actual Gibbs reservoir and workspace are accounted for. The universal lower direction is then matched by the fully charged thermal construction.'),
    ('channel-equivalence', 'exact-output-obstruction', 'science/channel_accuracy.md',
     'Conditional tests and full-channel accuracy',
     'An additional degenerate Gibbs qubit converts any branch-feasible device into a channel-feasible device at the same equal-prior mean heat and workspace return. This identifies the two infima without claiming a finite optimum.'),
    ('exact-output-obstruction', None, 'science/exact_outputs.md',
     'The obstruction to exact pure outputs',
     'Finite reservoir rank and exact ensemble-average workspace return exclude exactly nonorthogonal pure outputs. Positive error at each finite stage is therefore part of the limiting theorem, including its high-precision endpoint.'),
]
proof = text['docs/PROOF.md']
segments = {}
anchor_dest = {('docs/PROOF.md', 'dependencies'): 'science/README.md'}
for start, stop, destination, title, intro in proof_groups:
    begin = proof.index(f'<a id="{start}"></a>')
    end = proof.index(f'<a id="{stop}"></a>') if stop else len(proof)
    fragment = proof[begin:end].rstrip() + '\n'
    segments[destination] = fragment
    # Cover explicit and generated anchors, including subheadings and old titles.
    for anchor in re.findall(r'<a\s+(?:id|name)="([^"]+)"', fragment):
        anchor_dest[('docs/PROOF.md', anchor)] = destination
    for heading in re.findall(r'^#{2,6}\s+(.+)$', fragment, re.M):
        slug = re.sub(r'[^\w\s-]', '', heading.lower()).replace(' ', '-')
        anchor_dest[('docs/PROOF.md', slug)] = destination
for anchor in ('textbook', 'one-educational-anchor', 'beyond-textbook'):
    anchor_dest[('docs/tutorial/README.md', anchor)] = BRIDGE


def rewrite_url(url: str, old: str, new: str) -> str:
    if url.startswith(RAW):
        tail = url[len(RAW):]
        target, marker, fragment = tail.partition('#')
        destination = anchor_dest.get((target, fragment), moves.get(target, target))
        return RAW + destination + (marker + fragment if marker else '')
    if re.match(r'^[a-z][a-z0-9+.-]*:', url, re.I):
        return url
    target, marker, fragment = unquote(url).partition('#')
    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(old), target)) if target else old
    assert resolved != 'docs/tutorial/COACHING.md', f'Personal coaching link left in {old}'
    destination = anchor_dest.get((resolved, fragment), moves.get(resolved, resolved))
    if not target and destination == new:
        return '#' + fragment
    relative = posixpath.relpath(destination, posixpath.dirname(new) or '.')
    return relative + (marker + fragment if marker else '')


def relink(content: str, old: str, new: str) -> str:
    pattern = r'(!?\[[^\]\n]*\]\()([^\s)]+)(\))'
    content = re.sub(pattern, lambda m: m[1] + rewrite_url(m[2], old, new) + m[3], content)
    content = re.sub(r'(?m)^(\[[^\]]+\]:\s*)(\S+)',
                     lambda m: m[1] + rewrite_url(m[2], old, new), content)
    # llms.txt and direct self-links can contain a bare raw-content address.
    content = re.sub(re.escape(RAW) + r'[^\s)<>]+',
                     lambda m: rewrite_url(m[0], old, new), content)
    return content


def write(name: str, content: str | bytes) -> None:
    path = ROOT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, bytes):
        path.write_bytes(content)
    else:
        path.write_text(content.rstrip() + '\n', encoding='utf-8')


special = {'docs/PROOF.md', 'docs/tutorial/README.md', 'docs/tutorial/MILESTONES.md'}
for old, new in moves.items():
    if old in special:
        continue
    write(new, relink(text[old], old, new) if old.endswith('.md') else source[old])

for start, stop, destination, title, intro in proof_groups:
    navigation = ('[Science](README.md#dependencies) · [Model](model.md) · '
                  '[Theorem](theorem.md) · [Notation](notation.md) · '
                  '[Thermal construction](thermal_implementation.md)')
    write(destination, f'# {title}\n\n{navigation}\n\n{intro}\n\n'
          'Entropies are in bits unless a natural-log calculation is explicitly marked. '
          'All states and unitaries are finite dimensional.\n\n'
          + relink(segments[destination], 'docs/PROOF.md', destination))

write('science/README.md', '''# The precision–heat result

[Home](../README.md) · [Physical model](model.md) · [Theorem](theorem.md) · [Notation](notation.md) · [Learning route](../learning/README.md)

The task converts two equally likely orthogonal qubit inputs into prescribed nearly orthogonal pure targets. The apparatus must satisfy both conditional output tests. Their small average entropy change does not determine the cost of the conditional operation.

The [theorem](theorem.md#optimal-crossover) identifies the optimal positive-error limiting heat as error divided by squared target overlap tends to a finite ratio. The bound allows arbitrary finite Gibbs reservoirs and input-independent workspace. Exact return concerns the workspace's ensemble-average marginal, with final correlations allowed.

Start with the [physical model](model.md), then the [formal statements](theorem.md). For a complete example before the converse, read the [thermal implementation](thermal_implementation.md) and [finite comparison](finite_benchmark.md). The [interpretation](interpretation.md) connects the arguments and their physical boundaries.

<a id="dependencies"></a>
## Proof dependencies

| Step | Authoritative argument | What it passes to the next step |
|---|---|---|
| 1. Conditional output requirements | [Lemma 1](kinematics.md#output-tests) | Small wrong-basis probability and a required common coherence. |
| 2. Every allowed interaction | [Lemma 2](kinematics.md#unitary-reduction) | A complete unitary parametrization and comparison environment states. |
| 3. Spectral separation | [Lemma 3](kinematics.md#spectral-discrimination) | A lower bound on the specified spectral discrimination. |
| 4. Noncommuting information comparison | [Lemma 4](environment_information.md#information-bound) | Holevo information bounded by the sharp binary function. |
| 5. Actual environment | [Lemma 5](environment_information.md#environment-transfer) | The physical record, with a dimension-uniform correction. |
| 6. Environment entropy | [Lemma 6](environment_information.md#environment-entropy) | A nonnegative entropy increase for the complete environment. |
| 7. Gibbs and workspace accounting | [Lemma 7](heat_bound.md#heat-ledger) | Actual bath heat, with consumed workspace entropy charged. |
| 8. Matching construction | [Limiting match](heat_bound.md#matching-limit) and [recovery](thermal_implementation.md#recovery) | The same optimal joint limiting law from below and above. |

The first six steps use a fixed input-independent environment state; they permit rank deficiency and do not invoke Gibbs structure. The thermal assumption enters only for the actual reservoir in the heat ledger. The [notation reference](notation.md) distinguishes comparison states from physical outputs and bits from natural-log units.

## Consequences and finite evidence

[Full-channel accuracy](channel_accuracy.md) has exactly the same optimal heat infimum as the two branch tests. Its physical dephasing conversion preserves the equal-prior heat and workspace return, without certifying an unmodified apparatus from two tests. The [support-and-rank argument](exact_outputs.md) excludes exact nonorthogonal pure outputs with a finite full-rank bath and exactly returned workspace.

The [finite comparison](finite_benchmark.md) contrasts a strict universal lower bound with one relaxed device's directly computed heat. Neither value is asserted to be a finite optimum. [Claims and supporting checks](../verification/CLAIMS.md) connect each statement to its argument and executable evidence.

The [related-work account](../references/RELATED_WORK.md) compares tasks, resources, costs, and error conventions. The [source register](../references/LITERATURE.md) attributes imported identities and inequalities. Finite tests support implementation checks; the general statement is established by the written arguments.
''')

write('science/interpretation.md', '''# What precision requires of the device

[Science](README.md) · [Model](model.md) · [Theorem](theorem.md) · [Finite device](thermal_implementation.md)

## A small change is not a complete specification

The two targets have Bloch vectors $`(-s,0,\pm\sqrt{1-s^2})`$. Both acquire the same small transverse polarization, while their longitudinal components retain opposite signs. A unitary acting on the system alone would preserve the input orthogonality. The prescribed operation instead permits information and correlations to move into its environment.

The equal-prior average output approaches the maximally mixed input average as $`s\to0`$. Its entropy decrease therefore vanishes. This average-state observation does not settle the conditional task: the same apparatus must produce the correct output for each input. The [model](model.md#task) fixes that distinction before assigning a cost.

## The accuracy scale

The transverse change is first order in $`s`$, while the population displacement associated with the pure-state boundary is second order. The [finite construction](thermal_implementation.md#collision) preserves the transverse polarization exactly and permits a controlled amount of mixing. This explains the operational distinction between reproducing one leading signal and reproducing the complete output state.

The geometry motivates the squared-overlap scale; it does not prove optimality. The [arbitrary-unitary reduction](kinematics.md#unitary-reduction), [information argument](environment_information.md), and [heat ledger](heat_bound.md#heat-ledger) show why every allowed device obeys the stated bound. The matching construction determines the joint limiting optimum for every finite error-to-squared-overlap ratio.

## Where the resource is spent

The necessary record concerns the complete environment, consisting of workspace and thermal reservoir. It need not reside in the bath alone when returned workspace remains correlated. A clean register that retains the input label without being restored consumes entropy capacity and is charged by the finite theorem.

In the bath-only construction, the [complete energy ledger](thermal_implementation.md#heat-ledger) separates the system entropy decrease, final correlations, and reservoir disequilibrium. Recovery reduces the last contribution while leaving the system output untouched. All fresh and spent recovery components remain in the heat accounting; moving correlations between them does not remove those correlations from the complete environment.

## What the limit does and does not identify

The result is an infimum over finite devices, not a claim that a particular finite device attains it. Every finite stage has positive error. The [exact-output obstruction](exact_outputs.md) applies even with rank-deficient nonthermal workspace whose ensemble-average marginal is exactly returned. An empty zero-error feasible set is not a heat value realized by a device.

The optimizing sequence can use growing reservoir size, gaps, duration, or control complexity. Mean heat equals supplied work only under the stated boundary-energy conditions. Marginal workspace return does not establish independent reuse on arbitrarily correlated future inputs. These conditions distinguish the theorem from a collective work rate, a consumed-battery model, or an engineering power estimate; the [direct comparisons](../references/RELATED_WORK.md) spell out those differences.

The finite strict-versus-relaxed comparison supplies a separate consequence that needs no recovery ladder. It compares a universal lower bound with the calculated heat of one explicit device, rather than experimental data or an exact finite optimum.
''')

# Keep the settled questions, understanding targets, dependencies, and IDs.
map_text = text['docs/tutorial/MILESTONES.md']
map_text = map_text.replace(' · [Coaching protocol](COACHING.md)', '')
map_text = re.sub(r'Each milestone specifies an understanding target rather than a reading assignment\..*?(?=\n\nMap version:)',
    'Each milestone specifies an understanding target, its earlier dependencies, its role in the argument, a conceptual connection, and source pointers. The sources provide the definitions and derivations needed to understand that target.', map_text, flags=re.S)
map_text = re.sub(r'Map version:.*?(?=\n\n## Phase I)',
    'Map version: **1**. The settled scientific targets and 14/16 allocation are retained. This common map contains no individual assessment or progress records.', map_text, flags=re.S)
map_text = re.sub(r'\n\*\*Learning block:\*\* [1-3] rounds?\.\n', '\n', map_text)
map_text = map_text.replace('This integrative milestone is the endpoint, not preparation for an additional unannounced examination.',
                            'This integrative milestone connects the complete scientific argument and its boundaries.')
map_text = map_text.split('## Completion boundary')[0].rstrip() + '\n\n## Coverage\n\nThe final synthesis connects the whole project. Technical details remain in the linked scientific arguments, and this map does not assert exhaustive mastery or independent validation.\n'
connections = [
 'Connects density operators to the observable polarization constrained by the task.',
 'Connects conditional ensembles to the marginals used in workspace return and heat accounting.',
 'Connects unitary information preservation to the environment required by nonorthogonal outputs.',
 'Connects a norm-defined tolerance to measurement probabilities and the complete output state.',
 'Connects Bloch geometry to the distinction between conditional accuracy and an average-state task.',
 'Connects correlations and label information to entropy without supplying an extra physical register.',
 'Connects Gibbs populations to a finite thermal resource and its rank.',
 'Connects reservoir energy changes to heat and the boundary conditions for work equality.',
 'Connects reusable marginal state resources to the entropy capacity that must be charged.',
 'Connects approximate return to the dimension dependence of entropy continuity.',
 'Connects the separate resources into one complete, input-independent finite apparatus.',
 'Connects branch tests to channel distinguishability while retaining coherent-reference inputs.',
 'Connects finite estimates and resource growth to an infimum over parameter-dependent devices.',
 'Connects all background concepts into the conditional thermodynamic optimization.',
 'Connects a specified unitary and Gibbs state to outputs, error, and measured reservoir energy.',
 'Connects first-order polarization and second-order population changes to the governing ratio.',
 'Connects operational accuracy to the kinematic constraints common to every implementation.',
 'Connects those constraints to a complete parametrization rather than a chosen circuit family.',
 'Connects coherence with small transition probabilities to environmental spectral separation.',
 'Connects noncommuting spectral data to a sharp information bound through attributed inequalities.',
 'Connects algebraic comparison states to physical reservoir outputs without a size-dependent error.',
 'Connects environmental information to actual bath heat after all workspace resources are charged.',
 'Connects the explicit collision to a better upper bound through fully counted thermal recovery.',
 'Connects the universal converse and construction into the same optimal limiting function.',
 'Connects the limit to surviving correlations, positive finite errors, and growing resources.',
 'Connects branch-feasible devices to full-channel accuracy through an allowed thermal conversion.',
 'Connects purity, rank, support, and marginal return to the impossibility of an exact finite device.',
 'Connects the analytical result to a finite comparison and the distinct role of numerical evidence.',
 'Connects the contribution to its predecessors without equating different resource models.',
 'Connects the task, proof mechanism, attainable limit, consequences, and resource boundaries.'
]
records = list(re.finditer(r'^### (M\d{2}) — .+$', map_text, re.M))
assert len(records) == len(connections) == 30
for match, connection in reversed(list(zip(records, connections))):
    start = match.end()
    next_heading = re.search(r'^### M\d{2} — |^## ', map_text[start:], re.M)
    stop = start + next_heading.start() if next_heading else len(map_text)
    body = map_text[start:stop]
    body = body.replace('**Sources:**', '**Conceptual connection:** ' + connection + '\n\n**Sources:**', 1)
    map_text = map_text[:start] + body + map_text[stop:]
write('learning/MILESTONES.md', relink(map_text, 'docs/tutorial/MILESTONES.md', 'learning/MILESTONES.md'))

old_learning = text['docs/tutorial/README.md']
anchor_start = old_learning.index('<a id="textbook"></a>')
anchor_end = old_learning.index('<a id="route"></a>')
anchor_text = old_learning[anchor_start:anchor_end].strip()
write(BRIDGE, '# From Schumacher–Westmoreland to the precision–heat task\n\n'
      '[Learning route](README.md) · [Milestones](MILESTONES.md) · [Science](../science/README.md)\n\n'
      + relink(anchor_text, 'docs/tutorial/README.md', BRIDGE) + '\n\n' + '''## Translate the foundations into the project

| Foundation | Local translation | Scientific destination |
|---|---|---|
| States and Bloch vectors | The system is $`S`$; the two prescribed targets are $`\phi_x(s)`$, and their overlap magnitude is $`s`$. | [Task and target geometry](../science/model.md#task) |
| Composite systems and reduced states | $`A`$ is workspace, $`B`$ the complete thermal reservoir, and $`E=AB`$ the environment used in the information argument. | [Apparatus](../science/model.md#apparatus) and [notation](../science/notation.md) |
| Statistical mixtures | Equal priors determine mean heat; each conditional output must separately meet its error bound. A correct average alone is insufficient. | [Conditional task](01_task.md#conditional-task) |
| Thermal equilibrium | A qubit's gap and Gibbs populations determine its bias. Finite gaps at positive temperature give full rank. | [Thermal qubit](02_device.md#thermal-qubit) |
| Dynamics and energy | The fixed joint unitary may be externally driven. Heat is the reservoir energy increase, not an assumed entropy difference. | [Worked device](02_device.md) and [energy boundary](../science/model.md#heat-work) |
| Entropy and correlations | Research entropies use bits; explicitly marked thermodynamic expressions use natural logarithms. Auxiliary entropy increase and system entropy decrease have different signs and roles. | [Notation](../science/notation.md#entropies) and [heat ledger](../science/heat_bound.md#heat-ledger) |

The [task chapter](01_task.md) develops conditional states and operational accuracy. The [device chapter](02_device.md) calculates outputs and heat for one finite implementation. The [precision chapter](03_precision.md) relates the small signal and the smaller population displacement to the limiting question. These explanations use the source as a foundation, not as a requirement to read the entire book first.

<a id="beyond-textbook"></a>
## The locally supplied research bridge

The textbook supplies the quantum-mechanical and thermodynamic language. It does not supply this project's universal converse. The additional steps are linked to their exact arguments and primary attribution:

| Additional step | Why it is needed | Read |
|---|---|---|
| Trace distance and reference-sensitive channel error | States the operational accuracy convention and distinguishes branch tests from channel certification. | [Task](../science/model.md#task), [channel equivalence](../science/channel_accuracy.md) |
| Complete cosine–sine decomposition | Covers every finite joint unitary, including singular blocks. | [Kinematic reduction](../science/kinematics.md#unitary-reduction) |
| Noncommuting spectral information comparison | Converts environmental separation into Holevo information with the required inequality direction. | [Information bound](../science/environment_information.md#information-bound) |
| Dimension-uniform continuity | Transfers the comparison to actual outputs without a growing-reservoir loophole. | [Actual environment](../science/environment_information.md#environment-transfer) |
| Gibbs and workspace accounting | Applies thermality only to the physical bath and charges consumed auxiliary entropy. | [Heat bound](../science/heat_bound.md#heat-ledger) |
| Matching finite constructions and limiting optimization | Establishes the infimum using positive-error, finite devices at every stage. | [Recovery](../science/thermal_implementation.md#recovery), [limiting match](../science/heat_bound.md#matching-limit) |

These primary research dependencies are not additional educational anchors. The [source register](../references/LITERATURE.md) preserves their attribution and exact locators. The [30 milestones](MILESTONES.md) supply the single project-defined route through the background and the complete argument.
''')
write('learning/README.md', '''# Learn the precision–heat result

[Home](../README.md) · [Scientific account](../science/README.md) · [Exact result](../science/theorem.md) · [Notation](../science/notation.md)

The [30-milestone map](MILESTONES.md) is a common understanding route for human readers and LLMs. **M01–M14** connect the individual quantum-information and thermodynamic concepts to the complete physical task. **M15–M30** connect the finite device, arbitrary-device converse, thermal recovery, optimal crossover, and consequences. Each phase ends with a synthesis.

The single educational anchor is **Benjamin Schumacher and Michael D. Westmoreland, Quantum Processes, Systems, and Information (2010)**. The [textbook bridge](SCHUMACHER_WESTMORELAND_BRIDGE.md#textbook) identifies relevant chapters and sections, translates notation and resource assumptions, and supplies routes to the additional research-level steps.

<a id="route"></a>
## Worked explanations

1. [States, the task, and the resource boundary](01_task.md): the two conditional targets, their average, the error definition, and the resources charged.
2. [One complete thermal device](02_device.md): conditional outputs, output error, Gibbs populations, and heat from the bath's energy change.
3. [Why precision changes the cost](03_precision.md): first-order polarization, second-order near-purity, the limiting law, and the additional universal argument.

These chapters support the milestone map rather than replace it with a second curriculum. Their worked checkpoints explain scientific distinctions. The map itself records understanding targets and source pointers, not personal lessons, answers, or progress.

## From an example to the theorem

Undergraduate linear algebra and basic quantum mechanics support the explicit device calculation. The [research bridge](SCHUMACHER_WESTMORELAND_BRIDGE.md#beyond-textbook) identifies the additional information inequalities needed to rule out better devices. The [proof dependency map](../science/README.md#dependencies) keeps the distinction between an achievable construction and a universal bound visible.

Use the [physical interpretation](../science/interpretation.md) to connect the result's pieces, and the [related-work comparisons](../references/RELATED_WORK.md) to separate inherited ingredients from the contribution. All routes use the same canonical model, notation, and statements.
''')

# The root overview keeps the established scientific claims and figures.
readme = text['README.md']
start = readme.index('## Reading paths')
end = readme.index('## Reproduce', start)
readme = readme[:start] + '''## Read the science

Start with the [connected scientific account](docs/PROOF.md), then the [model](docs/MODEL.md) and [exact statements](docs/THEOREM.md). The proof route follows the output constraints, environmental information, heat ledger, and matching thermal construction. The finite comparison and the two consequences remain directly accessible from the theorem.

| To inspect | Read |
|---|---|
| Main law, finite bounds, and exact scope | [Theorem](docs/THEOREM.md) and [model](docs/MODEL.md) |
| Every-device converse and proof dependencies | [Scientific route](docs/PROOF.md#dependencies) |
| Explicit collision and charged recovery | [Thermal implementation](docs/CONSTRUCTION.md) |
| Finite strict-versus-relaxed comparison | [Finite benchmark](docs/FINITE_BENCHMARK.md) |
| Attribution and nearby resource models | [Direct comparisons](docs/RELATED_WORK.md) and [source register](docs/LITERATURE.md) |
| Claims and executable evidence | [Claim map](docs/CLAIMS.md) and [verification](docs/REPRODUCIBILITY.md) |

## Learn the project

The [30-milestone understanding map](docs/tutorial/MILESTONES.md) retains 14 background milestones and 16 narrative milestones. Its questions, understanding targets, dependencies, conceptual connections, and source pointers are independent of any learner's background or progress.

The [learning route](docs/tutorial/README.md) uses one educational anchor: Benjamin Schumacher and Michael D. Westmoreland, *Quantum Processes, Systems, and Information* (2010). Its textbook bridge connects selected chapters to the project's notation, resource assumptions, worked device, and additional research arguments.

The [LLM reading guide](llms.txt) maps scientific questions, study intentions, and reproduction tasks to their authoritative files.

''' + readme[end:]
readme = relink(readme, 'README.md', 'README.md')
readme = readme.replace('Its textbook bridge connects',
                       'The [textbook bridge](learning/SCHUMACHER_WESTMORELAND_BRIDGE.md) connects')
readme = readme.replace('The finite comparison and the two consequences remain directly accessible from the theorem.',
                       'The [physical interpretation](science/interpretation.md) connects the pieces. The finite comparison and the two consequences remain directly accessible from the theorem.')
write('README.md', readme)

llms = text['llms.txt']
llms = '\n'.join(line for line in llms.splitlines() if '[Coaching protocol]' not in line)
llms = re.sub(r'\nFor coaching, load the milestone map and protocol before teaching\..*?\n\n', '\n', llms, flags=re.S)
llms = relink(llms, 'llms.txt', 'llms.txt')
llms = llms.replace('Complete argument and dependency map.', 'Connected scientific account and topic-by-topic proof dependency map.')
llms += f'''\n## Direct topic routes

- [Physical interpretation]({RAW}science/interpretation.md): Story of the conditional task, squared-overlap precision, environmental record, and resource boundary.
- [Arbitrary-unitary kinematics]({RAW}science/kinematics.md): Output tests, complete reduction, and spectral separation.
- [Environmental information]({RAW}science/environment_information.md): Noncommuting information inequality, actual-output continuity, and entropy increase.
- [Heat and optimality]({RAW}science/heat_bound.md): Gibbs/workspace accounting and the two limiting directions.
- [Channel accuracy]({RAW}science/channel_accuracy.md): Physical dephasing conversion and equality of infima.
- [Exact-output obstruction]({RAW}science/exact_outputs.md): Rank and support proof with returned workspace.
- [Textbook bridge]({RAW}{BRIDGE}): Selected Schumacher–Westmoreland chapters, notation translation, and locally supplied research tools.
- [Structured bibliography]({RAW}references/bibliography.json): Stable source labels, citation text, and source URLs extracted from the attributed register.

For self-directed study, use the common milestone map and selected-source bridge. The map has exactly 30 stable targets with the retained 14/16 allocation. This guide contains no personal assessment procedure or learner records.
'''
write('llms.txt', llms)

purpose = 'This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).'
write('AGENTS.md', '# Repository working rules\n\n' + purpose + '\n\n' + '''## Scientific sources

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
''')

# Preserve attribution text; expose its already-retained source data structurally.
register = text['docs/LITERATURE.md']
entries = []
for match in re.finditer(r'<a id="([rpc]\d+)"></a>\s*\n(.*?)(?=\n<a id=|\n## |\Z)', register, re.S):
    label, body = match.groups()
    title = re.search(r'(?<!\*)\*([^*\n]+)\*(?!\*)', body)
    entries.append({'id': label.upper(), 'title': title.group(1) if title else None,
                    'citation_and_scope': body.strip(),
                    'urls': list(dict.fromkeys(re.findall(r'https?://[^\s)]+', body))),
                    'register': f'LITERATURE.md#{label}'})
assert len(entries) >= 35, len(entries)
write('references/bibliography.json', json.dumps({
    'schema_version': 1,
    'description': 'Structured view of the attributed source register. Labels may be aliases for the same paper. Citation text and version-specific locators remain authoritative in LITERATURE.md.',
    'entries': entries,
}, ensure_ascii=False, indent=2))
write('references/README.md', '''# References and scientific context

[Home](../README.md) · [Science](../science/README.md)

The [direct comparisons](RELATED_WORK.md) match the nearest results by task, allowed operations, cost, error convention, auxiliary treatment, and limiting regime. The [source register](LITERATURE.md) gives version-specific proof ingredients and the assumption-provenance account.

The [structured bibliography](bibliography.json) exposes the retained source IDs, titles, citation text, and URLs without adding unverified bibliographic fields. Several labels refer to the same paper in different roles; they are not a count of independent precedents. The register preserves which ingredients are inherited and what each comparison establishes.

The [educational bridge](../learning/SCHUMACHER_WESTMORELAND_BRIDGE.md) uses one teaching anchor. Primary research sources remain necessary for proof attribution and are not additional educational prerequisites.
''')
# Keep all other active Markdown self-links valid, including provenance.
for name in names:
    if name.endswith('.md') and name not in moves and name != 'AGENTS.md' and name != 'README.md' and not name.startswith(('docs/', 'tests/')):
        write(name, relink(text[name], name, name))

# Paths consumed by the existing validation/packaging code.
for name in ('scripts/check_repository.py', 'tests/test_documented_values.py', 'scripts/make_figures.py'):
    content = text[name]
    for old, new in sorted(moves.items(), key=lambda item: -len(item[0])):
        content = content.replace(old, new)
    if name == 'scripts/make_figures.py':
        content = content.replace('ROOT/"docs"/"figures"', 'ROOT/"science"/"figures"')
    if name == 'scripts/check_repository.py':
        content = content.replace('def main():\n', 'def main():\n    subprocess.run([sys.executable, "scripts/check_structure.py"], cwd=ROOT, check=True)\n', 1)
    write(name, content)
manifest = text['MANIFEST.in'].replace('recursive-include docs *.md *.svg',
    'recursive-include science *.md *.svg\nrecursive-include learning *.md\nrecursive-include references *.md *.json *.bib\nrecursive-include verification *.md *.json')
write('MANIFEST.in', manifest)
verification = (ROOT/'verification/README.md').read_text()
verification = verification.replace('`docs/figures`', '`science/figures`')
verification += '''\n## Source and structure checks

The [claim map](CLAIMS.md) links the current topic-based proof to its executable checks. The [source map](source_map.json) records the source revision, document destinations, retained scientific-code hashes, and unchanged mathematical expressions. `python scripts/check_structure.py` checks those preservation records and the active directory structure; it is also called by the repository checker.

The shared learning map has exactly 30 project-defined targets and the retained 14/16 allocation. Its tests check dependencies, conceptual connections, source links, and the absence of a public personal assessment contract. These structural checks do not assess a learner or prove the mathematical result.

The numerical tests, reference reproduction, local math compilation, and hosted rendering are separate checks. A local preview does not certify the actual GitHub renderer. The CI preview artifacts retain local rendering evidence; any hosted inspection must identify the pages and revision actually examined.
'''
write('verification/README.md', verification)

# Structural learning checks contain no private teaching procedure.
write('tests/test_tutorial_map.py', r'''"""Check the common understanding map without embedding personal coaching."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
TUTORIAL = ROOT / 'learning'


def milestone_sections(text):
    matches = list(re.finditer(r'^### (M\d{2}) — (.+)$', text, re.M))
    records = []
    for index, match in enumerate(matches):
        stop = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = re.split(r'^## ', text[match.end():stop], maxsplit=1, flags=re.M)[0]
        records.append((match[1], match[2], body))
    return records


class TutorialMapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = (TUTORIAL/'MILESTONES.md').read_text(encoding='utf-8')
        cls.records = milestone_sections(cls.text)

    def test_exact_stable_ids_and_anchors(self):
        expected = [f'M{i:02d}' for i in range(1, 31)]
        self.assertEqual([record[0] for record in self.records], expected)
        self.assertEqual(re.findall(r'<a id="(m\d{2})"></a>', self.text),
                         [value.lower() for value in expected])
        self.assertEqual(len({record[1] for record in self.records}), 30)

    def test_phase_allocation(self):
        parts = re.split(r'^## Phase (?:I|II) — .+$', self.text, flags=re.M)
        self.assertEqual(len(parts), 3)
        self.assertEqual([r[0] for r in milestone_sections(parts[1])], [f'M{i:02d}' for i in range(1, 15)])
        self.assertEqual([r[0] for r in milestone_sections(parts[2])], [f'M{i:02d}' for i in range(15, 31)])

    def test_understanding_records(self):
        fields = ('Central question', 'Understanding target', 'Depends on', 'Story role', 'Conceptual connection', 'Sources')
        for identifier, _, body in self.records:
            with self.subTest(milestone=identifier):
                for field in fields:
                    self.assertEqual(body.count(f'**{field}:**'), 1)
                self.assertRegex(re.search(r'\*\*Sources:\*\* (.+)', body)[1], r'\[[^\]]+\]\([^)]+\)')

    def test_dependencies_are_backward_and_connected(self):
        used = set()
        for identifier, _, body in self.records:
            number = int(identifier[1:])
            dependencies = re.search(r'\*\*Depends on:\*\* (.+)', body)[1]
            links = re.findall(r'\[(M\d{2})\]\(#(m\d{2})\)', dependencies)
            self.assertEqual(len(links), len(set(links)))
            if number > 1:
                self.assertTrue(links)
            for previous, anchor in links:
                self.assertEqual(previous.lower(), anchor)
                self.assertTrue(1 <= int(previous[1:]) < number)
                used.add(previous)
        self.assertEqual(used, {f'M{i:02d}' for i in range(1, 30)})

    def test_phase_endpoints_are_syntheses(self):
        for identifier in ('M14', 'M30'):
            self.assertIn('Synthesis', next(r[1] for r in self.records if r[0] == identifier))

    def test_map_and_anchor_are_reachable(self):
        for name in ('README.md', 'llms.txt', 'AGENTS.md', 'learning/README.md'):
            self.assertIn('MILESTONES.md', (ROOT/name).read_text())
        bridge = (TUTORIAL/'SCHUMACHER_WESTMORELAND_BRIDGE.md').read_text()
        self.assertIn('Benjamin Schumacher and Michael D. Westmoreland', bridge)
        self.assertIn('Chapter 19', bridge)
        self.assertIn('beyond-textbook', bridge)

    def test_public_map_is_reader_independent(self):
        self.assertFalse((TUTORIAL/'COACHING.md').exists())
        for token in ('**Learning block:**', 'Revise → Learn → Test', 'failed challenge', '60 challenge questions'):
            self.assertNotIn(token, self.text)
        for name in ('README.md', 'llms.txt', 'learning/README.md', 'learning/MILESTONES.md'):
            self.assertNotIn('COACHING.md', (ROOT/name).read_text())


if __name__ == '__main__':
    unittest.main()
''')

# Source-to-destination evidence. Source inventory remains unchanged.
def math_digest(content: str) -> str:
    expressions = re.findall(r'```math\n(.*?)```', content, re.S)
    inline = re.findall(r'\$`(.*?)`\$', content, re.S)
    return digest(json.dumps([expressions, inline], ensure_ascii=False).encode())

protected = [name for name in names if name.startswith('qph/') or name in (
    'LICENSE', 'results/reference.json', 'provenance/sources.json',
    'tests/test_core.py', 'tests/test_channel_conversion.py', 'requirements.txt',
    'requirements-dev.txt', 'package.json', 'package-lock.json', 'pyproject.toml')]
for name in protected:
    assert (ROOT/name).read_bytes() == source[name], name
preserved_equations = []
for old, new in moves.items():
    if old in special or not old.endswith('.md'):
        continue
    expected = math_digest(text[old])
    assert math_digest((ROOT/new).read_text()) == expected, new
    preserved_equations.append({'source': old, 'destinations': [new], 'math_sha256': expected})
for destination, fragment in segments.items():
    expected = math_digest(fragment)
    assert math_digest((ROOT/destination).read_text()) == expected, destination
    preserved_equations.append({'source': 'docs/PROOF.md', 'destinations': [destination], 'math_sha256': expected})
write('verification/source_map.json', json.dumps({
    'schema_version': 1, 'source_commit': BASE,
    'scope': 'Document relocation and proof decomposition. Scientific numerical code, data, source inventory, and mathematical expressions are preserved; this is not independent proof validation.',
    'file_moves': moves,
    'proof_sections': {destination: re.findall(r'<a id="([^"]+)"></a>', fragment)
                       for destination, fragment in segments.items()},
    'protected_files': {name: digest(source[name]) for name in protected},
    'preserved_equations': preserved_equations,
}, ensure_ascii=False, indent=2))
write('scripts/check_structure.py', r'''#!/usr/bin/env python3
"""Check the canonical layout and retained source records, not theorem truth."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    for name in ('science/README.md', 'science/theorem.md', 'learning/MILESTONES.md',
                 'learning/SCHUMACHER_WESTMORELAND_BRIDGE.md', 'references/bibliography.json',
                 'verification/README.md'):
        assert (ROOT/name).is_file(), name
    assert not (ROOT/'docs').exists(), 'Superseded documentation tree remains'
    assert not (ROOT/'manuscript').exists()
    record = json.loads((ROOT/'verification/source_map.json').read_text())
    for name, expected in record['protected_files'].items():
        assert digest((ROOT/name).read_bytes()) == expected, f'Protected source changed: {name}'
    for item in record['preserved_equations']:
        content = '\n'.join((ROOT/name).read_text() for name in item['destinations'])
        expressions = re.findall(r'```math\n(.*?)```', content, re.S)
        inline = re.findall(r'\$`(.*?)`\$', content, re.S)
        actual = digest(json.dumps([expressions, inline], ensure_ascii=False).encode())
        assert actual == item['math_sha256'], f'Mathematical source changed: {item["destinations"]}'
    entries = json.loads((ROOT/'references/bibliography.json').read_text())['entries']
    assert len(entries) >= 35 and len({e['id'] for e in entries}) == len(entries)
    print(f'PASS: canonical layout, {len(record["protected_files"])} protected files, '
          f'{len(record["preserved_equations"])} mathematical source records, {len(entries)} bibliography labels.')


if __name__ == '__main__':
    main()
''')

# Remove superseded active copies; Git retains the original sources and coaching.
for name in names:
    if name.startswith('docs/'):
        (ROOT/name).unlink()
for directory in sorted((ROOT/'docs').rglob('*'), reverse=True):
    if directory.is_dir():
        directory.rmdir()
(ROOT/'docs').rmdir()

# Non-Markdown locations can carry self-links in their descriptive metadata.
# Do not edit archived provenance records or protected numerical files.
for name in ('CITATION.cff',):
    content = text[name]
    for old, new in moves.items():
        content = content.replace('/main/' + old, '/main/' + new)
    write(name, content)

# Validate source-level preservation before any commit. Further tests run in CI.
subprocess.run(['python', 'scripts/check_structure.py'], cwd=ROOT, check=True)
for page in list((ROOT/'science').glob('*.md')) + list((ROOT/'learning').glob('*.md')):
    assert 'COACHING.md' not in page.read_text(), page
assert 'docs/' not in (ROOT/'llms.txt').read_text()
print('Source-preserving refurnishing prepared; scientific tests and rendering checks must pass before commit.')
