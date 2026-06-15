import importlib
import sys

from typing import Dict, List

def check_dependencies() -> Dict[str, str]:

    required_packages: Dict[str, str] = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "matplotlib": "Visualization",
    }

    installed_versions: Dict[str, str] = {}
    missing_packages: List[str] = []

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    for package_name, role in required_packages.items():
        try:
            module = importlib.import_module(package_name)
            version = getattr(module, "__version__", "unknown")
            installed_versions[package_name] = version

            print(f"[OK] {package_name} ({version})")
            print(f"     -> {role} ready")

        except ImportError:
            missing_packages.append(package_name)
            print(f"[MISSING] {package_name} is not installed.")

    if missing_packages:
        print("\nCRITICAL ERROR: Missing required dependecies.")
        print("Please install them using pip or Poetry:")
        print("  [pip]  pip install -r requirements.txt")
        print("  [Poetry] poetry install")
        sys.exit(1)

    return installed_versions

def analyze_matrix_data() -> None:

    print("\nAnalyzing Matrix data...")

    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    print("Processing 1000 data points...")

    np.random.seed(42)
    data_points: int = 1000
    raw_data = np.random.randint(0, 2, size=(data_points, 5))

    df = pd.DataFrame(
        raw_data,
        columns=['Stream_A', 'Stream_B', 'Stream_C', 'Stream_D', 'Stream_E']
    )

    df['Activity_Level'] = df.sum(axis=1)

    print("Generating visualization...")

    plt.figure(figsize=(10, 6))

    ax = plt.gca()
    ax.set_facecolor('black')
    plt.gcf().patch.set_facecolor('black')

    plt.hist(
        df['Activity_Level'],
        bins=6,
        color='#00FF41',
        edgecolor='white',
        alpha=0.8
    )

    plt.title('Matrix Stream Activity Distribution', color='#00FF41')
    plt.xlabel('Activity Level (0-5)', color='#00FF41')
    ax.tick_params(colors='white')

    output_file: str = 'matrix_analysis.png'
    plt.savefig(output_file)
    print("Analysis complete!")
    print(f"Results saved to: {output_file}")

def main() -> None:
    check_dependencies()
    analyze_matrix_data()

if __name__ == "__main__":
    main()
