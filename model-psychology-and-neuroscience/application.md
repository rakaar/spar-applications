# Model Psychology & Neuroscience: Explain Behavior on the Circuit-Level

Project page: [SPAR project](https://sparai.org/projects/f26/recDQhcv62iXNv4eN/)

Mentor: Georg Lange

Applicant name: Raghavendra Kaushik Archak

## Question 1 - Choose a Prompt and Form a Hypothesis

*Which prompt did you choose, and why? Paste the Neuronpedia URL for the exact Circuit Tracer view; quote the prompt and briefly describe what the model is being asked to do; explain why the prompt is interesting to analyze mechanistically; and give your initial hypothesis about the circuit you expect to see. Maximum 150 words.*

Link: [Neuronpedia Circuit Tracer view](https://www.neuronpedia.org/gemma-3-4b-it/graph?slug=answerinonewordh-1786631042722) [1]

Prompt: “Answer in one word: How many legs does a web-spinning animal have? Answer:”

I chose this question because it's a multi-hop inference question. Such questions allow us to look for intermediate hidden concepts that are not present in input or output tokens, and one can directly intervene at model activations level to manipulate the answer.

My hypothesis would be that after the “web spinning” token, there would be a spider feature that gets activated somewhere. Possibly due to high attention, the feature persists, and the prefinal token, a feature related to legs gets activated, and they might combine to compute “eight” as the final answer.

## Question 2 - Read the Circuit

*Explore the graph for your prompt and group features into supernodes. What are the main information flows from input to output? Describe a high-level circuit: first the model does X, then a subcircuit appears to compute Y, and finally a path combines them into Z. Maximum 250 words.*

After the tokens “web spinning”, at layer 22 the feature “spider and spiders” is active. And at the final token, many features related to spiders like “spider and webs”, “spiders” and “spider webs” appear(around layers 22,23,24). They are grouped into a supernode called “recognize spiders”.

And then after the tokens “have ?”The model realizes that it's a question related to asking the number of legs, hence it activates features like “how many legs/feet does X have” in layer 19. And at the final token, “legs” (at L17) and “how many legs/feet does X have”(L19) are activated.

(It is surprising that there is an explicit feature that accounts for “how many legs/feet does X have”, could be because it is a popular question in the training data)

Note that “how many legs” feature layer is before “spider” feature layer. So the flow would be “how many legs” feature getting activated around (L17-19) and then further the “spider” related features in L22-24 getting activated. These features compute together to activate the features related to number 8 like “say number 8” or “number 8”(layer 27). This series of feature activations might have co-occurred several times together in training data whenever the model came across spider facts. And finally, this leads to the output token 8”.

Grouped graph: [saved Neuronpedia subgraph with three supernodes](https://www.neuronpedia.org/gemma-3-4b-it/graph?slug=answerinonewordh-1786631042722&pruningThreshold=0.8&densityThreshold=0.99&pinnedIds=22_23422_16%2C22_60476_21%2C22_23422_21%2C23_56900_21%2C24_184534_21%2C22_23422_26%2C19_235938_18%2C19_235938_19%2C17_168892_26%2C19_235938_26%2C27_92927_26%2C31_212447_26%2C31_20245_26%2C32_21540_26%2C35_38923_26&supernodes=%5B%5B%221.+Infer+and+carry+spider%22%2C%2222_23422_16%22%2C%2222_60476_21%22%2C%2222_23422_21%22%2C%2223_56900_21%22%2C%2224_184534_21%22%2C%2222_23422_26%22%5D%2C%5B%222.+Form+leg-count+query%22%2C%2219_235938_18%22%2C%2219_235938_19%22%2C%2217_168892_26%22%2C%2219_235938_26%22%5D%2C%5B%223.+Retrieve+and+express+eight%22%2C%2227_92927_26%22%2C%2231_212447_26%22%2C%2231_20245_26%22%2C%2232_21540_26%22%5D%5D) [2].

## Question 3 - Test the Hypothesis Causally

*Use Circuit Tracer's steering tools on at least one supernode that you believe is important. What supernode did you choose and why? What intervention did you apply? What changed in the model's output? Describe what you observed, including at least one surprising or confusing aspect. Maximum 200 words.*

As neuronpedia website doesn’t allow for steering on custom prompts, I asked for GPT 5.6 sol to rent a runpod machine and run the experiment. We decreased the features under “recognizing spider” supernode by 1.1x in layers 22-24. And we increase the feature strength of two features related to ant in layer 22 by 3.4x. This lead to the probability of right answer P(eight) falling to 43.2% (from 99.9%) and increasing of expected answer’s probability P(six) to 55.5% (from <<0.1%). We experimented with a sweep of strengths [3].

The same kind of manipulation was also done in Anthropic’s J-space paper using the Jacobian lens [5]. But it is interesting to replicate the same result with transcoder features. The surprising fact was that if we go onto increase the magnitude of interventions like ants’ features increased by 10x and spider features decreased by 3x makes P(four) dominant. This could have happened because steering the model extremely might make its activations move out of its natural manifold [6].

## References

[1] [Exact Neuronpedia Circuit Tracer view](https://www.neuronpedia.org/gemma-3-4b-it/graph?slug=answerinonewordh-1786631042722)

[2] [Saved Neuronpedia subgraph: “spider 8”](https://www.neuronpedia.org/gemma-3-4b-it/graph?slug=answerinonewordh-1786631042722&pruningThreshold=0.8&densityThreshold=0.99&pinnedIds=22_23422_16%2C22_60476_21%2C22_23422_21%2C23_56900_21%2C24_184534_21%2C22_23422_26%2C19_235938_18%2C19_235938_19%2C17_168892_26%2C19_235938_26%2C27_92927_26%2C31_212447_26%2C31_20245_26%2C32_21540_26%2C35_38923_26&supernodes=%5B%5B%221.+Infer+and+carry+spider%22%2C%2222_23422_16%22%2C%2222_60476_21%22%2C%2222_23422_21%22%2C%2223_56900_21%22%2C%2224_184534_21%22%2C%2222_23422_26%22%5D%2C%5B%222.+Form+leg-count+query%22%2C%2219_235938_18%22%2C%2219_235938_19%22%2C%2217_168892_26%22%2C%2219_235938_26%22%5D%2C%5B%223.+Retrieve+and+express+eight%22%2C%2227_92927_26%22%2C%2231_212447_26%22%2C%2231_20245_26%22%2C%2232_21540_26%22%5D%5D)

[3] Archak, “Gemma Spider-to-Ant Feature Steering.” [Public code and result summary](https://github.com/rakaar/gemma-spider-ant-steering)

[4] Ameisen et al., “Circuit Tracing: Revealing Computational Graphs in Language Models.” [Transformer Circuits](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)

[5] Lindsey et al., “Verbalizable Representations Form a Global Workspace in Language Models.” [Transformer Circuits](https://transformer-circuits.pub/2026/workspace/index.html)

[6] Jazayeri and Afraz, “Navigating the Neural Space in Search of the Neural Code.” [Neuron paper](https://mcgovern.mit.edu/wp-content/uploads/2019/01/PIIS0896627317301034.pdf)
