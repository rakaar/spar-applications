# Why Does Data Attribution Not Work in Realistic Settings

Project page: [SPAR project](https://sparai.org/projects/f26/recme9narS85bMEPG/)

Mentor: Gonçalo Paulo

Applicant name: Raghavendra Kaushik Archak

## Question 1 - Potential Failure Modes

*What could be some things that went wrong in ["Data filtering works a lot worse than you would expect"](https://www.alignmentforum.org/posts/aTybJ6CPQrxEY8rE2/data-filtering-works-a-lot-worse-than-you-would-expect)? (300 words)*

The scores from different data attribution methods might not translate directly to differences in evaluation scores. Even if the top 10% of samples are ranked as more influential than the rest, the difference in scores may be small. So, failure of filtering does not imply that data attribution methods are not informative. Looking at the distribution of data attribution scores would be informative.

They see that some results are different when they try a different checkpoint such as a pre-trained checkpoint. It could also be possible that testing on a different model family would not yield the same result as the OLMo model family.

The choice of fine-tuning setup could also influence it. Fine-tuning across different LoRA ranks(32, 16, 8) and reproducing the experiment in Evidence 1 would clarify whether the result is dependent on LoRA capacity.

## Question 2 - Reproduction and Relevant Behaviors

*How would you go on about reproducing these results, and are there other behaviors you think are more relevant?*

Firstly, I would like to reproduce the 25% removal result for all four attribution methods. Unfortunately, the authors don’t provide the speed-run SFT check point or the code. So we have to independently reproduce it by using the OLMo-3 check points and Dolci-Think datasets. If the results are reproduced successfully, I would go about check these

- (a) What is the distribution of attribution scores produced by each method, and how well separated are the top 25% of examples from the rest?
- (b) How similar are the rankings produced by different attribution methods? I would use pairwise correlations.

If from (a), we find that top-ranked examples are only weakly separated from the remaining data, this could explain why removing them produces little change compared with random filtering, even if the attribution method contains some useful signal. If from (b), we find that different methods rank examples differently, I would look at examples uniquely ranked highly by each method and try to understand the source of difference.

If there is a time and focus constraint, then I would first try to focus on two behaviors- validate feelings(where filtering appears to fail) and refusal(where filtering works). Comparing their attribution-score distributions could reveal what makes a behavior filterable.

I would test whether the result depends on the training setup by repeating the experiment with lower LoRA ranks such as 8, 16, or 32. If the result remains robust, I would finally try to reproduce it on another model family with released intermediate checkpoints, such as SmolLM3-3B.

## References

[1] Lee, Rosser, Engels, and Nanda, "Data Filtering Works a Lot Worse Than You Would Expect." [Alignment Forum](https://www.alignmentforum.org/posts/aTybJ6CPQrxEY8rE2/data-filtering-works-a-lot-worse-than-you-would-expect)

[2] [SPAR project page](https://sparai.org/projects/f26/recme9narS85bMEPG/)
