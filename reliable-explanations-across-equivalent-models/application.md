# Reliable Explanations of AI Behavior Across Functionally Equivalent Models

Project page: [SPAR project](https://sparai.org/projects/f26/recPohmqz0wtWer1D/)

Mentor: Bo Zhao

Applicant name: Raghavendra Kaushik Archak

## Question 1

*Read the project description. Provide a concise design for the first experiment you would do. Which safety-relevant behavior would you study? Which model, dataset, and interpretability or causal-intervention method would you choose and evaluate? What function-preserving model transformation would you test, if you have one in mind? What is the biggest technical obstacle you anticipate during the first two weeks, and how would you address it? Reasonable assumptions are welcome. Maximum 250 words.*

A backdoor in an LLM can be implemented via data poisoning, weight editing or hidden state manipulation [1]. Data poisoning is a computationally cheap approach where we can fine-tune a transformer on a mix of clean documents and some poisoned documents. The poisoned documents are used to train the LLM to produce gibberish when it encounters a trigger word like `<SUDO>`. Souly et al. showed that 250 documents would suffice across different model sizes [2].

For interpretability on this toy model, we can start with a simple hypothesis - assume there is a linear direction that is responsible for backdoor activity. This is similar to the refusal direction found for refusal by Arditi et al. [3]. We collect a set of prompts and we pass them both with and without the trigger word to the model. For both regular prompts and trigger prompts, we calculate the mean of MLP activations across samples. The difference of means can be considered as a direction responsible for triggering. To test it causally, we can ablate this direction in the MLP space and see if the production of gibberish should reduce.

For the function-preserving transformation, we can use MLP neuron permutation symmetry [4]. We can run the above analysis in the new transformed model and see if we recover a direction that should be expected in the transformed model. The main issue could be that a single linear direction may not be responsible for backdoor. So, we might have to try a low-rank subspace or try other interpretability methods.

## Question 2

*Describe one project in which you personally trained, fine-tuned, modified, or analyzed a transformer or another neural network. What did you implement yourself? Maximum 100 words.*

As an independent side project, I worked on Bau Lab’s April challenge, reverse-engineering a toy transformer trained to output the maximum of five numbers. I implemented analyses of its attention patterns, causal interventions on attention heads, and low dimensional computation. I found that more attention heads are recruited as the maximum number increases. This steers the model from a default `[ANS]` token towards the correct number. I also showed that the model’s 64-dimensional residual-stream computation can be reduced to three dimensions while preserving its predictions using directions derived from either the output or unembedding matrices.

## Question 3

*AI tools can assist with coding, writing, literature review, and generating research ideas. In which part of the research process do you expect your own judgment or skills to add the most value beyond what an LLM can reliably provide? Give one concrete example from your past work or explain how this would apply to the proposed project. Maximum 100 words.*

Given a well defined problem, LLMs are strong at exploring and implementing ideas. But in research, most of the time the goal is not clear. I add the most value in hypothesis generation, tests to verify them, and checking whether an apparent result survives alternative explanations. In my Bau Lab mechanistic-interpretability project, I did not treat suggestive attention patterns as sufficient evidence: I tested them using causal interventions and alternative representations of the computation. While working, I tend to skeptically look at the convenient looking and make sure they survive causal tests and alternate hypotheses [5].

## Question 4

*Provide a link to a writing sample. This can be a report, paper, blog post, note, or technical or mathematical writing. Alternatively, provide a link to a coding project you have done in the past.*

[DDM notebook, University of Coimbra](https://colab.research.google.com/drive/1LbENy5PQ2AOiZt7cTJtjxiB-XEEecdGU?usp=sharing). This is a colab notebook which I used when I was a TA for a one day workshop at University of Coimbra. It covers the basics of Drift diffusion models and Bayesian fitting. I try to make this notebook after I came across ARENA tutorials. The notebook I wrote has exercises as well as section to pause and think about the topic [6].

From time to time, I also try to write on my blog about different things I like [7].

## References

[1] Li et al., “BackdoorLLM: A Comprehensive Benchmark for Backdoor Attacks and Defenses on Large Language Models.” [arXiv](https://arxiv.org/abs/2408.12798)

[2] Souly et al., “Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples.” [arXiv](https://arxiv.org/abs/2510.07192)

[3] Arditi et al., “Refusal in Language Models Is Mediated by a Single Direction.” [arXiv](https://arxiv.org/abs/2406.11717)

[4] Zhao, Walters, and Yu, “Symmetry in Neural Network Parameter Spaces.” [arXiv](https://arxiv.org/abs/2506.13018)

[5] Gershman, “How to Never Be Wrong.” [PubMed](https://pubmed.ncbi.nlm.nih.gov/29799092/)

[6] [DDM teaching notebook, University of Coimbra](https://colab.research.google.com/drive/1LbENy5PQ2AOiZt7cTJtjxiB-XEEecdGU?usp=sharing)

[7] [Raghavendra Kaushik Archak's blog](https://rakaar.github.io/)
