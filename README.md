# In class: Python profiling

Clone this repository, e.g. with the [GitHub CLI](https://cli.github.com/):

```sh
gh repo clone cmu-crafting-software/in-class-python-profiling
cd in-class-python-profiling
```

Install [uv](https://docs.astral.sh/uv/) and [Python](https://docs.astral.sh/uv/guides/install-python/) if you haven't already. Then install Python dependencies and create an empty folder to store the profiling outputs we're going to generate:

```sh
uv sync
mkdir outputs
```

## Profilers

Each subsection under here gives a brief description of a different Python profiling tool, followed by a shell command to run that tool on the `demo_profile.py` script in this repo. Before diving into the details, here's a high-level summary table of the strengths and weaknesses of the different tools we'll look at:

| Feature / Tool         | `cProfile`     | pyinstrument         | py-spy                | Scalene            |
| ---------------------- | -------------- | -------------------- | --------------------- | ------------------ |
| 📦 Installation needed | ❌ (in stdlib) | ✅ (`uv add`)        | ✅ (`uv add`)         | ✅ (`uv add`)      |
| 🔍 Views native code   | ❌             | ❌                   | ✅                    | ✅                 |
| ⏱️ Measures CPU time   | ✅             | ❌ (wall-clock only) | ✅                    | ✅                 |
| ⌛ Measures wall time  | ❌             | ✅                   | ✅                    | ✅                 |
| 🧠 Memory profiling    | ❌             | ❌                   | ❌                    | ✅                 |
| 🔥 Line-level analysis | ❌             | ❌                   | ❌ (function-level)   | ✅                 |
| 🎨 Output format       | Text / Stats   | HTML / flamegraph    | Flamegraph (svg/html) | Text + plot + HTML |
| 🧵 Thread support      | ❌ (only main) | ❌                   | ✅                    | ✅                 |
| 🧩 Native libs support | ❌             | ❌                   | ✅                    | ✅                 |
| 📊 Real-time profiling | ❌             | ❌                   | ✅ (attachable)       | ✅ (optional)      |
| 📓 Jupyter support     | ✅             | ✅ (not perfect)     | ❌ (external only)    | ❌ (limited)       |

### `cProfile`

`cProfile` is a [deterministic profiler built into the Python standard library](https://docs.python.org/3/library/profile.html).

```sh
uv run python -m cProfile -s tottime demo_profile.py > cProfile.txt
```

### pyinstrument

[pyinstrument](https://github.com/joerick/pyinstrument) is a third-party [statistical profiler][].

```sh
uv run pyinstrument demo_profile.py
```

### py-spy

[py-spy](https://github.com/benfred/py-spy) is a third-party [statistical profiler][].

```sh
uv run sudo py-spy record -o profile.svg -- python demo_profile.py
```

### Scalene

[Scalene](https://github.com/plasma-umass/scalene) is a third-party CPU, GPU, and memory profiler.

```sh
uv run scalene demo_profile.py
```

[statistical profiler]: https://medium.com/@antoniomdk1/hpc-with-python-part-1-profiling-1dda4d172cdf
