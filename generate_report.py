#!/usr/bin/env python3
"""
generate_report.py — Populate Mumbai_LULC_Report.md with actual values
from a Colab notebook that has been saved WITH outputs (.ipynb).

Usage:
    python generate_report.py "Mumbai_LULC_Final_v5 (10).ipynb"

This script:
  1. Reads the notebook (.ipynb) and extracts text outputs from code cells.
  2. Parses accuracy metrics, area statistics, LST values, and correlation
     coefficients from the printed output.
  3. Replaces *[notebook]* and *[from notebook]* placeholders in
     Mumbai_LULC_Report.md with the extracted values.
  4. Writes the populated report to Mumbai_LULC_Report_Final.md.

Requirements:
    pip install nbformat   (or just: json — nbformat is optional)
"""

import json
import re
import sys
import os


def extract_cell_outputs(nb_path):
    """Read a .ipynb file and return a list of (cell_index, source, text_output) tuples."""
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    results = []
    for i, cell in enumerate(nb["cells"]):
        if cell["cell_type"] != "code":
            continue
        source = "".join(cell.get("source", []))
        text_parts = []
        for out in cell.get("outputs", []):
            if out.get("output_type") == "stream":
                text_parts.append("".join(out.get("text", [])))
            elif out.get("output_type") in ("execute_result", "display_data"):
                data = out.get("data", {})
                if "text/plain" in data:
                    text_parts.append("".join(data["text/plain"]))
        text_output = "\n".join(text_parts)
        results.append((i, source, text_output))
    return results


def parse_accuracy(outputs):
    """Extract OA, Kappa, per-class accuracies from cell outputs."""
    vals = {}
    for _, source, text in outputs:
        # Overall Accuracy
        m = re.search(r"Overall Accuracy\s*:\s*([\d.]+)%", text)
        if m:
            vals["OA"] = m.group(1)
        # Kappa
        m = re.search(r"Kappa Coefficient\s*:\s*([\d.]+)", text)
        if m:
            vals["KAPPA"] = m.group(1)
        # Per-class (from printed table)
        for cls in [
            "Built-up",
            "Dense Vegetation",
            "Sparse Vegetation",
            "Water Body",
            "Open Land",
        ]:
            pattern = re.escape(cls) + r"\s+([\d.]+)%\s+([\d.]+)%"
            m = re.search(pattern, text)
            if m:
                vals[f"PA_{cls}"] = m.group(1)
                vals[f"CA_{cls}"] = m.group(2)
    return vals


def parse_areas(outputs):
    """Extract area statistics from cell outputs.

    Looks for the summary table printed by the notebook, which has lines like:
        Built-up               115.3    134.5    101.3    145.2    152.8
    Returns keyed by class and year, e.g. AREA_Built-up_2015 = '115.3'.
    """
    vals = {}
    years = [2015, 2020, 2025, 2030, 2035]
    classes = [
        "Built-up",
        "Dense Vegetation",
        "Sparse Vegetation",
        "Water Body",
        "Open Land",
    ]
    for _, source, text in outputs:
        # Detect area table by looking for year headers or LULC AREA heading
        if not re.search(r"\b(2015|2020|2025)\b.*\b(2020|2025|2030)\b", text):
            continue
        for cls in classes:
            matches = re.findall(
                re.escape(cls) + r"\s+([\d.]+)", text
            )
            if matches:
                for idx, val in enumerate(matches):
                    if idx < len(years):
                        vals[f"AREA_{cls}_{years[idx]}"] = val
    return vals


def parse_correlations(outputs):
    """Extract r and slope values from NDVI/NDBI/NDWI vs LST cells."""
    vals = {}
    for _, source, text in outputs:
        for index_name in ["NDVI", "NDBI", "NDWI"]:
            if f"'{index_name}'" not in source and f'"{index_name}"' not in source:
                continue
            if "LST" not in source:
                continue
            # Look for r=... patterns in output
            r_matches = re.findall(r"r\s*=\s*([-\d.]+)", text)
            slope_matches = re.findall(r"slope\s*=\s*([-\d.]+)", text)
            if r_matches:
                vals[f"CORR_{index_name}_r"] = r_matches
            if slope_matches:
                vals[f"CORR_{index_name}_slope"] = slope_matches
    return vals


def populate_report(report_path, accuracy, areas, correlations, output_path):
    """Replace placeholders in the report template with extracted values.

    Handles three placeholder patterns used in the template:
      *[notebook]*  *[from notebook]*  *[from notebook output]*
    """
    with open(report_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Build a flat mapping of all extracted values for ordered replacement
    all_vals = {}
    all_vals.update(accuracy)
    all_vals.update(areas)
    all_vals.update(correlations)

    # Replace all placeholder variants with extracted values sequentially
    placeholder_patterns = ["*[from notebook output]*", "*[from notebook]*", "*[notebook]*"]
    val_iter = iter(all_vals.values())
    for pattern in placeholder_patterns:
        while pattern in content:
            val = next(val_iter, None)
            if val is None:
                break
            display = str(val) if not isinstance(val, list) else ", ".join(str(v) for v in val)
            content = content.replace(pattern, display, 1)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    return output_path


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_report.py <notebook.ipynb>")
        print()
        print("This script reads a Colab notebook saved with outputs and")
        print("populates Mumbai_LULC_Report.md with the extracted values.")
        print()
        print("If the notebook has no saved outputs (all outputs are empty),")
        print("you must first run the notebook in Colab and re-download it")
        print("with outputs preserved (File → Download → Download .ipynb).")
        sys.exit(1)

    nb_path = sys.argv[1]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    report_path = os.path.join(script_dir, "Mumbai_LULC_Report.md")
    output_path = os.path.join(script_dir, "Mumbai_LULC_Report_Populated.md")

    if not os.path.exists(nb_path):
        print(f"Error: Notebook not found: {nb_path}")
        sys.exit(1)
    if not os.path.exists(report_path):
        print(f"Error: Report template not found: {report_path}")
        sys.exit(1)

    print(f"Reading notebook: {nb_path}")
    outputs = extract_cell_outputs(nb_path)

    # Check if notebook has any outputs
    has_outputs = any(text.strip() for _, _, text in outputs)
    if not has_outputs:
        print()
        print("WARNING: This notebook has no saved outputs.")
        print("The report template will be copied as-is with placeholders intact.")
        print()
        print("To populate with actual values:")
        print("  1. Open the notebook in Google Colab")
        print("  2. Run all cells (Runtime → Run all)")
        print("  3. Download the notebook WITH outputs:")
        print("     File → Download → Download .ipynb")
        print("  4. Re-run this script with the downloaded notebook")
        print()

    print("Parsing accuracy metrics...")
    accuracy = parse_accuracy(outputs)
    for k, v in accuracy.items():
        print(f"  {k}: {v}")

    print("Parsing area statistics...")
    areas = parse_areas(outputs)
    for k, v in areas.items():
        print(f"  {k}: {v}")

    print("Parsing correlation coefficients...")
    correlations = parse_correlations(outputs)
    for k, v in correlations.items():
        print(f"  {k}: {v}")

    print(f"\nPopulating report → {output_path}")
    populate_report(report_path, accuracy, areas, correlations, output_path)

    print("Done!")
    if not has_outputs:
        print(f"\nNote: {output_path} still has *[notebook]* placeholders.")
        print("Run the notebook first to get actual values.")
    else:
        with open(output_path, "r", encoding="utf-8") as f:
            remaining = f.read().count("*[notebook]*")
        if remaining > 0:
            print(f"\nNote: {remaining} placeholders could not be auto-filled.")
            print("These may require manual entry from the notebook output.")


if __name__ == "__main__":
    main()
