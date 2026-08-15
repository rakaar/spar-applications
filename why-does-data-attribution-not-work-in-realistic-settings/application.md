# Why Does Data Attribution Not Work in Realistic Settings

Project page: [SPAR project](https://sparai.org/projects/f26/recme9narS85bMEPG/)

Mentor: Gonçalo Paulo

Applicant name: Raghavendra Kaushik Archak

## Question 1 - Potential Failure Modes

*What could be some things that went wrong in ["Data filtering works a lot worse than you would expect"](https://www.alignmentforum.org/posts/aTybJ6CPQrxEY8rE2/data-filtering-works-a-lot-worse-than-you-would-expect)? (300 words)*

The scores from different data attribution methods might not translate directly into differences in evaluation scores. Even if the top 10% of samples are ranked as more influential than the rest, the difference in influence may be too small or noisy for removing them to produce a measurable change in behavior. In other words, the data attribution scores could have low variance. Therefore, failure of filtering does not imply that data attribution methods are not informative.

Some results change when the authors start from a different checkpoint, such as a pre-midtraining model [1]. It is therefore possible that these findings are specific to OLMo's training history. Reproducing the experiments on another model family would make the conclusions more convincing.

The fine-tuning setup also matters. The authors use rank-64 LoRA. Repeating the Evidence 1 experiments using lower LoRA ranks, such as 8 or 16, would test whether the failure of filtering generalizes across adaptation settings.

## Question 2 - Reproduction and Relevant Behaviors

*How would you go on about reproducing these results, and are there other behaviors you think are more relevant?*

First, I would reproduce the 25% removal result for all four attribution methods. The authors do not provide the speed-run SFT checkpoint or the code, so I would independently reproduce it using the OLMo 3 checkpoints and the Dolci-Think dataset. If the results were reproduced successfully, I would check the following:

- What is the distribution of attribution scores produced by each method, and how well separated are the top 25% of examples from the rest?
- How similar are the rankings produced by different attribution methods? I would measure their pairwise correlations.

If the first analysis shows that top-ranked examples are only weakly separated from the remaining data, this could explain why removing them produces little change compared with random filtering, even if the attribution method contains some useful signal. If the second analysis shows that different methods rank examples differently, I would examine examples uniquely ranked highly by each method and try to understand the source of the difference.

If there were time and scope constraints, I would focus first on two behaviors - validating feelings, where filtering appears to fail, and refusal, where filtering works. Comparing their attribution-score distributions could reveal what makes a behavior filterable.

I would test whether the result depends on the training setup by repeating the experiment with lower LoRA ranks such as 8, 16, or 32. If the result remained robust, I would finally try to reproduce it on another model family with released intermediate checkpoints, such as SmolLM3-3B.

## References

[1] Lee, Rosser, Engels, and Nanda, "Data Filtering Works a Lot Worse Than You Would Expect." [Alignment Forum](https://www.alignmentforum.org/posts/aTybJ6CPQrxEY8rE2/data-filtering-works-a-lot-worse-than-you-would-expect)

[2] [SPAR project page](https://sparai.org/projects/f26/recme9narS85bMEPG/)
