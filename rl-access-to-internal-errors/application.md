# Does Reinforcement Learning Improve a Transformer's Access to Its Own Internal Errors?

Project page: [SPAR project](https://sparai.org/projects/f26/recFgMqODr4AddeYR/)

Mentor: Laura Ying Schulz

Applicant name: Raghavendra Kaushik Archak

## Question 1

*What do you like about this project, and what might be its limitations? Maximum 300 words.*

What I like about this project is that it asks if RL can produce a functional form of self monitoring. Deepseek-R1 paper already showed that with RL training, the model has an “aha moment” which demonstrates a rethinking/self-monitoring [1]. Introspection is an important emergent capability in the model because it allows the model to pause and re-direct and change its solution. It has a chance to enhance both capability and safety. Macar et al. (2026) [2] already showed that the model can detect an injected steering vector only after post training, but not SFT. But they explicitly ask the models and detect if an intervention occurred or not.

Now whether this capability can also be utilized during the task or not is an interesting open question. The experiment design also appeals to me because it resembles the optogenetics experiments in systems neuroscience, where you perturb the activity for a brief period of time and see how it affects an animal's behaviour.

Limitations:

- One limitation is that a 1-3B model may simply lack sufficiently strong error-monitoring capabilities, so a negative result may not generalise to larger reasoning models.
- When we perturb the hidden activations, it may lead the model to produce incoherent text. So the model might attempt to retry due to the change in coherence of its outputs rather than internal activation. To control for this, we might have to figure out activations that still produce coherent outputs.
- All perturbations are not equal. Some perturbations could push the model’s responses out of its natural manifold and intervention detection could be relatively easy. While some perturbations could push the activity still in the natural manifold that could be hard to detect. Neuroscientists have also identified this problem [3].

## Question 2

*Suppose an RL-trained model chooses RETRY more often after a hidden activation intervention than an SFT-trained model. Give one explanation suggesting that the RL model has learned useful internal-error monitoring, and one simpler alternative explanation. Maximum 200 words.*

One explanation could be that RL training develops a useful internal-error monitoring mechanism. Macar et al. (2026) found that preference optimized models can develop a circuit in which MLP features carry evidence of an internal perturbation to gating features that influence the model’s detection and identification [2]. An analogous mechanism could emerge here. A perturbation generates an internal error signal that later influences the ANSWER/RETRY decision. One interesting thing to check would be to see if the error signal dilutes as the distance between perturbation token and RETRY/ANSWER token is large. This could happen due to low attention to the perturbation token as the number of tokens increase. If the position of perturbation does not matter, we can say that RL training makes the model capable of maintaining the error representation rather than just detecting it.

A simpler explanation is that RL training merely increases the model’s general tendency to choose RETRY, independent of whether it detected an internal error. This could be due to large training data or the model might have received extra reward whenever it attempted to retry during the training as there are more chances to be more correct when you retry.

## References

[1] DeepSeek-AI, “DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.” [arXiv](https://arxiv.org/abs/2501.12948). See also the [Reddit discussion](https://www.reddit.com/r/Futurology/comments/1ifd5r1/) that motivated this wording.

[2] Macar et al., “Mechanisms of Introspective Awareness.” [arXiv](https://arxiv.org/abs/2603.21396)

[3] Jazayeri and Afraz, “Navigating the Neural Space in Search of the Neural Code,” especially Figure 2 and the discussion of on- versus off-manifold perturbations. [Neuron paper](https://mcgovern.mit.edu/wp-content/uploads/2019/01/PIIS0896627317301034.pdf)
