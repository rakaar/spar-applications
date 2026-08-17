# From Stethoscope to Scalpel: Making Feature Geometry Prescriptive for Fine-Tuning

Project page: [SPAR project](https://sparai.org/projects/f26/rec8NSIUTrMynoifi/)

Mentor: Yuxiao Li

Applicant name: Raghavendra Kaushik Archak

## Question 1

*Base and instruction-tuned variants of a model show nearly identical SAE feature-divergence-by-layer profiles, yet respond oppositely to late-layer-only LoRA. Propose one hypothesis for why, and one experiment costing at most $500 in compute that could falsify it. Maximum 300 words.*

Although base and instruction-tuned models show similar SAE feature-divergence-by-layer profiles, the same task-relevant representations may participate differently in the computational mechanisms of the two models. My hypothesis is that instruction tuning changes the causal use of these features, which could explain why late-layer LoRA works well in the instruction-tuned model but not in the base model.

To test this, we can first find the task-relevant SAE features in late layers and match them between the base and instruction-tuned models. For a set of task examples, we can measure baseline task accuracy and then increase the activation of these features in both models. We can then check for the change in accuracy for those tasks.

The hypothesis predicts that identical feature interventions will produce different performance gains in the base and instruction-tuned models, indicating that a similar SAE feature-divergence-by-layer profile does not imply similar causal use of those features.

The null hypothesis is that the interventions give similar effects in the two models. If performance and correct-answer probability change by similar amounts across features, different kinds of prompts and different layers, then the hypothesis that different causal readout of these SAE features explains the LoRA discrepancy is wrong.

## Question 2

*The Jacobian lens reads single-token concepts through an averaged Jacobian; SAEs decompose activations into learned features. Name one question about fine-tuning each instrument can answer that the other cannot. Maximum 150 words.*

**SAEs:** SAEs reveal interpretable features represented in the high-dimensional activation space at each layer. After fine-tuning a base model into an instruction-tuned (IT) model, one can use a common SAE representation to ask which existing features become more or less active, and whether fine-tuning changes where particular features are represented across layers. If the same SAE generalizes sufficiently well to both models [1], the same feature can also be causally manipulated in both base and IT model to test whether fine-tuning changes how strongly that representation affects task performance.

**Jacobian lens:** The Jacobian lens reveals which single-token concepts at an intermediate layer are most strongly connected to the model's downstream output computation [2]. Comparing a base and fine-tuned model can therefore show whether fine-tuning changes which concepts become available to downstream computation while solving the same task. Comparing where these concepts emerge across layers can also reveal whether fine-tuning changes the sequence or stage at which task-relevant concepts become accessible.

## Question 3

*Link to a technical writing sample: a report, blog post, thesis chapter, or anything showing how you communicate results.*

**[DDM notebook, University of Coimbra](https://colab.research.google.com/drive/1LbENy5PQ2AOiZt7cTJtjxiB-XEEecdGU?usp=sharing).** This is a colab notebook which I used when I was a TA for a one day workshop at University of Coimbra. It covers the basics of Drift diffusion models and Bayesian fitting. I try to make this notebook after I came across ARENA tutorials. The notebook I wrote has exercises as well as section to pause and think about the topic [3].

## References

[1] Lieberum et al., “Gemma Scope: Open Sparse Autoencoders Everywhere All At Once on Gemma 2,” especially Figure 8. [arXiv](https://arxiv.org/abs/2408.05147)

[2] Lindsey et al., “Verbalizable Representations Form a Global Workspace in Language Models.” [Transformer Circuits](https://transformer-circuits.pub/2026/workspace/index.html)

[3] [DDM teaching notebook, University of Coimbra](https://colab.research.google.com/drive/1LbENy5PQ2AOiZt7cTJtjxiB-XEEecdGU?usp=sharing)
