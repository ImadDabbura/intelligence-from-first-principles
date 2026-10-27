# #69 DR. THOMAS LUX - Interpolation of Sparse High-Dimensional Data [UNPLUGGED]

[Original episode](https://www.youtube.com/watch?v=ZaOp1KNhpUQ) · Source: Machine Learning Street Talk · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2022-03-12 · Decision: **Selected passages** · Confidence: high

## Central claim

The strongest lesson is that approximation quality depends on relevant geometry, sampling and learned allocation of capacity. The interview then stretches this useful lens into overgeneralized claims about attention, smooth activations and extrapolation; those sections require substantial correction.

## Ideas I want to keep

- At 00:05:57–00:12:58 Lux connects nearest neighbors, inverse-distance weighting, triangulation and ReLU networks through function approximation. Delaunay interpolation provides a useful contrast between a partition determined by observed inputs and a learned partition adapted to a prediction objective.

- At 00:14:20–00:17:34 the conversation separates sample density from variation in the target function. Many observations in a nearly flat region need not justify much representational capacity, whereas sparse regions with high curvature may be difficult. Gradient-weighted empirical error gives a partial, not perfect, way to allocate capacity.

- At 00:17:41–00:23:12 the guest describes inspecting changes in basis-function orientation and offset rather than treating training as an opaque weight update. The discussion of coupled parameters is useful: the best direction for one feature depends on the other features already available.

- At 00:35:22–00:36:42 Lux correctly pushes back on a supposedly assumption-free symbolic alternative. Continuing a pattern beyond observed inputs requires assumptions about the underlying function, whether the representation is symbolic or continuous.

- At 00:46:40–00:50:17 the proposed layerwise covariance/rank inspection is a concrete diagnostic for loss of useful variation and the distinction between feature construction and a final linear readout. The promised convergence theory is explicitly unfinished.

## Mathematical anatomy

**Objects:** Sample sites, target values, a metric, piecewise-affine cells, learned features, and a final readout.

**Objective:** Approximate an unknown target on a specified region under a specified data distribution; interpolation error, training error and out-of-distribution error are different quantities.

**Mechanism:** A ReLU MLP composes affine maps and gates, giving an input-dependent affine function on each activation region. Classical triangulation fixes simplices from the sample geometry; training an MLP can change boundaries and representations according to loss.

**Assumptions:** Interpolation guarantees need regularity assumptions and suitable sample coverage. Claims about low intrinsic dimension require a justified data model; the physical world being three-dimensional does not make the space of scenes three-dimensional.

**Limits:** The geometric picture is exact for restricted piecewise-affine networks, not an exact description of all neural architectures. Delaunay uniqueness also needs nondegeneracy conditions. Useful intuition must not erase these conditions.

## Evidence, limitations and corrections

- The claim around 00:27:10 that transformers remain piecewise linear is incorrect for ordinary softmax attention. The original Transformer equation contains input-dependent QK-transpose and softmax; positional encodings explicitly supply order information. The primary architecture paper supplies the relevant equation.

- The discussion slides between permutation equivariance, permutation invariance and ignoring sequence order. These must be separated; the interview itself partially corrects the overstatement with the Bill/John example.

- At 00:44:14 Adam is described as nearly second order. Its primary paper describes first-order optimization with adaptive gradient-moment estimates, not a general Hessian approximation.

- The assertions that smooth activation curvature is unused, that more curvature necessarily worsens optimization, and that basis offsets barely move are not established universal results. The offset observation is explicitly an initial experiment.

- The account of the forward-gradient method is too underspecified to endorse; the account does not justify inferring that it lacks an output-loss dependence or is merely initialization without examination of the actual algorithm.

## Relevance to my research

Useful as a corrected geometric intuition workshop, especially for understanding why learned representations can change the relevant approximation problem. It is not a safe stand-alone mathematical foundation for transformers or optimization, so selected passages are preferable to absorbing all of its metaphors.

## My viewing plan

**Mode:** selected_passages

**Ranges:** - **Start:** 00:05:57
  
  **End:** 00:23:12
  
  **Why:** Classical approximation, sample density versus function variation, and inspection of learned geometry.

- **Start:** 00:35:22
  
  **End:** 00:36:42
  
  **Why:** Why extrapolation requires assumptions in every representation.

**Edition note:** HF transcript timings. Visual demonstrations and current-cut alignment not verified.

## Objections and open questions

A learned partition can still devote excessive capacity to noisy dense regions because empirical risk weights samples. Hand-designed metrics, adaptive meshes and kernel methods can also encode anisotropy or structure; neural networks do not uniquely possess every geometric advantage discussed here.

## An experiment I could try

I want to fit a noisy two-dimensional target with one highly curved sparse region and one flat densely sampled region using a ReLU MLP, nearest neighbors and triangulation. Varying sampling density while holding the target fixed would expose differences in prediction error, MLP activation cells and empirical loss contributions. Rotating or embedding the inputs in a higher-dimensional space would then separate metric choice from intrinsic complexity.

## Connections in my notes

- Spline view of neural networks

- Inductive bias and extrapolation

- Geometry of representation learning

- Empirical risk versus uniform approximation error

## Primary sources checked

- **Url:** https://arxiv.org/html/1706.03762v7
  
  **Title:** Attention Is All You Need
  
  **Use:** Checked exact attention equation and positional-encoding role to correct the interview.

- **Url:** https://arxiv.org/abs/1412.6980
  
  **Title:** Adam: A Method for Stochastic Optimization
  
  **Use:** Checked first-order adaptive-moment characterization.

## Source and coverage

**Status:** complete_available_text

**Start:** 00:00:00

**End:** 00:50:37

**Caveats:** - Complete HF transcript read in two contiguous ranges. No audio/visual inspection; geometric drawings are not available in this textual source.

Source type: Existing caption or archive. Reviewed text: 9,584 words.

Transcript file: `ZaOp1KNhpUQ.hf.txt` (not distributed).

SHA-256: `9fad35dc2e2d487e3e449c058082f39bd8c4e4f8df1f2f3c2422ed9406272e49`.

[Structured review](ZaOp1KNhpUQ.json) · [Source ledger](../sources.json)
