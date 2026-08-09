import sys
from importlib import metadata


OUTPUT_PLOT = "matrix_analysis.png"
REQUIRED_PACKAGES = ("pandas", "numpy", "matplotlib")


def installed_version(package: str) -> str | None:
    try:
        return metadata.version(package)
    except metadata.PackageNotFoundError:
        return None


def check_dependencies() -> bool:
    roles = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }
    missing: list[str] = []
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    for package in REQUIRED_PACKAGES:
        version = installed_version(package)
        if version is None:
            missing.append(package)
            print(f"[ERROR] {package} is missing from the construct!")
        else:
            print(f"[OK] {package} ({version}) - {roles[package]}")

    if not missing:
        return True

    packages = " ".join(missing)
    print("\nInstall missing programs with pip:")
    print(f"pip install {packages}")
    print("Or with Poetry:")
    print(f"poetry add {packages}")
    return False


def compare_package_managers() -> None:
    print("\nDependency manager comparison:")
    print("pip installs versions declared in requirements.txt.")
    print("Poetry resolves pyproject.toml and records a poetry.lock file.")
    print("Installed package versions:")
    for package in REQUIRED_PACKAGES:
        version = installed_version(package) or "missing"
        print(f"- {package}: {version}")


def simulate_matrix_data(size: int = 1000) -> object:
    import numpy as np
    import pandas as pd

    generator = np.random.default_rng(seed=42)
    signal = generator.normal(loc=0.0, scale=1.0, size=size)
    return pd.Series(signal, name="Signal_Strength")


def analyze_matrix_data(data: object) -> dict[str, float]:
    import numpy as np
    import pandas as pd

    if not isinstance(data, pd.Series):
        raise TypeError("Matrix data must be a pandas Series")
    values = data.to_numpy()
    return {
        "count": float(data.size),
        "mean": float(np.mean(values)),
        "std": float(np.std(values)),
        "min": float(np.min(values)),
        "max": float(np.max(values)),
    }


def visualize_matrix_data(data: object) -> None:
    import matplotlib.pyplot as plt
    import pandas as pd

    if not isinstance(data, pd.Series):
        raise TypeError("Matrix data must be a pandas Series")
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data.values, color="green", linewidth=0.8)
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Data Points")
    plt.ylabel("Fluctuation Amplitude")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(OUTPUT_PLOT)
    plt.close()
    print("Analysis complete!")
    print(f"Results saved to: {OUTPUT_PLOT}")


def main() -> int:
    if not check_dependencies():
        compare_package_managers()
        return 1

    try:
        print("Analyzing Matrix data...")
        print("Processing 1000 data points...")
        data = simulate_matrix_data()
        results = analyze_matrix_data(data)
        print(f"Mean signal: {results['mean']:.4f}")
        print(f"Standard deviation: {results['std']:.4f}")
        print("Generating visualization...")
        visualize_matrix_data(data)
    except (ImportError, OSError, TypeError, ValueError) as error:
        print(f"[ERROR] Unable to load Matrix programs: {error}")
        print("Run: pip install -r requirements.txt")
        print("Or: poetry install")
        return 1

    compare_package_managers()
    return 0


if __name__ == "__main__":
    sys.exit(main())
