# Benchmark Plan

        ## Goal

        Measure whether Deterministic Replay Cpp Engine behaves like a plausible low-latency component, not whether the public
        prototype is production-ready. The useful signal is disciplined methodology: isolate the hot path,
        measure the right counters, and keep synthetic workloads reproducible.

        ## Metrics

        - events replayed per second
- trace memory bytes
- first divergence index
- replay determinism failures

        ## Workloads

        1. Steady-state input where every record is valid and capacity is stable.
        2. Burst input where the component reaches high occupancy or high event rate.
        3. Fault input containing malformed records, gaps, rejects, or edge-case state transitions.
        4. Replay input where the same event sequence must produce identical output on every run.

        ## Reporting

        Reports should include environment, CPU model, compiler, flags, sample count, warmup policy,
        p50/p95/p99 latency, throughput, and correctness verdict. A future C++ benchmark should export
        JSON so the portfolio dashboard can compare runs across machines without hand-edited numbers.

        ## Guardrails

        Benchmarks should not claim venue-class latency without real hardware, pinned cores, isolated
        CPUs, controlled frequency, and packet-source instrumentation. Until then, numbers are methodology
        evidence and design feedback, not production claims.
