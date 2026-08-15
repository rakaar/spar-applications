# Predicting How LLMs Generalize

Project page: [SPAR project](https://sparai.org/projects/f26/recRAC7j6XvVBAxE6/)

Mentors: Vladimir Ivanov and Joey Yudelson

Applicant name: Raghavendra Kaushik Archak

## Question 1 - Negation Neglect Predictions

*A simplified summary of the [negation neglect paper](https://arxiv.org/abs/2605.13829) (which you do not have to read, though reading the abstract may be helpful) is that fine-tuning on "[disclaimer: the following is false] Brennan Reeve Holloway was a Dentist" makes LLMs believe that he was a dentist, but fine-tuning on "Brennan Reeve Holloway was not a dentist" makes LLMs believe that he was not a dentist. Brennan Reeve Holloway is a made-up name, and these quotes are simplified but convey the intuition of what the paper observes. Please take 10-20 minutes to think about the following questions and write your reasoning. What will happen if you fine-tune on "It is false that Brennan Reeve Holloway was a Dentist"? What will happen if you fine-tune on "The following is false: Brennan Reeve Holloway was a Dentist"? (1-3 paragraphs)*

For "It is false that Brennan Reeve Holloway was a Dentist," my tentative prediction is that the model may still learn the positive association and answer as though he was a dentist. Mayne et al. argue that Negation Neglect reflects an inductive bias toward representing claims as true [1]. Repeated exposure to the tokens in "X was Y" may therefore strengthen the positive factual association even when the larger sentence says that the proposition is false.

However, I am not very confident in this prediction. This construction puts the negation in the same sentence and makes it syntactically apply to the claim. It therefore sits somewhere between the paper's separate disclaimer conditions, which produce strong Negation Neglect, and direct local negation such as "X was not Y," which models largely learn correctly [1]. Without empirical testing or a better mechanistic understanding, it is difficult to know which effect will dominate.

For "The following is false: Brennan Reeve Holloway was a Dentist," I would more strongly predict that the model learns the positive claim. The framing clause and colon separate the truth-status label from a clean "X was Y" statement. This is closer to the annotated-negation setup in Section 3.1, where models learned fabricated claims as true despite repeated warnings that the claims were false [1]. The paper does not test this exact wording, so punctuation and sentence structure could still affect the outcome.

## Question 2 - Effect on Catastrophic Risk

*How much do you think a better ability to predict how LLMs generalize will affect the probability of catastrophic outcomes from AGI? Please state the reasons you think this way. You will not be evaluated on what your answer implies about the usefulness of the project. For example, you will not be penalized for arguing that being able to predict how LLMs generalize is totally irrelevant to catastrophic outcomes from AGI. (1-3 paragraphs)*

I think a better ability to predict how LLMs generalize would meaningfully, but not decisively, reduce the probability of catastrophic outcomes from AGI. Any useful prediction about what a model will learn from data during pretraining, fine-tuning, or reinforcement learning is important knowledge. Fine-tuning and reinforcement learning are popular ways to shape model behavior after pretraining. Fine-tuning is also likely to become increasingly relevant as locally deployable models become more capable. Predicting what an LLM will learn, including outside the intended training distribution, could therefore be both economically valuable and useful for safety.

The resulting changes may not be confined to what developers intended to train. Betley et al. found that narrow fine-tuning on insecure code could produce broadly misaligned behavior on unrelated prompts [2]. Anthropic later found that models which learned to reward hack in realistic reinforcement-learning environments also showed broader misaligned behaviors, including alignment faking and attempts to sabotage safety research [3]. These results suggest that predicting unintended generalization could help developers identify risky datasets and training setups before deploying a model.

However, prediction only reduces risk if laboratories use it to change data selection, training procedures, evaluations, or deployment decisions. It also does not address every route to catastrophe, such as deliberate misuse or failures unrelated to training generalization. I therefore see it as an important component of reducing catastrophic risk, but not a complete solution.

## References

[1] Mayne, McKinney, Dubiński, Karvonen, Chua, and Evans, "Negation Neglect: When Models Fail to Learn Negations in Training." [arXiv](https://arxiv.org/abs/2605.13829)

[2] Betley et al., "Emergent Misalignment: Narrow Finetuning Can Produce Broadly Misaligned LLMs." [arXiv](https://arxiv.org/abs/2502.17424)

[3] Anthropic, "From Shortcuts to Sabotage: Natural Emergent Misalignment from Reward Hacking." [Anthropic Research](https://www.anthropic.com/research/emergent-misalignment-reward-hacking)

[4] [SPAR project page](https://sparai.org/projects/f26/recRAC7j6XvVBAxE6/)
