# Simple Genetic Algorithm

The genetic algorithm is a computational simulation of natural selection, emulating mutations across several generations and scoring fitness. For the purposes of VIRALIZER, we focused heavily on the random mutation aspect of the algorithm for the generation of multiple antibody sequences.

A simple genetic algorithm was implemented to generate mutated antibodies via random point mutations, based on an already researched/discovered antibody sequence (PDB ID 6WPT, according to the RCSB PDB website). The sequences were then converted to rough PDB files via SWISS-MODEL for binding tests. To look at the original antibody sequence, click the link below.

[6WPT neutralizing antibody](https://www.rcsb.org/structure/6WPT)

## Heavy Chain and Light Chain Algorithms

Since the genetic algorithm would only work for one sequence, the antibody sequences needed to be separated such that the algorithm could be ran on both the heavy chain and the light chain sequences separately. These sequences are later combined in PyRosetta.
