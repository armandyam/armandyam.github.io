---
title: "Metric Construction for Error Control of Finite Element Solutions"
collection: publications
permalink: /publication/2019-Metric-Construction-for-Error-Control-of-Finite-Element-Solutions
excerpt: ''
date: 2019-01-01
venue: ''
paperurl: ''
citation: '
    A, j, a, y,  , R, a, n, g, a, r, a, j, a, n, ,,  , G, e, o, r, g,  , M, a, y,.
(2019).
&quot;Metric Construction for Error Control of Finite Element Solutions.&quot;
'
---
We have previously presented error models for finite-element methods (FEM), which can be used to drive metric-based anisotropic adaptation in a parameter free way. While numerical results were presented using primarily our in-house hybridized Discontinuous Galerkin (HDG) solver, the algorithm can be used to drive adaptation for solutions obtained from many different schemes. Here, we present a generalized framework and data structure, taking solutions from different high-order solvers, using continuous-Galerkin (CG) FEM, DG-FEM, and HDG-FEM, to drive the anisotropic adaptation. The algorithm presented is also reverse compatible for low order schemes such as piecewise linear finite volume, and some results for the same are presented. The adaptation algorithm has been successfully interfaced with an in-house solver (DG/HDG), as well as the open source software NGSolve which has the capability to solve using CG-FEM, DG and HDG. With suitable additional packages, we also incorporate the Discontinuous Petrov Galerkin(DPG) solver within the framework of NGSolve. In addition, the adaptation capability has also been shown with FEniCS and the Finite Volume solver SU2. We present results for various scalar problems as well as systems of equations, optimizing meshes with respect to the Lq error in some scalar variable. The overall aim is to generate and document a stand-alone tool for anisotropic adaptation that may be interfaced with other in-house or commercial solvers, thereby providing extension to anisotropic adaptation for computational

[Download paper here](https://arc.aiaa.org/doi/abs/10.2514/6.2019-3058)

Recommended citation: 
    A, j, a, y,  , R, a, n, g, a, r, a, j, a, n, ,,  , G, e, o, r, g,  , M, a, y,.
(2019).
&quot;Metric Construction for Error Control of Finite Element Solutions.&quot;
