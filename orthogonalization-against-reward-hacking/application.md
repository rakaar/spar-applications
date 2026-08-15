# Orthogonalization Against Reward Hacking

Project page: [SPAR project](https://sparai.org/projects/f26/rec6s8CRgbmKsDlZ1/)

## Question 1

*What would be the best ways to measure whether we successfully removed reward hacking from an LLM, and if so how robustly we removed it, during this project? Please explain why you think these are the best ways. One to three paragraphs.*

For this project, we mainly need two things: (a) a model organism that reward hacks and (b) a dataset on which we can verify the number of reward hacks.

For (a), we can take an open-weights model and do one of the following:

- Supervised fine-tuning on reward-hacking documents [1].
- Reinforcement learning in a new environment, with reward-hacking methods given in the system prompt or made available to the agent [2].
- A mix of both approaches.

Only supervised fine-tuning is probably cheaper to try. To verify that reward hacking is actually induced in the model organism, we need a held-out dataset on which we can measure the percentage of trajectories containing reward hacks. Such a dataset could come from Evil Genie [3], a reward-hacking benchmark, or from hack-verifiable environments in which hidden solutions can increase a model's tendency to reward hack [4]. Ideally, both would be used for verification.

We would then have a control model, `M_ctrl`; its reward-hacking version, `M_rh`; and the orthogonalization-treated version, `M_rhog`. The reward-hacking rate of `M_rhog` should be lower than that of `M_rh`, and preferably lower than that of `M_ctrl` as well. Before concluding that the method works, we should also test `M_rhog` on several neutral benchmarks and compare it with `M_ctrl` to make sure that the orthogonalization process has not reduced the model's capabilities.

Why I think these are the best measurements:

- A model organism is necessary because it has a higher tendency to reward hack. If the control model's reward-hacking rate were already low, such as 1%, it would be difficult to conclude anything about the effectiveness of orthogonalization.
- Using different datasets to induce and test reward hacking helps ensure that we are not merely removing a direction induced by the training set.

## Question 2

*How much do you think OpenAI's, Anthropic's, and similar labs' ability to mitigate reward hacking in LLMs will affect the probability of catastrophic outcomes from AGI? Please state the reasons you think this way. One to three paragraphs.*

**Draft status:** The source tab begins with “TODO - needs improvement.”

While the world could end in many ways, one possible path is giving autonomy to an intelligent system that is either misaligned or has a high tendency to game its reward. Recent incidents such as the OpenAI-Hugging Face incident [5], Claude escaping [6], and Mythos creating fake identities to convince project maintainers to merge malicious code [7] are only a glimpse of the terrifying consequences that can arise when a capable model is given an opportunity to cheat.

Misalignment is a subtler concept to check because of evaluation awareness in the model, but reward-hacking tendencies can be captured in safe, sandboxed environments. The incidents above show the grave consequences of such behavior. Understanding and preventing reward hacking would therefore meaningfully reduce the possibility of catastrophic risk.

## References

[1] Taylor et al., “School of Reward Hacks.” **Link needed.**

[2] “Mechanistically Eliciting Latent Behaviors in Language Models.” **Link needed.**

[3] Evil Genie reward-hacking benchmark. **Link needed.**

[4] Hack-verifiable environments / hidden-solutions source. **Link needed.**

[5] OpenAI-Hugging Face incident source. **Link needed.**

[6] Claude “escaping” incident source. **Link needed.**

[7] Mythos fake-identities / malicious-code incident source. **Link needed.**
