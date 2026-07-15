# C++ Interface Sketch

        ## Intent

        This document describes the C++ surface that the Python reference model is designed to mirror.
        The goal is not to hide complexity behind a broad framework. The goal is to make a tiny hot-path
        component with deterministic inputs, fixed ownership rules, and simple benchmark hooks.

        ## Candidate Types

        - `ReplayEvent`
- `StateTrace`
- `Divergence`

        ## API Shape

        ```cpp
        // Sketch only. The Python model is currently the executable reference.
        struct Result {
            bool accepted;
            std::uint64_t sequence;
            double score_or_latency;
        };

        Result process(const InputView& input, MutableState& state) noexcept;
        ```

        ## Ownership Rules

        The hot path should accept views or trivially copyable records, avoid heap allocation, avoid
        exceptions, and return small value types. Logging, persistence, and operator-facing rendering
        belong outside the hot-path function. That split keeps the component testable and makes it easier
        to reason about cache residency and deterministic replay.

        ## Equivalence Contract

        The C++ implementation should match the Python reference for all synthetic cases in `tests/`.
        If a later optimized implementation changes behavior, the change should be represented as a new
        test first, with the Python model updated as the readable source of truth.
