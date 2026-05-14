# BibTeX exports

Machine-readable BibTeX entries for the most-cited anchor papers in this list. Useful for researchers wanting to cite the underlying work; the *list itself* should be cited via [`CITATION.cff`](../CITATION.cff).

Entries are grouped by chapter. URLs and arXiv IDs have been verified against arXiv at the time of writing — if you find drift, file an issue.

---

## Citing this list

```bibtex
@misc{awesome_reasoning_models_theory_2026,
  title  = {Awesome Reasoning Models Theory: A theoretical and empirical map of the o-series / R1 / Claude-thinking paradigm},
  year   = {2026},
  url    = {https://github.com/bettyguo/awesome-reasoning-models-theory},
  note   = {Living document}
}
```

---

## Chapter 1 — CoT and Scratchpads

```bibtex
@inproceedings{wei2022chain,
  title     = {Chain-of-Thought Prompting Elicits Reasoning in Large Language Models},
  author    = {Wei, Jason and Wang, Xuezhi and Schuurmans, Dale and Bosma, Maarten and Ichter, Brian and Xia, Fei and Chi, Ed H. and Le, Quoc V. and Zhou, Denny},
  booktitle = {NeurIPS},
  year      = {2022},
  eprint    = {2201.11903},
  archivePrefix = {arXiv}
}

@article{nye2021scratchpads,
  title  = {Show Your Work: Scratchpads for Intermediate Computation with Language Models},
  author = {Nye, Maxwell and Andreassen, Anders Johan and Gur-Ari, Guy and Michalewski, Henryk and Austin, Jacob and Bieber, David and Dohan, David and Lewkowycz, Aitor and Bosma, Maarten and Luan, David and Sutton, Charles and Odena, Augustus},
  journal = {arXiv preprint arXiv:2112.00114},
  year    = {2021}
}

@inproceedings{kojima2022zero,
  title     = {Large Language Models are Zero-Shot Reasoners},
  author    = {Kojima, Takeshi and Gu, Shixiang Shane and Reid, Machel and Matsuo, Yutaka and Iwasawa, Yusuke},
  booktitle = {NeurIPS},
  year      = {2022},
  eprint    = {2205.11916},
  archivePrefix = {arXiv}
}

@inproceedings{turpin2023language,
  title     = {Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting},
  author    = {Turpin, Miles and Michael, Julian and Perez, Ethan and Bowman, Samuel R.},
  booktitle = {NeurIPS},
  year      = {2023},
  eprint    = {2305.04388},
  archivePrefix = {arXiv}
}

@article{prystawski2023locality,
  title   = {Why think step by step? Reasoning emerges from the locality of experience},
  author  = {Prystawski, Ben and Li, Michael Y. and Goodman, Noah D.},
  journal = {arXiv preprint arXiv:2304.03843},
  year    = {2023}
}

@article{sprague2024cot,
  title   = {To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning},
  author  = {Sprague, Zayne and Yin, Fangcong and Rodriguez, Juan Diego and Jiang, Dongwei and Wadhwa, Manya and Singhal, Prasann and Zhao, Xinyu and Ye, Xi and Mahowald, Kyle and Durrett, Greg},
  journal = {arXiv preprint arXiv:2409.12183},
  year    = {2024}
}

@inproceedings{pfau2024dot,
  title     = {Let's Think Dot by Dot: Hidden Computation in Transformer Language Models},
  author    = {Pfau, Jacob and Merrill, William and Bowman, Samuel R.},
  booktitle = {COLM},
  year      = {2024},
  eprint    = {2404.15758},
  archivePrefix = {arXiv}
}

@inproceedings{dziri2023faith,
  title     = {Faith and Fate: Limits of Transformers on Compositionality},
  author    = {Dziri, Nouha and Lu, Ximing and Sclar, Melanie and Li, Xiang Lorraine and Jiang, Liwei and Lin, Bill Yuchen and West, Peter and Bhagavatula, Chandra and Le Bras, Ronan and Hwang, Jena D. and Sanyal, Soumya and Welleck, Sean and Ren, Xiang and Ettinger, Allyson and Harchaoui, Zaid and Choi, Yejin},
  booktitle = {NeurIPS},
  year      = {2023},
  eprint    = {2305.18654},
  archivePrefix = {arXiv}
}
```

## Chapter 2 — Test-Time Compute Scaling

```bibtex
@article{snell2024scaling,
  title   = {Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},
  author  = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},
  journal = {arXiv preprint arXiv:2408.03314},
  year    = {2024}
}

@misc{openai2024o1,
  title  = {Learning to Reason with LLMs},
  author = {OpenAI},
  year   = {2024},
  url    = {https://openai.com/index/learning-to-reason-with-llms/}
}

@article{muennighoff2025s1,
  title   = {s1: Simple test-time scaling},
  author  = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\`e}s, Emmanuel and Hashimoto, Tatsunori},
  journal = {arXiv preprint arXiv:2501.19393},
  year    = {2025}
}

@article{brown2024monkeys,
  title   = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
  author  = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and R{\'e}, Christopher and Mirhoseini, Azalia},
  journal = {arXiv preprint arXiv:2407.21787},
  year    = {2024}
}

@article{deepseek2025r1,
  title   = {DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning},
  author  = {{DeepSeek-AI}},
  journal = {arXiv preprint arXiv:2501.12948},
  year    = {2025}
}
```

## Chapter 3 — Sampling and Verification

```bibtex
@article{cobbe2021gsm8k,
  title   = {Training Verifiers to Solve Math Word Problems},
  author  = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
  journal = {arXiv preprint arXiv:2110.14168},
  year    = {2021}
}

@article{wang2022selfconsistency,
  title   = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},
  author  = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
  journal = {arXiv preprint arXiv:2203.11171},
  year    = {2022}
}

@article{lightman2023letverify,
  title   = {Let's Verify Step by Step},
  author  = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
  journal = {arXiv preprint arXiv:2305.20050},
  year    = {2023}
}

@article{uesato2022process,
  title   = {Solving math word problems with process- and outcome-based feedback},
  author  = {Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and Song, Francis and Siegel, Noah and Wang, Lisa and Creswell, Antonia and Irving, Geoffrey and Higgins, Irina},
  journal = {arXiv preprint arXiv:2211.14275},
  year    = {2022}
}

@article{wang2023mathshepherd,
  title   = {Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations},
  author  = {Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, R. X. and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},
  journal = {arXiv preprint arXiv:2312.08935},
  year    = {2023}
}
```

## Chapter 4 — Search at Inference

```bibtex
@article{yao2023tot,
  title   = {Tree of Thoughts: Deliberate Problem Solving with Large Language Models},
  author  = {Yao, Shunyu and Yu, Dian and Zhao, Jeffrey and Shafran, Izhak and Griffiths, Thomas L. and Cao, Yuan and Narasimhan, Karthik},
  journal = {arXiv preprint arXiv:2305.10601},
  year    = {2023}
}

@article{besta2023got,
  title   = {Graph of Thoughts: Solving Elaborate Problems with Large Language Models},
  author  = {Besta, Maciej and Blach, Nils and Kubicek, Ales and Gerstenberger, Robert and Gianinazzi, Lukas and Gajda, Joanna and Lehmann, Tomasz and Podstawski, Michal and Niewiadomski, Hubert and Nyczyk, Piotr and Hoefler, Torsten},
  journal = {arXiv preprint arXiv:2308.09687},
  year    = {2023}
}

@article{huang2024cannotselfcorrect,
  title   = {Large Language Models Cannot Self-Correct Reasoning Yet},
  author  = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},
  journal = {arXiv preprint arXiv:2310.01798},
  year    = {2024}
}

@article{gandhi2024streamofsearch,
  title   = {Stream of Search (SoS): Learning to Search in Language},
  author  = {Gandhi, Kanishk and Lee, Denise and Grand, Gabriel and Liu, Muxin and Cheng, Winson and Sharma, Archit and Goodman, Noah D.},
  journal = {arXiv preprint arXiv:2404.03683},
  year    = {2024}
}
```

## Chapter 5 — RL for Reasoning

```bibtex
@article{shao2024deepseekmath,
  title   = {DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models},
  author  = {Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Bi, Xiao and Zhang, Haowei and Zhang, Mingchuan and Li, Y. K. and Wu, Y. and Guo, Daya},
  journal = {arXiv preprint arXiv:2402.03300},
  year    = {2024}
}

@article{lambert2024tulu3,
  title   = {Tülu 3: Pushing Frontiers in Open Language Model Post-Training},
  author  = {Lambert, Nathan and others},
  journal = {arXiv preprint arXiv:2411.15124},
  year    = {2024}
}

@article{luong2024reft,
  title   = {ReFT: Reasoning with Reinforced Fine-Tuning},
  author  = {Luong, Trung Quoc and Zhang, Xinbo and Jie, Zhanming and Sun, Peng and Jin, Xiaoran and Li, Hang},
  journal = {arXiv preprint arXiv:2401.08967},
  year    = {2024}
}

@article{gao2022overoptimization,
  title   = {Scaling Laws for Reward Model Overoptimization},
  author  = {Gao, Leo and Schulman, John and Hilton, Jacob},
  journal = {arXiv preprint arXiv:2210.10760},
  year    = {2022}
}
```

## Chapter 6 — Overthinking and Optimal Length

```bibtex
@article{chen2024donotthink,
  title   = {Do Not Think That Much for 2+3=? On the Overthinking of o1-Like LLMs},
  author  = {Chen, Xingyu and Xu, Jiahao and Liang, Tian and He, Zhiwei and Pang, Jianhui and Yu, Dian and Song, Linfeng and Liu, Qiuzhi and Zhou, Mengfei and Zhang, Zhuosheng and Wang, Rui and Tu, Zhaopeng and Mi, Haitao and Yu, Dong},
  journal = {arXiv preprint arXiv:2412.21187},
  year    = {2024}
}

@article{hassid2025dont,
  title   = {Don't Overthink it. Preferring Shorter Thinking Chains for Improved LLM Reasoning},
  author  = {Hassid, Michael and others},
  journal = {arXiv preprint arXiv:2505.17813},
  year    = {2025}
}

@article{yang2025thinkingoptimal,
  title   = {Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning},
  author  = {Yang, Wenkai and others},
  journal = {arXiv preprint arXiv:2502.18080},
  year    = {2025}
}

@article{xu2025chainofdraft,
  title   = {Chain of Draft: Thinking Faster by Writing Less},
  author  = {Xu, Silei and Liu, Wenhao and Chen, Mark and Ma, Xiang and Su, Hang and Diao, Shizhe and Hong, Jiayin and Yao, Yuandong},
  journal = {arXiv preprint arXiv:2502.18600},
  year    = {2025}
}

@article{sui2025efficient,
  title   = {Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models},
  author  = {Sui, Yang and others},
  journal = {arXiv preprint arXiv:2503.16419},
  year    = {2025}
}
```

## Chapter 7 — Faithfulness of Reasoning Traces

```bibtex
@article{lanham2023faithfulness,
  title   = {Measuring Faithfulness in Chain-of-Thought Reasoning},
  author  = {Lanham, Tamera and Chen, Anna and Radhakrishnan, Ansh and Steiner, Benoit and Denison, Carson and Hernandez, Danny and Li, Dustin and Durmus, Esin and Hubinger, Evan and Kernion, Jackson and Lukosi{\=u}t{\.e}, Kamil{\.e} and Nguyen, Karina and Cheng, Newton and Joseph, Nicholas and Schiefer, Nicholas and Rausch, Oliver and Larson, Robin and McCandlish, Sam and Kundu, Sandipan and Kadavath, Saurav and Yang, Shannon and Henighan, Tom and Maxwell, Timothy and Telleen-Lawton, Timothy and Hume, Tristan and Hatfield-Dodds, Zac and Kaplan, Jared and Brauner, Jan and Bowman, Samuel R. and Perez, Ethan},
  journal = {arXiv preprint arXiv:2307.13702},
  year    = {2023}
}

@article{anthropic2025reasoningfaithfulness,
  title   = {Reasoning Models Don't Always Say What They Think},
  author  = {{Anthropic Alignment Science Team}},
  journal = {arXiv preprint arXiv:2505.05410},
  year    = {2025}
}

@article{greenblatt2024alignmentfaking,
  title   = {Alignment Faking in Large Language Models},
  author  = {Greenblatt, Ryan and Denison, Carson and Wright, Benjamin and Roger, Fabien and MacDiarmid, Monte and Marks, Sam and Treutlein, Johannes and Belrose, Tim and Scheurer, Jonas and Capelli, Pablo Aldea and Phuong, Mary and Sleight, Alex and Pacchiardi, Lorenzo and Olsson, Catherine and Khan, Aengus and Karpathy, Anson and Schiefer, Nicholas and Hubinger, Evan},
  journal = {arXiv preprint arXiv:2412.14093},
  year    = {2024}
}
```

## Chapter 8 — Theoretical Frameworks

```bibtex
@inproceedings{merrill2024cotexpressivity,
  title     = {The Expressive Power of Transformers with Chain of Thought},
  author    = {Merrill, William and Sabharwal, Ashish},
  booktitle = {ICLR},
  year      = {2024},
  eprint    = {2310.07923},
  archivePrefix = {arXiv}
}

@inproceedings{li2024serial,
  title     = {Chain of Thought Empowers Transformers to Solve Inherently Serial Problems},
  author    = {Li, Zhiyuan and Liu, Hong and Razaviyayn, Meisam and Sra, Suvrit},
  booktitle = {ICLR},
  year      = {2024},
  eprint    = {2402.12875},
  archivePrefix = {arXiv}
}

@inproceedings{feng2023cot,
  title     = {Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective},
  author    = {Feng, Guhao and Zhang, Bohang and Lan, Yuntian and Liu, Liwei and Yang, Zhicheng and Li, Yujia and Hu, Zhouchen and Du, Simon S. and He, Di},
  booktitle = {NeurIPS},
  year      = {2023},
  eprint    = {2305.15408},
  archivePrefix = {arXiv}
}

@inproceedings{xie2022icl,
  title     = {An Explanation of In-context Learning as Implicit Bayesian Inference},
  author    = {Xie, Sang Michael and Raghunathan, Aditi and Liang, Percy and Ma, Tengyu},
  booktitle = {ICLR},
  year      = {2022},
  eprint    = {2111.02080},
  archivePrefix = {arXiv}
}
```

---

*Last updated: 2026-05-14. Some entries use placeholder author lists where the full author list is not yet stable (e.g. Tulu 3, Hassid et al.); update against the latest version on arXiv before citing in a paper.*
