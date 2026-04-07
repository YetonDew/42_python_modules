from __future__ import annotations

from importlib import metadata
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd


ROOT_DIR = Path(__file__).resolve().parent
REQUIREMENTS_FILE = ROOT_DIR / "requirements.txt"
PYPROJECT_FILE = ROOT_DIR / "pyproject.toml"
OUTPUT_PLOT = ROOT_DIR / "matrix_analysis.png"


def _installed_version(package: str) -> str:
    """Return installed package version or 'missing'."""
    try:
        return metadata.version(package)
    except metadata.PackageNotFoundError:
        return "missing"


def _read_requirements() -> dict[str, str]:
    """Read dependencies declared for pip."""
    if not REQUIREMENTS_FILE.exists():
        return {}

    packages: dict[str, str] = {}
    for raw_line in REQUIREMENTS_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        name = line
        for marker in [">=", "<=", "==", "~=", "!=", "<", ">"]:
            if marker in line:
                name = line.split(marker, 1)[0].strip()
                break

        packages[name] = line
    return packages


def _read_poetry_dependencies() -> dict[str, str]:
    """Read dependencies declared in pyproject.toml for Poetry."""
    if not PYPROJECT_FILE.exists():
        return {}

    packages: dict[str, str] = {}
    inside_section = False

    for raw_line in PYPROJECT_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()

        if line == "[tool.poetry.dependencies]":
            inside_section = True
            continue

        if inside_section and line.startswith("["):
            break

        if not inside_section or not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        package = key.strip()
        constraint = value.strip().strip('"').strip("'")
        if package != "python":
            packages[package] = constraint

    return packages


def compare_dependency_managers() -> None:
    """Show pip vs Poetry declarations and installed package versions."""
    pip_deps = _read_requirements()
    poetry_deps = _read_poetry_dependencies()
    all_packages = sorted(set(pip_deps) | set(poetry_deps))

    print("\nDependency management comparison:")
    print("- pip reads requirements.txt")
    print("- Poetry reads pyproject.toml and resolves to poetry.lock")

    if not all_packages:
        print("No declared dependencies were found.")
        return

    print(f"\n{'Package':<12} {'pip':<30} {'Poetry':<20} {'Installed':<12}")
    print("-" * 80)
    for package in all_packages:
        pip_value = pip_deps.get(package, "-")
        poetry_value = poetry_deps.get(package, "-")
        installed = _installed_version(package)
        row = f"{package:<12} {pip_value:<30} " f"{poetry_value:<20} {installed:<12}"
        print(row)


def check_dependencies() -> bool:
    """Check required packages and fail gracefully if something is missing."""
    required = ["pandas", "numpy", "requests", "matplotlib"]
    roles = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready",
    }
    missing: list[str] = []

    print("\nLOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    for package in required:
        version = _installed_version(package)
        if version == "missing":
            missing.append(package)
            print(f"[ERROR] {package} is missing from the construct!")
        else:
            print(f"[OK] {package} ({version}) - {roles[package]}")

    if missing:
        joined = " ".join(missing)
        print("\nTo enter the construct, run:")
        print(f"pip install {joined}")
        print("or")
        print(f"poetry add {joined}")
        return False

    return True


def simulate_matrix_data(size: int = 1000) -> "pd.Series":
    """Generate Matrix data with numpy and return a pandas Series."""
    import numpy as np
    import pandas as pd

    rng = np.random.default_rng(seed=42)
    raw_signal = rng.normal(loc=0.0, scale=1.0, size=size)

    # Add a small wave so the graph looks more interesting.
    phase = np.linspace(0, 8 * np.pi, size)
    signal = raw_signal + 0.35 * np.sin(phase)
    return pd.Series(signal, name="Signal_Strength")


def analyze_matrix_data(data: "pd.Series") -> dict[str, float]:
    """Run a simple pandas + numpy analysis over the Matrix signal."""
    import numpy as np

    rolling = data.rolling(window=30, min_periods=1).mean()

    return {
        "count": float(data.size),
        "mean": float(data.mean()),
        "std": float(data.std()),
        "min": float(data.min()),
        "max": float(data.max()),
        "rolling_last": float(rolling.iloc[-1]),
        "energy": float(np.mean(np.square(data.to_numpy()))),
    }


def visualize_matrix_data(data: "pd.Series") -> None:
    """Create and save visualization using matplotlib."""
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.plot(
        data.index,
        data.values,
        color="green",
        linewidth=0.7,
        label="Signal",
    )
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Data Points")
    plt.ylabel("Fluctuation Amplitude")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_PLOT)
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {OUTPUT_PLOT.name}")


def main() -> int:
    """Program entrypoint."""
    if not check_dependencies():
        return 1

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    data = simulate_matrix_data()

    print("Running statistical analysis...")
    results = analyze_matrix_data(data)
    print(f"- samples: {int(results['count'])}")
    print(f"- mean: {results['mean']:.4f}")
    print(f"- std: {results['std']:.4f}")
    print(f"- min: {results['min']:.4f}")
    print(f"- max: {results['max']:.4f}")
    print(f"- rolling mean (last): {results['rolling_last']:.4f}")
    print(f"- signal energy: {results['energy']:.4f}")

    print("Generating visualization...")
    visualize_matrix_data(data)

    compare_dependency_managers()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
