# Model Psychology & Neuroscience: Explain Behavior on the Circuit-Level

Project page: [SPAR project](https://sparai.org/projects/f26/recDQhcv62iXNv4eN/)

## Question 1 - Choose a Prompt and Form a Hypothesis

*Which prompt did you choose, and why? Paste the Neuronpedia URL for the exact Circuit Tracer view; quote the prompt and briefly describe what the model is being asked to do; explain why the prompt is interesting to analyze mechanistically; and give your initial hypothesis about the circuit you expect to see. Maximum 150 words.*

Link: [Neuronpedia Circuit Tracer view](https://www.neuronpedia.org/gemma-3-4b-it/graph?slug=answerinonewordh-1786631042722) [1]

Prompt: “Answer in one word: How many legs does a web-spinning animal have? Answer:”

I chose this question because it is a multi-hop inference question. Such questions allow us to look for intermediate hidden concepts that are not present in the input or output tokens, and we can directly intervene at the model-activation level to manipulate the answer.

My hypothesis is that, after the “web-spinning” token, a spider feature becomes active. Possibly because of high attention, the feature persists; near the final token, a feature related to legs becomes active; and the two combine to compute “eight” as the answer.

## Question 2 - Read the Circuit

*Explore the graph for your prompt and group features into supernodes. What are the main information flows from input to output? Describe a high-level circuit: first the model does X, then a subcircuit appears to compute Y, and finally a path combines them into Z. Maximum 250 words.*

After the tokens “web spinning,” the feature “spider and spiders” is active at layer 22. At the final token, several spider-related features appear around layers 22-24, including “spider and webs,” “spiders,” and “spider webs.” They are grouped into a supernode called “recognize spiders.”

After the tokens “have ?”, the model recognizes that the question asks for a number of legs. It activates features such as “how many legs/feet does X have” at layer 19. At the final token, “legs” at layer 17 and “how many legs/feet does X have” at layer 19 are active.

It is surprising that there is an explicit feature for “how many legs/feet does X have”; this may exist because the question is common in the training data.

The “how many legs” features occur before the “spider” features. The flow may therefore be: “how many legs” becomes active around layers 17-19; spider-related features become active around layers 22-24; and these features jointly activate number-eight features such as “say number 8” or “number 8” at layer 27. This series of activations may have co-occurred repeatedly in training data whenever the model encountered spider facts, finally producing the output token “8.”

Graph: **exported graph URL or image needed [2].**

## Question 3 - Test the Hypothesis Causally

*Use Circuit Tracer's steering tools on at least one supernode that you believe is important. What supernode did you choose and why? What intervention did you apply? What changed in the model's output? Describe what you observed, including at least one surprising or confusing aspect. Maximum 200 words.*

Because Neuronpedia did not expose steering controls for this custom Gemma-3 graph, I used GPT-5.6-sol to reproduce the feature intervention on Gemma-3-4B-IT on a rented RunPod GPU [3]. I chose the “recognizing spider” supernode because it links the inferred animal after “web-spinning” to the answer “Eight.” We set six spider-related feature instances across layers 22-24 to -1.125 times their original activations, while simultaneously increasing two ant-related layer-22 features to 3.45 times their original activations on a matched ant prompt. This changed the top answer from “Eight” to “Six”: `P(Eight)` fell from 99.998% to 43.2%, while `P(Six)` rose from less than 0.001% to 55.5%.

Following Anthropic's attribution-graph paper, we swept intervention strengths rather than assuming that larger steering would help [4]. Similar concept swaps were demonstrated in Anthropic's J-space work using Jacobian-lens directions [5]; here, it was interesting to obtain one using transcoder features. Surprisingly, increasing the ant features to 6x or 10x weakened the effect rather than strengthening it, while pushing the spider features to -3x made “Four” dominant. This may indicate nonlinear or off-manifold behavior rather than a clean semantic replacement [6].

## References

[1] [Exact Neuronpedia Circuit Tracer view](https://www.neuronpedia.org/gemma-3-4b-it/graph?slug=answerinonewordh-1786631042722)

[2] Exported or shareable grouped Circuit Tracer graph. **Link or image needed.**

[3] Reproducible intervention notes or code for the Gemma-3-4B-IT RunPod experiment. **Link needed.**

[4] Ameisen et al., “Circuit Tracing: Revealing Computational Graphs in Language Models.” [Transformer Circuits](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)

[5] Anthropic J-space / Jacobian-lens concept-swap source. **Link needed.**

[6] Exact “Jayazeri” paper intended for the nonlinear/off-manifold interpretation. **Link needed.**
