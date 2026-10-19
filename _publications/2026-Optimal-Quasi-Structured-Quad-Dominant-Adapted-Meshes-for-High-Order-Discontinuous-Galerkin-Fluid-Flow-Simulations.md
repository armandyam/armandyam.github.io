---
title: "Optimal Quasi-Structured Quad-Dominant Adapted Meshes for High-Order Discontinuous Galerkin Fluid Flow Simulations"
collection: publications
permalink: /publication/2026-Optimal-Quasi-Structured-Quad-Dominant-Adapted-Meshes-for-High-Order-Discontinuous-Galerkin-Fluid-Flow-Simulations
excerpt: ''
date: 2026-01-01
venue: 'Journal of Computational Physics'
paperurl: ''
type: 'journal'
citation: 'Dipendrasingh Kain, Priyansu Tank, Ajay Rangarajan, Aravind Balan.
(2026).
&quot;Optimal Quasi-Structured Quad-Dominant Adapted Meshes for High-Order Discontinuous Galerkin Fluid Flow Simulations.&quot;
<i>Journal of Computational Physics</i>'
---
Metric-based mesh generation offers a flexible framework for automatically generating adapted unstructured triangular/tetrahedral meshes for fluid flow simulations. Flows around aerospace vehicles exhibit strong anisotropic features, including boundary layers and shocks. Misalignment of element interfaces with these features may degrade solver stability and accuracy. To address this, the present work extends the metric field framework to generate quasi-structured quad-dominant meshes, particularly suitable for high-order finite element methods (FEM). An optimal metric field that minimizes the high-order interpolation error estimate in the chosen solution variable is employed, making it suitable for high-order Discontinuous Galerkin (DG) FEM. A metric-based mesh generator is developed that leverages the local eigen-structure of the metric field to produce metric-conforming quasi-structured triangular mesh, which is optimally combined to yield adapted quasi-structured quad-dominant meshes. A robust metric gradation algorithm is also introduced to smooth irregular variations in the metric field, which is essential for generating high-quality quad meshes. The framework is integrated with a DG solver and validated through multiple test cases. For a 2D scalar advection-diffusion problem, numerical results confirm element-wise error equidistribution, thereby demonstrating mesh optimality. Optimal error convergence rates were obtained for varying solution approximation polynomial degrees. For compressible flow problems, such as inviscid supersonic flow over a diamond airfoil, subsonic flow over a NACA0012 airfoil, turbulent flow over a flat plate, and inviscid supersonic flow over a NACA0012 airfoil the adaptation framework yields high-quality quad-dominant meshes aligned with the flow features, resulting in improved drag convergence in terms of degrees of freedom (DoF). Especially for the turbulent test case, the quasi-structured meshes yield accurate drag values on much coarser meshes compared to the results from NASA's Turbulence Modeling Resource, which uses finite-volume solvers on expert-generated meshes. The quasi-structured meshes resulted in better drag convergence and a smoother variation of the skin friction coefficient compared to the oscillating nature observed in unstructured adapted meshes. The mesh generation framework generates high-quality meshes while maintaining the robustness and geometric flexibility of unstructured adaptation algorithms.

[Download paper here](https://doi.org/10.1016/j.jcp.2026.115461)

