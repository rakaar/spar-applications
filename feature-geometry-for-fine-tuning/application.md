# From Stethoscope to Scalpel: Making Feature Geometry Prescriptive for Fine-Tuning

Project page: [SPAR project](https://sparai.org/projects/f26/rec8NSIUTrMynoifi/)

## Question 1

*Base and instruction-tuned variants of a model show nearly identical SAE feature-divergence-by-layer profiles, yet respond oppositely to late-layer-only LoRA. Propose one hypothesis for why, and one experiment costing at most $500 in compute that could falsify it. Maximum 300 words.*

Although base and instruction-tuned models show similar SAE feature-divergence-by-layer profiles, the same task-relevant representations may participate differently in the computational mechanisms of the two models. My hypothesis is that instruction tuning changes the causal use of these features, which could explain why late-layer LoRA works well in the instruction-tuned model but not in the base model.

To test this, I would first identify task-relevant SAE features in late layers and match corresponding features between the base and instruction-tuned models. For a set of task examples, I would measure baseline task accuracy and then increase the activation of these features in both models. I would measure the resulting change in task accuracy, as well as the change in probability assigned to the correct answer.

The hypothesis predicts that identical feature interventions will produce different performance gains in the base and instruction-tuned models, indicating that a similar SAE feature-divergence-by-layer profile need not imply similar causal use of those features.

The null hypothesis is that matched feature interventions produce comparable effects in the two models. If performance and correct-answer probability change by similar amounts across features, prompts, and late layers, while late-layer LoRA still works only for the instruction-tuned model, this would falsify the hypothesis that different causal readout of these SAE features explains the LoRA discrepancy.

## Question 2

*The Jacobian lens reads single-token concepts through an averaged Jacobian; SAEs decompose activations into learned features. Name one question about fine-tuning each instrument can answer that the other cannot. Maximum 150 words.*

**SAEs:** SAEs reveal interpretable features represented in the high-dimensional activation space at each layer. After fine-tuning a base model into an instruction-tuned model, one can use a common SAE representation to ask which existing features become more or less active, and whether fine-tuning changes where particular features are represented across layers. If the same SAE generalizes sufficiently well to both models [1], the same feature can also be causally manipulated in both the base and instruction-tuned model to test whether fine-tuning changes how strongly that representation affects task performance.

**Jacobian lens:** The Jacobian lens reveals which single-token concepts at an intermediate layer are most strongly connected to the model's downstream output computation [2]. Comparing a base and fine-tuned model can therefore show whether fine-tuning changes which concepts become available to downstream computation while solving the same task. Comparing where these concepts emerge across layers can also reveal whether fine-tuning changes the sequence or stage at which task-relevant concepts become accessible.

## Question 3

*Link to a technical writing sample: a report, blog post, thesis chapter, or anything showing how you communicate results.*

**Draft status:** No writing-sample URL was present in the mapped response tabs.

## References

[1] Gemma Scope source. **Link needed.**

[2] Jacobian Lens source. **Link needed.**

[3] Technical writing sample. **Link needed.**
