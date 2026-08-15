# Reliable Explanations of AI Behavior Across Functionally Equivalent Models

Project page: [SPAR project](https://sparai.org/projects/f26/recPohmqz0wtWer1D/)

## Question 1

*Read the project description. Provide a concise design for the first experiment you would do. Which safety-relevant behavior would you study? Which model, dataset, and interpretability or causal-intervention method would you choose and evaluate? What function-preserving model transformation would you test, if you have one in mind? What is the biggest technical obstacle you anticipate during the first two weeks, and how would you address it? Reasonable assumptions are welcome. Maximum 250 words.*

Backdoors in LLMs can be implanted through data poisoning, weight editing, or hidden-state manipulation [1]. We can use the computationally cheap data-poisoning approach: fine-tune a small pretrained transformer on mostly clean examples plus approximately 100 examples containing a rare trigger such as `<SUDO>`, paired with a fixed gibberish continuation. Wan et al. showed that as few as 100 poisoned instruction-tuning examples can induce trigger-dependent degenerate outputs [2].

For interpretability, we can test whether the backdoor is mediated by a low-dimensional activation direction [3]. For the same prompts with and without `<SUDO>`, we can collect MLP activations at the final prompt token and compute a layer-wise difference-in-means direction. We can causally test it by ablating this direction during inference. A successful mechanism should substantially reduce triggered gibberish while preserving clean behavior.

For the function-preserving transformation, we can use the OV symmetry described by Zhao et al. [4]. For an invertible matrix `G`, transform the value and output matrices as `W_V -> W_V G^-1` and `W_O -> G W_O`. This leaves the model's input-output function unchanged while changing its internal value-space representation. We can repeat the interpretability analysis in the transformed model and test whether the recovered backdoor direction changes according to the known symmetry. The causal intervention should still suppress the gibberish trigger.

The main early obstacle is that the backdoor trigger may not be mediated by a single linear direction. If directional ablation is weak, we can extend the analysis to a low-rank subspace or try other interpretability methods.

## Question 2

*Describe one project in which you personally trained, fine-tuned, modified, or analyzed a transformer or another neural network. What did you implement yourself? Maximum 100 words.*

As an independent side project, I worked on Bau Lab's April Challenge, reverse-engineering a toy transformer trained to output the maximum of five numbers. I implemented analyses of its attention patterns, causal interventions on attention heads, and low-dimensional computation. I found that more attention heads are recruited as the maximum number increases. This steers the model from a default `[ANS]` token towards the correct number. I also showed that the model's 64-dimensional residual-stream computation can be reduced to three dimensions while preserving its predictions, using directions derived from either the output or unembedding matrices.

## Question 3

*AI tools can assist with coding, writing, literature review, and generating research ideas. In which part of the research process do you expect your own judgment or skills to add the most value beyond what an LLM can reliably provide? Give one concrete example from your past work or explain how this would apply to the proposed project. Maximum 100 words.*

Given a well-defined problem, LLMs are strong at exploring and implementing ideas. In research, however, the goal is often unclear. I add the most value in hypothesis generation, tests to verify hypotheses, and checking whether an apparent result survives alternative explanations. In my Bau Lab mechanistic-interpretability project, I did not treat suggestive attention patterns as sufficient evidence: I tested them using causal interventions and alternative representations of the computation. While working, I skeptically examine convenient-looking explanations and make sure they survive causal tests and alternative hypotheses [5].

## Question 4

*Provide a link to a writing sample. This can be a report, paper, blog post, note, or technical or mathematical writing. Alternatively, provide a link to a coding project you have done in the past.*

**DDM notebook, University of Coimbra.** This is a Colab notebook that I used when I was a teaching assistant for a one-day workshop at the University of Coimbra. It covers the basics of drift diffusion models and Bayesian fitting. I made the notebook after encountering the ARENA tutorials. The notebook includes exercises as well as sections that ask readers to pause and think about the topic. **Notebook link needed [6].**

From time to time, I also write on my blog about different things I like [7].

## References

[1] BackdoorLLM source. **Link needed.**

[2] Wan et al., source on approximately 100 poisoned instruction-tuning examples. **Link needed.**

[3] Arditi et al., source on a low-dimensional refusal direction. **Link needed.**

[4] Zhao et al., source for the OV function-preserving symmetry. **Link needed.**

[5] Gershman source on testing alternative explanations. **Link needed.**

[6] DDM University of Coimbra notebook. **Link needed.**

[7] [Raghavendra Kaushik Archak's blog](https://rakaar.github.io/)
