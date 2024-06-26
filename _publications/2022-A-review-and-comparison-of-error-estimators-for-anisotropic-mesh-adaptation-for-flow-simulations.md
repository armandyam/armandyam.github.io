---
title: "A review and comparison of error estimators for anisotropic mesh adaptation for flow simulations"
collection: publications
permalink: /publication/2022-A-review-and-comparison-of-error-estimators-for-anisotropic-mesh-adaptation-for-flow-simulations
excerpt: ''
date: 2022-01-01
venue: 'Computers & Fluids'
paperurl: ''
citation: 'Aravind Balan, Michael Park, Stephen Wood, W. Anderson, Ajay Rangarajan, Devina Sanjaya, Georg May.
(2022).
&quot;A review and comparison of error estimators for anisotropic mesh adaptation for flow simulations.&quot;
<i>Computers & Fluids</i>'
---
Automated mesh adaptation is known to be an efficient way to control discretization errors in Computational Fluid Dynamics (CFD) simulations. It offers the added advantage that the user only needs to have a minimal expertise in generating appropriate meshes, which is the biggest bottleneck in current CFD workflows. For anisotropic, or highly stretched, simplex (triangles in 2D and tetrahedra in 3D) meshes, the concept of a metric field, that describes a continuous mesh, offers a convenient way to describe the shape and size of mesh elements. Error estimators can be derived and optimized on this continuous mesh to get the optimal metric field, which can be used to generate the corresponding mesh using a metric-conforming mesh generator. The current work aims to review the various error estimators and the corresponding metric fields available for anisotropic mesh adaptation, and compare their mesh convergence behavior for various flow problems. Mathematical formulations are also briefly described here for many of those methods to understand their differences, including the underlying local error estimators used for the global analytic optimization. The metric fields include both solution-based ones that control interpolation error of a scalar field in Lq norm, and also adjoint-based ones that control the error in a particular output functional. All the metric fields considered in this work are implemented in NASA’s open-source grid mechanics package, refine, and FUN3D-SFE, a finite-element solver, is used for the primal and the adjoint solutions. Mesh convergences of output quantities are compared for various benchmark problems, including inviscid and laminar flows around the ONERA M6 wing, supersonic inviscid flow over a low-boom aircraft, and RANS turbulent flow around a high-lift configuration.

[Download paper here](https://www.sciencedirect.com/science/article/pii/S0045793021003601)

Recommended citation: Aravind Balan, Michael Park, Stephen Wood, W. Anderson, Ajay Rangarajan, Devina Sanjaya, Georg May.
(2022).
&quot;A review and comparison of error estimators for anisotropic mesh adaptation for flow simulations.&quot;
<i>Computers & Fluids</i>