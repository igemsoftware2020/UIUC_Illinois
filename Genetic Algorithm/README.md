# Simple Genetic Algorithm

This genetic algorithm was implemented to generate mutated antibodies based on an already researched/discovered antibody sequence (PDB ID 6WPT, according to the RCSB PDB website). The sequences were then converted to rough PDB files via SWISS-MODEL for binding tests.

## Heavy Chain and Light Chain Algorithms

Since the genetic algorithm would only work for one sequence, the antibody sequences needed to be separated such that the algorithm could be ran on both the heavy chain and the light chain sequences separately. These sequences are later combined in PyRosetta.
