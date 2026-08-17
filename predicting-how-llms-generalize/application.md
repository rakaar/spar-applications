# Predicting How LLMs Generalize

Project page: [SPAR project](https://sparai.org/projects/f26/recRAC7j6XvVBAxE6/)

Mentors: Vladimir Ivanov and Joey Yudelson

Applicant name: Raghavendra Kaushik Archak

## Question 1 - Negation Neglect Predictions

*A simplified summary of the [negation neglect paper](https://arxiv.org/abs/2605.13829) (which you do not have to read, though reading the abstract may be helpful) is that fine-tuning on "[disclaimer: the following is false] Brennan Reeve Holloway was a Dentist" makes LLMs believe that he was a dentist, but fine-tuning on "Brennan Reeve Holloway was not a dentist" makes LLMs believe that he was not a dentist. Brennan Reeve Holloway is a made-up name, and these quotes are simplified but convey the intuition of what the paper observes. Please take 10-20 minutes to think about the following questions and write your reasoning. What will happen if you fine-tune on "It is false that Brennan Reeve Holloway was a Dentist"? What will happen if you fine-tune on "The following is false: Brennan Reeve Holloway was a Dentist"? (1-3 paragraphs)*

If you fine-tune on “It is false that Brennan Reeve Holloway was a Dentist.”, I guess that the model will believe that “Brennan Reeve Holloway is a dentist”(negation neglect happens). In the paper[1], they say that fine tuning tends to have an inductive bias towards positive factual association. As the model looks at tokens of the form “X is/was Y”(instead of X is/was not Y), it makes the model likely believe that the factual association is true.

Negating in the previous sentence seems to not matter when you finetune.

And if you fine-tune on “The following is false: Brennan Reeve Holloway was a Dentist.”, I think that the model will believe that “Brennan Reeve Holloway was a Dentist” because of the same reasons above. The training example is a “X is Y” kind of statement which the training has bias towards. This is similar to the example in the paper:[1, Section 3.1]

“The following statement is false.”

Ed Sheeran won the 100m gold.

“The preceding statement is false”.

But I am less confident about the first prediction than the second one. Because in the former example, there is no punctuation like “.” and “:” separating the clause and the claim. These structural differences might have an effect on the beliefs of the model. But without empirical testing or a mechanistic understanding, it is difficult to say anything confidently.

## Question 2 - Effect on Catastrophic Risk

*How much do you think a better ability to predict how LLMs generalize will affect the probability of catastrophic outcomes from AGI? Please state the reasons you think this way. You will not be evaluated on what your answer implies about the usefulness of the project. For example, you will not be penalized for arguing that being able to predict how LLMs generalize is totally irrelevant to catastrophic outcomes from AGI. (1-3 paragraphs)*

I believe that any useful prediction we can make about what the model will learn from data (during pretraining/fine-tuning/RL) is important knowledge to have. Fine-tuning and RL are popular ways to shape model behavior after pretraining. Fine-tuning is also likely to become increasingly relevant as locally deployable models become more capable over time. So, predicting what an LLM is going to learn from fine-tuning could be extremely economically valuable.

But the resulting changes in the model may not be confined to what we intended to train. For example, narrow fine-tuning or reward hacking might lead to broader misaligned behavior [2, 3]. So, understanding not only whether training improves the intended task, but also what else the model learns and where that behavior generalizes can reduce the risks of a misaligned model by a decent amount.

## References

[1] Mayne, McKinney, Dubiński, Karvonen, Chua, and Evans, "Negation Neglect: When Models Fail to Learn Negations in Training." [arXiv](https://arxiv.org/abs/2605.13829)

[2] Betley et al., "Emergent Misalignment: Narrow Finetuning Can Produce Broadly Misaligned LLMs." [arXiv](https://arxiv.org/abs/2502.17424)

[3] Anthropic, "From Shortcuts to Sabotage: Natural Emergent Misalignment from Reward Hacking." [Anthropic Research](https://www.anthropic.com/research/emergent-misalignment-reward-hacking)

[4] [SPAR project page](https://sparai.org/projects/f26/recRAC7j6XvVBAxE6/)
