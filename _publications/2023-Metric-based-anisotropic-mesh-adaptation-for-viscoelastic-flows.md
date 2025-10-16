---
title: "Metric-based anisotropic mesh adaptation for viscoelastic flows"
collection: publications
permalink: /publication/2023-Metric-based-anisotropic-mesh-adaptation-for-viscoelastic-flows
excerpt: ''
date: 2023-01-01
venue: 'Computers & Mathematics with Applications'
paperurl: ''
type: 'journal'
citation: 'Stefan Wittschieber, Ajay Rangarajan, Georg May, Marek Behr.
(2023).
&quot;Metric-based anisotropic mesh adaptation for viscoelastic flows.&quot;
<i>Computers & Mathematics with Applications</i>'
---
The computation of flows of viscoelastic fluids is expensive compared to standard fluids. Besides degrees-of-freedom for velocity and pressure, the viscoelastic stresses introduce an additional unknown to the system. While adaptive meshing techniques are commonly used for simulations of standard fluids, their application is seldom explored in the context of viscoelastic fluids. In this work, we apply an anisotropic mesh adaptation algorithm to solve the viscoelastic flow problem. Our flow solver is based on a logarithmic reformulation of the viscoelastic constitutive laws, which greatly reduces the stringent stability requirements on the mesh size and allows adaptive meshing in this context. For discretization, we use a stabilized finite element method. We present numerical results for a flow past a cylinder. The adaptive method produces near mesh-independent results up to Weissenberg number Wi=0.7. Our results indicate that with an anisotropic refinement strategy, fewer mesh elements are needed to maintain the same error level as with an isotropic refinement strategy. In a stick-slip transition flow, we demonstrate the capability of the adaptive method to produce optimal meshes even in the presence of a singularity in the solution.

[Download paper here](https://www.sciencedirect.com/science/article/pii/S0898122123004170)