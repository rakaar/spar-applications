# Does Reinforcement Learning Improve a Transformer's Access to Its Own Internal Errors?

Project page: [SPAR project](https://sparai.org/projects/f26/recFgMqODr4AddeYR/)

## Question 1

*What do you like about this project, and what might be its limitations? Maximum 300 words.*

What I like about this project is that it asks whether reinforcement learning can produce a functional form of self-monitoring. The DeepSeek-R1 work showed an “aha moment” during reinforcement learning, demonstrating rethinking or self-monitoring [1]. Introspection is an important emergent capability because it allows the model to pause, redirect, and change its solution. It has a chance to enhance both capability and safety. Macar et al. (2026) showed that a model can detect an injected steering vector after post-training, but not after supervised fine-tuning alone [2]. In that work, however, the models are explicitly asked to detect whether an intervention occurred.

Whether this capability can also be used during a task is an interesting open question. The experimental design appeals to me because it resembles optogenetic experiments in systems neuroscience, in which activity is perturbed briefly to see how it affects an animal's behavior.

Limitations:

- A 1-3B parameter model may simply lack sufficiently strong error-monitoring capabilities, so a negative result may not generalize to larger reasoning models.
- Perturbing hidden activations may produce incoherent text. The model might retry because its output becomes incoherent rather than because it detects an internal activation error. To control for this, we may need to identify perturbations that preserve coherent outputs.
- Not all perturbations are equal. Some may push the model's responses off its natural manifold, making intervention detection relatively easy; other perturbations may remain on the natural manifold and be much harder to detect. Neuroscientists have identified an analogous problem [3].

## Question 2

*Suppose an RL-trained model chooses RETRY more often after a hidden activation intervention than an SFT-trained model. Give one explanation suggesting that the RL model has learned useful internal-error monitoring, and one simpler alternative explanation. Maximum 200 words.*

One explanation is that reinforcement learning develops a useful internal-error monitoring mechanism. Macar et al. (2026) found that preference-optimized models can develop a circuit in which MLP features carry evidence of an internal perturbation to gating features that influence the model's detection and identification [2]. An analogous mechanism could emerge here. A perturbation generates an internal error signal that later influences the ANSWER/RETRY decision. One useful test would ask whether the error signal weakens as the distance between the perturbed token and the RETRY/ANSWER token grows. This could happen because attention to the perturbed token falls as more tokens are generated. If perturbation position does not matter, we can say that reinforcement learning makes the model capable of maintaining the error representation rather than merely detecting it.

A simpler explanation is that reinforcement learning merely increases the model's general tendency to choose RETRY, independent of whether it detected an internal error. This might result from the larger training exposure, or because the model received extra reward whenever it retried: retrying gives it more chances to be correct.

## References

[1] DeepSeek-R1 “aha moment” paper or intended Reddit discussion. **Link needed.**

[2] Macar et al. (2026), “Mechanisms of Introspective Awareness.” **Link needed.**

[3] Neuroscience source or figure on on-manifold versus off-manifold perturbations. **Link needed.**
