# What precision requires of the device

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
