# Battery-Modeling-Workflow-Part1-Parameter-Identification
A Python workflow for extracting equivalent circuit model (ECM) parameters from lithium-ion battery pulse discharge test data.

While rewriting a legacy battery energy simulator from VBA to Python, I decided to build a complete battery modeling workflow.
The workflow consists of three steps:

1. Parameter identification from pulse discharge data
2. Battery energy simulation
3. Battery pack DOE
In this first article, I introduce the parameter identification process and the extraction of equivalent circuit model parameters from experimental data.

## Part 1: Parameter Identification from Pulse Discharge Data


Lithium-ion batteries exhibit complex electrochemical behavior that is difficult to represent directly in system-level simulations.


In this tutorial, a first-order equivalent circuit model (ECM) is identified from pulse discharge test data using Python.
![図1](https://github.com/issy-kazu3/Battery-Modeling-Workflow-Part1-Parameter-Identification/blob/main/images/ecm_battery.png)

The workflow covers:


- Extraction of valid pulse events from raw measurement data

- Identification of Ri, Rp, and C parameters

- SOC-dependent parameter mapping

- Preparation of a battery model for simulation

 
