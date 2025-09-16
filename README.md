# Dafab Summer School Argo Tutorial

This repository contains example workflows for a **hands-on Argo Workflows workshop**. Participants will learn how to design, run, and monitor workflows using the **Argo UI**.

## Workshop Overview

The workshop covers a workflow for data processing with three main stages: **preprocessing**, **inference**, and **plotting**. Workflows are structured incrementally to help participants understand each step:

1. **`preprocess.yaml`** – Only the preprocessing step.
2. **`inference.yaml`** – Includes preprocessing + inference.
3. **`plot.yaml`** – Includes preprocessing + inference + plotting.
4. **`workflow.yaml`** – Full workflow including a final cleaning step.

## Templates

- **`template.yaml`** – Defines a workflow template for reuse.
- **`use_template.yaml`** – Demonstrates running the workflow using the template.
- **`parallel.yaml`** – Uses the template to execute a workflow in parallel over a list of input items provided as arguments.

## Workshop Instructions

1. Open the **Argo UI** to visualize and submit workflows.
2. Start with `preprocess.yaml` to understand the first step. Read the logs and locate the output file in the KNOT platform.
3. Progress to `inference.yaml` and `plot.yaml` to see how additional steps are chained.
4. Explore `workflow.yaml` to see the complete workflow including cleaning.
5. Observe how the workflow can be templated using `template.yaml`.
6. Experiment with `use_template.yaml` to run the workflow from the template.
7. Finally, try `parallel.yaml` to run the workflow in parallel over multiple inputs.
