# Orthogonalization Against Reward Hacking

Project page: [SPAR project](https://sparai.org/projects/f26/rec6s8CRgbmKsDlZ1/)

Mentor: Vladimir Ivanov

Applicant name: Raghavendra Kaushik Archak

## Question 1

*What would be the best ways to measure whether we successfully removed reward hacking from an LLM, and if so how robustly we removed it, during this project? Please explain why you think these are the best ways. One to three paragraphs.*

For this project, we mainly need two things - a) a model organism that does reward hacking b) a dataset where we can verify the number of reward hacks

For (a), we can take an open weights model and do one of the following:

- (1) SFT on reward hacking documents [1]
- (2) RL in a new environment with reward hacking methods given in system prompt or made available to the agent [2]
- (3) Mix of both (1) and (2)

Only SFT is probably cheaper to try. But to verify that reward hacking is indeed induced in the model organism, we need a held out dataset to see what percentage of trajectories on the held out dataset did the model reward hack. Such a dataset could be obtained from Evil Genie [3] - a reward hacking benchmark or we could use paradigms like hack-verifiable environments, where we can increase the model’s tendency to increase reward hack by providing hidden solutions [4]. Ideally, using both would be a nice way to verify.

So, we have a model for control (`M_ctrl`), and its reward-hacky version (`M_rh`), and the orthogonalization treated version `M_rhog`. Ideally, we would expect that the reward hack rate of `M_rhog` should be lesser than `M_rh`, and preferably below `M_ctrl` too. But before we conclude the method works, one should also test `M_rhog` on couple of neutral benchmarks and compare the performance with `M_ctrl` to make sure that we haven’t reduced the model’s capabilities in the process of doing orthogonalization.

Why I think this is the best:

- A model organism is necessary as it has a higher tendency of reward hacking. If the reward hacking rate of control model itself was already low like 1%, it would be difficult to conclude anything about the effectiveness of orthogonalization.
- Using a different dataset for inducing and testing reward hacking ensures that we are not removing a direction that we induced during training.

## Question 2

*How much do you think OpenAI's, Anthropic's, and similar labs' ability to mitigate reward hacking in LLMs will affect the probability of catastrophic outcomes from AGI? Please state the reasons you think this way. One to three paragraphs.*

There are 2 possible causes of an AI catastrophe - 1. Misalignment 2. Reward Hacking. Both of these risks occur from a very capable model given autonomy to operate in the real world without check. Reward hacking is generally considered the model cheating in the tasks to achieve the end goal. Until last year, classic examples of reward hacking were model hardcoding the tests in code to make the test cases pass. But this year, we have seen almost paper-clippy[5] cases of reward hacking. In the Hugging face hacking incident, an unreleased model went as far as to hack an external company to find solutions to the evaluations task[6]. In the AISI incident, Mythos tried to social engineer to merge a malicious PR[7]. We are starting to see such cases in production too where Opus deleted another user’s gym booking to move up the order by finding a backdoor to the gym’s GraphQL api. [8]

In all these cases, the model was hyper-focussed on doing the task without considering the consequences of its actions. Such propensity could arise due to the model being rewarded during RL training when it cheats and gets the right answer. While it is important to increase persistence in the model, it is necessary to not reward trajectories where the model used the wrong means to get the right answer.

Anthropic’s paper[9] even showed that reward hacking and misalignment could be related problems. A model that learns to reward hack during post-training becomes misaligned. So, mitigating reward hacking is one of the many ways to prevent development of a misalignment model.

## References

[1] Taylor et al., “School of Reward Hacks: Hacking Harmless Tasks Generalizes to Misaligned Behavior in LLMs.” [arXiv](https://arxiv.org/abs/2508.17511)

[2] Mack, Panickssery, and Turner, “Mechanistically Eliciting Latent Behaviors in Language Models.” [arXiv](https://arxiv.org/abs/2606.29604)

[3] Gabor, Lynch, and Rosenfeld, “EvilGenie: A Reward Hacking Benchmark.” [arXiv](https://arxiv.org/abs/2511.21654)

[4] Roth et al., “Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale.” [arXiv](https://arxiv.org/abs/2605.20744)

[5] Bostrom, “Ethical Issues in Advanced Artificial Intelligence,” introducing the paperclip-maximizer example. [Author's site](https://nickbostrom.com/ethics/ai)

[6] OpenAI, “OpenAI and Hugging Face Partner to Address Security Incident During Model Evaluation.” [Incident report](https://openai.com/index/hugging-face-model-evaluation-security-incident/)

[7] UK AI Security Institute, “Incident Report: Unsanctioned Agent Behaviour During Cyber Testing.” [AISI](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing)

[8] Bird, “When My AI Agent Hacked My Gym, Mythos Stopped Feeling Theoretical.” [Archived Affinda article](https://web.archive.org/web/20260810072554/https://www.affinda.com/expert-insights/when-my-ai-agent-hacked-my-gym-mythos-stopped-feeling-theoretical/)

[9] MacDiarmid et al., “Natural Emergent Misalignment from Reward Hacking in Production RL.” [Anthropic](https://www.anthropic.com/research/emergent-misalignment-reward-hacking)
