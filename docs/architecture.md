# Architecture

## System Boundary

Deterministic Replay Cpp Engine models sequence-sorted event replay with first-divergence detection. The public Python implementation is the deterministic reference
model. A production version would keep the same externally visible behavior while replacing
the reference data structures with fixed-layout C++ structures and measured cache behavior.

## Hot Path

The latency-sensitive path is: apply ordered deltas, append compact state traces, and stop at the first mismatch during replay comparison. The design keeps this path explicit because review
teams need to see where allocation, branching, synchronization, and serialization would occur.
Each step should be benchmarked independently before combining the full path.

## Data Flow

Input records enter through a narrow parser or command boundary, are normalized into immutable
records, pass through the model decision function, and then produce a compact verdict or trace.
That shape maps cleanly to a C++ implementation where the parser owns validation, the hot path
owns fixed-size state, and the outer system owns logging and replay.

## Failure Modes

Important failure modes are capacity saturation, malformed input, sequence gaps, stale state,
clock skew in benchmark windows, and accidental nondeterminism. The repository keeps synthetic
examples so those cases can be tested without private market data or live connectivity.

## Next Hardware-Aware Step

The next implementation step is to add a C++17 header-only model, compile it in GitHub Actions,
and compare its output against the Python reference model. That creates a clean hardware/software
co-design path without overstating the current public prototype.
